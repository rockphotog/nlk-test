#!/usr/bin/env python3
"""
Enhanced NLK CSV to FSH CodeSystem Generator

This script generates a comprehensive FHIR CodeSystem from the Norwegian Laboratory Codebook
CSV data, including all available metadata as CodeSystem properties and concept details.

Features:
- Rich concept properties (component, system, unit, domain, etc.)
- Proper FHIR CodeSystem structure with typed properties
- Status tracking (active/retired)
- Replacement relationships
- Temporal validity periods
"""

import pandas as pd
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class EnhancedNLKFSHGenerator:
    """Enhanced generator for NLK FHIR CodeSystem with complete metadata."""
    
    def __init__(self, csv_path: str):
        """Initialize with path to cleaned CSV file."""
        self.csv_path = Path(csv_path)
        self.df: Optional[pd.DataFrame] = None
        
        # FHIR CodeSystem property definitions
        self.properties = {
            'status': {'type': 'code', 'description': 'Status of the concept (active|retired)'},
            'effectiveDate': {'type': 'dateTime', 'description': 'Date when the concept became effective'},
            'expirationDate': {'type': 'dateTime', 'description': 'Date when the concept expires'},
            'lastModified': {'type': 'dateTime', 'description': 'Date of last modification'},
            'replacedBy': {'type': 'code', 'description': 'Code that replaces this concept'},
            'component': {'type': 'string', 'description': 'Laboratory component being measured'},
            'componentSpec': {'type': 'string', 'description': 'Component specification details'},
            'system': {'type': 'string', 'description': 'Biological system or specimen type'},
            'systemSpec': {'type': 'string', 'description': 'System specification details'},
            'property': {'type': 'string', 'description': 'Type of property being measured'},
            'propertySpec': {'type': 'string', 'description': 'Property specification details'},
            'unit': {'type': 'string', 'description': 'Unit of measurement'},
            'primaryDomain': {'type': 'string', 'description': 'Primary medical domain'},
            'secondaryDomain': {'type': 'string', 'description': 'Secondary medical domain'},
            'grouping': {'type': 'string', 'description': 'Laboratory test grouping category'}
        }
    
    def load_data(self) -> bool:
        """Load and validate CSV data."""
        try:
            logger.info(f"Loading enhanced CSV data from: {self.csv_path}")
            
            self.df = pd.read_csv(
                self.csv_path,
                encoding='utf-8',
                parse_dates=['gyldig_fra', 'gyldig_til', 'endringsdato'],
                date_format='ISO8601'
            )
            
            logger.info(f"Loaded {len(self.df)} records with {len(self.df.columns)} columns")
            
            # Validate required columns
            required_columns = ['kode', 'norsk_bruksnavn', 'gyldig_fra', 'primært_fagområde']
            missing_columns = [col for col in required_columns if col not in self.df.columns]
            
            if missing_columns:
                logger.error(f"Missing required columns: {missing_columns}")
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Error loading CSV data: {e}")
            return False
    
    def _escape_fsh_string(self, text: str) -> str:
        """Escape text for safe use in FSH strings."""
        if pd.isna(text) or text == '':
            return '""'
        
        # Convert to string and clean
        text = str(text).strip()
        
        # Escape quotes and backslashes
        text = text.replace('\\', '\\\\').replace('"', '\\"')
        
        # Handle newlines
        text = text.replace('\n', '\\n').replace('\r', '\\r')
        
        return f'"{text}"'
    
    def _format_datetime(self, dt: pd.Timestamp) -> str:
        """Format datetime for FHIR."""
        if pd.isna(dt):
            return None
        return dt.strftime('%Y-%m-%dT%H:%M:%S+00:00')
    
    def _get_concept_status(self, row: pd.Series) -> str:
        """Determine concept status based on validity dates."""
        now = pd.Timestamp.now()
        
        # Check if expired
        if not pd.isna(row['gyldig_til']) and row['gyldig_til'] < now:
            return 'retired'
        
        # Check if not yet effective
        if not pd.isna(row['gyldig_fra']) and row['gyldig_fra'] > now:
            return 'draft'
        
        return 'active'
    
    def generate_codesystem_header(self) -> str:
        """Generate FSH CodeSystem header with property definitions."""
        
        active_count = len(self.df[self.df.apply(lambda row: self._get_concept_status(row) == 'active', axis=1)])
        total_count = len(self.df)
        
        header = f'''
// Norwegian Laboratory Codebook (NLK) - Enhanced FHIR CodeSystem
// Generated from: {self.csv_path.name}
// Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
// 
// Total concepts: {total_count:,}
// Active concepts: {active_count:,}
// Retired concepts: {total_count - active_count:,}

CodeSystem: NorskLaboratoriekodeverk
Id: norsk-laboratoriekodeverk
Title: "Norsk Laboratoriekodeverk (NLK)"
Description: """Enhanced Norwegian Laboratory Codebook containing {total_count:,} laboratory test codes with comprehensive metadata including components, systems, properties, units, and medical domains. Generated from official source data version 7280.77."""
* ^url = "http://ehelse.no/fhir/CodeSystem/norsk-laboratoriekodeverk"
* ^version = "7280.77"
* ^status = #active
* ^experimental = true
* ^date = "{datetime.now().strftime('%Y-%m-%d')}"
* ^publisher = "Direktoratet for e-helse"
* ^contact.name = "Direktoratet for e-helse"
* ^jurisdiction = urn:iso:std:iso:3166#NO "Norway"
* ^copyright = "© Direktoratet for e-helse"
* ^caseSensitive = true
* ^content = #complete
* ^count = {total_count}

// Property definitions for enhanced metadata
'''
        
        # Add property definitions
        for prop_code, prop_def in self.properties.items():
            header += f'* ^property[+].code = #{prop_code}\n'
            header += f'* ^property[=].type = #{prop_def["type"]}\n'
            header += f'* ^property[=].description = "{prop_def["description"]}"\n\n'
        
        return header
    
    def generate_concept(self, row: pd.Series) -> str:
        """Generate enhanced FSH concept with all available properties."""
        
        code = row['kode']
        display = row['norsk_bruksnavn']
        definition = row.get('kodedefinisjon', '')
        status = self._get_concept_status(row)
        
        # Start concept definition
        concept = f'* #{code} "{display}"\n'
        
        # Add definition if available
        if not pd.isna(definition) and definition.strip():
            concept += f'  * ^definition = {self._escape_fsh_string(definition)}\n'
        
        # Add properties
        properties = []
        
        # Status
        properties.append(f'    * code = #status\n    * valueCode = #{status}')
        
        # Temporal properties
        if not pd.isna(row['gyldig_fra']):
            effective_date = self._format_datetime(row['gyldig_fra'])
            properties.append(f'    * code = #effectiveDate\n    * valueDateTime = "{effective_date}"')
        
        if not pd.isna(row['gyldig_til']):
            expiration_date = self._format_datetime(row['gyldig_til'])
            properties.append(f'    * code = #expirationDate\n    * valueDateTime = "{expiration_date}"')
        
        if not pd.isna(row['endringsdato']):
            last_modified = self._format_datetime(row['endringsdato'])
            properties.append(f'    * code = #lastModified\n    * valueDateTime = "{last_modified}"')
        
        # Replacement relationship
        if not pd.isna(row['erstattes_av']):
            properties.append(f'    * code = #replacedBy\n    * valueCode = #{row["erstattes_av"]}')
        
        # Laboratory-specific properties
        lab_properties = [
            ('komponent', 'component'),
            ('komponent_spesifikasjon', 'componentSpec'),
            ('system', 'system'),
            ('system_spesifikasjon', 'systemSpec'),
            ('egenskapsart', 'property'),
            ('egenskapsart_spesifikasjon', 'propertySpec'),
            ('enhet', 'unit'),
            ('primært_fagområde', 'primaryDomain'),
            ('sekundært_fagområde', 'secondaryDomain'),
            ('gruppering', 'grouping')
        ]
        
        for csv_col, fhir_prop in lab_properties:
            if csv_col in row and not pd.isna(row[csv_col]) and str(row[csv_col]).strip():
                value = self._escape_fsh_string(str(row[csv_col]).strip())
                properties.append(f'    * code = #{fhir_prop}\n    * valueString = {value}')
        
        # Add all properties to concept
        if properties:
            for i, prop in enumerate(properties):
                if i == 0:
                    concept += '  * ^property[+]\n' + prop + '\n'
                else:
                    concept += '  * ^property[+]\n' + prop + '\n'
        
        return concept
    
    def generate_enhanced_fsh(self, output_file: str = "nlk_enhanced_codesystem.fsh") -> None:
        """Generate complete enhanced FSH CodeSystem."""
        
        if not self.load_data():
            logger.error("Failed to load data")
            return
        
        logger.info("Generating enhanced FSH CodeSystem...")
        
        # Filter active concepts (optional - include all for completeness)
        concepts_df = self.df.copy()
        
        # Sort by code for consistent output
        concepts_df = concepts_df.sort_values('kode')
        
        logger.info(f"Processing {len(concepts_df)} concepts...")
        
        # Generate FSH content
        fsh_content = self.generate_codesystem_header()
        fsh_content += "\n// Concept definitions\n"
        
        # Process concepts in batches for memory efficiency
        batch_size = 1000
        concept_count = 0
        
        for i in range(0, len(concepts_df), batch_size):
            batch = concepts_df.iloc[i:i + batch_size]
            
            for _, row in batch.iterrows():
                try:
                    concept_fsh = self.generate_concept(row)
                    fsh_content += concept_fsh + "\n"
                    concept_count += 1
                    
                    if concept_count % 500 == 0:
                        logger.info(f"Processed {concept_count:,} concepts...")
                        
                except Exception as e:
                    logger.warning(f"Error processing concept {row.get('kode', 'unknown')}: {e}")
                    continue
        
        # Write to file
        output_path = Path(output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(fsh_content)
        
        logger.info(f"Enhanced FSH CodeSystem generated: {output_path}")
        logger.info(f"Total concepts: {concept_count:,}")
        
        # Generate statistics
        self._generate_statistics()
    
    def _generate_statistics(self) -> None:
        """Generate and log statistics about the CodeSystem."""
        
        total_concepts = len(self.df)
        
        # Status distribution
        status_counts = {}
        for _, row in self.df.iterrows():
            status = self._get_concept_status(row)
            status_counts[status] = status_counts.get(status, 0) + 1
        
        logger.info("📊 Enhanced CodeSystem Statistics:")
        logger.info(f"   Total concepts: {total_concepts:,}")
        
        for status, count in status_counts.items():
            percentage = (count / total_concepts) * 100
            logger.info(f"   {status.title()} concepts: {count:,} ({percentage:.1f}%)")
        
        # Domain distribution
        domain_counts = self.df['primært_fagområde'].value_counts()
        logger.info(f"\n📈 Primary Domain Distribution:")
        for domain, count in domain_counts.head(10).items():
            percentage = (count / total_concepts) * 100
            logger.info(f"   {domain}: {count:,} ({percentage:.1f}%)")
        
        # Property completeness
        logger.info(f"\n📋 Metadata Completeness:")
        metadata_cols = ['kodedefinisjon', 'komponent', 'system', 'egenskapsart', 'enhet', 'gruppering']
        for col in metadata_cols:
            if col in self.df.columns:
                completeness = (1 - self.df[col].isna().sum() / total_concepts) * 100
                logger.info(f"   {col}: {completeness:.1f}%")


def main():
    """Main function to generate enhanced NLK CodeSystem."""
    
    # Path to cleaned CSV file
    csv_file = "../nlk-test/resources/csv_output/norsk_laboratoriekodeverk_7280.77-clean_full_cleaned.csv"
    
    if not Path(csv_file).exists():
        print(f"❌ CSV file not found: {csv_file}")
        print("Please ensure the file exists and run this script from the scripts directory.")
        return
    
    print("🧬 Enhanced Norwegian Laboratory Codebook - FSH CodeSystem Generator")
    print("=" * 80)
    
    # Generate enhanced CodeSystem
    generator = EnhancedNLKFSHGenerator(csv_file)
    generator.generate_enhanced_fsh("nlk_enhanced_codesystem.fsh")
    
    print("\n✅ Enhanced CodeSystem generation completed!")
    print("\nKey features of the enhanced CodeSystem:")
    print("  🔹 Complete metadata as CodeSystem properties")
    print("  🔹 Status tracking (active/retired/draft)")
    print("  🔹 Temporal validity periods")
    print("  🔹 Replacement relationships")
    print("  🔹 Laboratory-specific properties (component, system, units)")
    print("  🔹 Medical domain classifications")
    print("  🔹 FHIR R4 compliant structure")


if __name__ == "__main__":
    main()