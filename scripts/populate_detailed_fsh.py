#!/usr/bin/env python3
"""
Populate NLK FSH CodeSystem with Enhanced Properties from CSV

This script reads the cleaned NLK CSV data and generates a complete FSH CodeSystem
that matches the existing structure but includes all available metadata as properties
for each concept.
"""

import pandas as pd
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import sys
import os

# Add scripts directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class NLKDetailedFSHPopulator:
    """Populates the existing NLK detailed FSH CodeSystem with complete metadata."""
    
    def __init__(self, csv_path: str):
        """Initialize with path to cleaned CSV file."""
        self.csv_path = Path(csv_path)
        self.df: Optional[pd.DataFrame] = None
    
    def load_data(self) -> bool:
        """Load and validate CSV data."""
        try:
            logger.info(f"Loading CSV data from: {self.csv_path}")
            
            self.df = pd.read_csv(
                self.csv_path,
                encoding='utf-8',
                parse_dates=['gyldig_fra', 'gyldig_til', 'endringsdato'],
                date_format='ISO8601'
            )
            
            logger.info(f"Loaded {len(self.df)} records with {len(self.df.columns)} columns")
            
            # Validate required columns
            required_columns = ['kode', 'norsk_bruksnavn', 'gyldig_fra']
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
    
    def generate_populated_concept(self, row: pd.Series) -> str:
        """Generate populated FSH concept with all available properties."""
        
        code = row['kode']
        display = row['norsk_bruksnavn']
        definition = row.get('kodedefinisjon', '')
        
        # Start concept definition
        concept = f'* #{code} "{display}"'
        
        # Add definition if available
        if not pd.isna(definition) and definition.strip():
            concept += f'\n  * ^definition = {self._escape_fsh_string(definition)}'
        
        # Build properties list
        properties = []
        
        # Temporal properties from CSV columns
        if not pd.isna(row['gyldig_fra']):
            valid_from = self._format_datetime(row['gyldig_fra'])
            properties.append(f'    * code = #validFrom\n    * valueDateTime = "{valid_from}"')
        
        if not pd.isna(row['gyldig_til']):
            valid_to = self._format_datetime(row['gyldig_til'])
            properties.append(f'    * code = #validTo\n    * valueDateTime = "{valid_to}"')
        
        if not pd.isna(row['erstattes_av']):
            properties.append(f'    * code = #replacedBy\n    * valueCode = #{row["erstattes_av"]}')
        
        if not pd.isna(row['endringsdato']):
            change_date = self._format_datetime(row['endringsdato'])
            properties.append(f'    * code = #changeDate\n    * valueDateTime = "{change_date}"')
        
        # Laboratory-specific properties
        lab_properties = [
            ('kodedefinisjon', 'codeDefinition'),
            ('komponent', 'component'),
            ('komponent_spesifikasjon', 'componentSpec'),
            ('system', 'system'),
            ('system_spesifikasjon', 'systemSpec'),
            ('egenskapsart', 'propertyType'),
            ('egenskapsart_spesifikasjon', 'propertySpec'),
            ('enhet', 'unit'),
            ('primært_fagområde', 'primaryDomain'),
            ('sekundært_fagområde', 'secondaryDomain'),
            ('gruppering', 'grouping')
        ]
        
        for csv_col, fsh_prop in lab_properties:
            if csv_col in row and not pd.isna(row[csv_col]) and str(row[csv_col]).strip():
                # Skip kodedefinisjon if already used as definition
                if csv_col == 'kodedefinisjon' and not pd.isna(definition) and definition.strip():
                    continue
                    
                value = self._escape_fsh_string(str(row[csv_col]).strip())
                properties.append(f'    * code = #{fsh_prop}\n    * valueString = {value}')
        
        # Add all properties to concept
        if properties:
            for prop in properties:
                concept += '\n  * ^property[+]\n' + prop
        
        return concept
    
    def generate_populated_fsh(self, output_file: str) -> None:
        """Generate the populated FSH CodeSystem."""
        
        if not self.load_data():
            logger.error("Failed to load data")
            return
        
        logger.info("Generating populated FSH CodeSystem...")
        
        # Count active/retired concepts
        active_count = 0
        retired_count = 0
        
        for _, row in self.df.iterrows():
            status = self._get_concept_status(row)
            if status == 'active':
                active_count += 1
            elif status == 'retired':
                retired_count += 1
        
        total_count = len(self.df)
        
        # Generate FSH header that matches existing structure
        fsh_content = f'''// Norwegian Laboratory Codebook (Norsk Laboratoriekodeverk) - Enhanced with Complete Properties
// Generated from: {self.csv_path.name}
// Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
// Total concepts: {total_count}
// Active concepts: {active_count}
// Retired concepts: {retired_count}

CodeSystem: NorskLaboratoriekodeverkDetailed
Id: norsk-laboratoriekodeverk-detailed
Title: "Norsk Laboratoriekodeverk"
Description: "Norwegian Laboratory Codebook - a comprehensive terminology for laboratory medicine in Norway with complete metadata properties"
* ^url = "http://hl7.no/fhir/ig/nlk-test/CodeSystem/norsk-laboratoriekodeverk-detailed"
* ^version = "7280.77"
* ^status = #active
* ^experimental = true
* ^date = "{datetime.now().strftime('%Y-%m-%d')}"
* ^publisher = "Espen"
* ^contact.name = "Espen"
* ^jurisdiction = urn:iso:std:iso:3166#NO "Norway"
* ^caseSensitive = true
* ^content = #complete
* ^count = {total_count}

// Properties for additional metadata
* ^property[0].code = #validFrom
* ^property[=].description = "Valid from date"
* ^property[=].type = #dateTime

* ^property[+].code = #validTo
* ^property[=].description = "Valid to date"
* ^property[=].type = #dateTime

* ^property[+].code = #replacedBy
* ^property[=].description = "Code that replaces this code"
* ^property[=].type = #code

* ^property[+].code = #changeDate
* ^property[=].description = "Date of last change"
* ^property[=].type = #dateTime

* ^property[+].code = #codeDefinition
* ^property[=].description = "Technical code definition"
* ^property[=].type = #string

* ^property[+].code = #component
* ^property[=].description = "Component being measured"
* ^property[=].type = #string

* ^property[+].code = #componentSpec
* ^property[=].description = "Component specification"
* ^property[=].type = #string

* ^property[+].code = #system
* ^property[=].description = "System/specimen type"
* ^property[=].type = #string

* ^property[+].code = #systemSpec
* ^property[=].description = "System specification"
* ^property[=].type = #string

* ^property[+].code = #propertyType
* ^property[=].description = "Type of property measured"
* ^property[=].type = #string

* ^property[+].code = #propertySpec
* ^property[=].description = "Property specification"
* ^property[=].type = #string

* ^property[+].code = #unit
* ^property[=].description = "Unit of measurement"
* ^property[=].type = #string

* ^property[+].code = #primaryDomain
* ^property[=].description = "Primary medical domain"
* ^property[=].type = #string

* ^property[+].code = #secondaryDomain
* ^property[=].description = "Secondary medical domain"
* ^property[=].type = #string

* ^property[+].code = #grouping
* ^property[=].description = "Grouping category"
* ^property[=].type = #string

// Concepts with complete properties
'''
        
        # Process concepts in order
        concepts_df = self.df.sort_values('kode')
        concept_count = 0
        
        logger.info(f"Processing {len(concepts_df)} concepts...")
        
        for _, row in concepts_df.iterrows():
            try:
                concept_fsh = self.generate_populated_concept(row)
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
        
        logger.info(f"Populated FSH CodeSystem written to: {output_path}")
        logger.info(f"Total concepts processed: {concept_count:,}")
        
        # Generate statistics
        logger.info("📊 Populated CodeSystem Statistics:")
        logger.info(f"   Total concepts: {total_count:,}")
        logger.info(f"   Active concepts: {active_count:,} ({active_count/total_count*100:.1f}%)")
        logger.info(f"   Retired concepts: {retired_count:,} ({retired_count/total_count*100:.1f}%)")
        
        # Property completeness
        logger.info(f"\n📋 Property Completeness:")
        metadata_cols = ['kodedefinisjon', 'komponent', 'system', 'egenskapsart', 'enhet', 'gruppering']
        for col in metadata_cols:
            if col in self.df.columns:
                completeness = (1 - self.df[col].isna().sum() / total_count) * 100
                logger.info(f"   {col}: {completeness:.1f}%")


def main():
    """Main function to populate the detailed NLK CodeSystem."""
    
    # Path to deduplicated CSV file (use command line arg if provided)
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    else:
        csv_file = "../nlk-test/resources/csv_output/norsk_laboratoriekodeverk_7280.77-clean_full_deduplicated.csv"
    
    if not Path(csv_file).exists():
        print(f"❌ CSV file not found: {csv_file}")
        print("Please ensure the file exists and run this script from the scripts directory.")
        return
    
    print("🧬 Norwegian Laboratory Codebook - Populate FSH with Complete Properties")
    print("=" * 80)
    
    # Output file (use command line arg if provided)
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        output_file = "nlk-detailed-populated.fsh"
    
    # Generate populated CodeSystem
    populator = NLKDetailedFSHPopulator(csv_file)
    populator.generate_populated_fsh(output_file)
    
    print("\n✅ FSH CodeSystem population completed!")
    print("\nFeatures added to each concept:")
    print("  🔹 Complete temporal validity (validFrom, validTo, changeDate)")
    print("  🔹 Replacement relationships (replacedBy)")
    print("  🔹 Laboratory metadata (component, system, property, unit)")
    print("  🔹 Medical domain classifications")
    print("  🔹 Technical definitions and specifications")


if __name__ == "__main__":
    main()