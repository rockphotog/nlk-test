#!/usr/bin/env python3
"""
Norwegian Laboratory Codebook CSV Data Processor
Optimized for working with the converted CSV dataset
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging
from typing import Optional, List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class NLKDataProcessor:
    """
    High-performance processor for Norwegian Laboratory Codebook CSV data
    Optimized for large datasets with efficient memory usage
    """
    
    def __init__(self, csv_path: str):
        """
        Initialize with CSV file path
        
        Args:
            csv_path: Path to the processing-optimized CSV file
        """
        self.csv_path = Path(csv_path)
        self.df: Optional[pd.DataFrame] = None
        self._load_data()
    
    def _load_data(self) -> None:
        """Load and optimize CSV data for processing"""
        try:
            logger.info(f"Loading CSV data from: {self.csv_path}")
            
            # Load with optimized settings for large datasets
            self.df = pd.read_csv(
                self.csv_path,
                encoding='utf-8',
                low_memory=False,  # Read entire file for consistent dtypes
                na_values=['', 'None', 'null'],  # Treat these as NaN
                keep_default_na=True
            )
            
            # Convert date columns
            date_columns = ['gyldig_fra', 'gyldig_til', 'endringsdato']
            for col in date_columns:
                if col in self.df.columns:
                    self.df[col] = pd.to_datetime(self.df[col], errors='coerce')
            
            logger.info(f"Loaded {len(self.df):,} records with {len(self.df.columns)} columns")
            
        except Exception as e:
            logger.error(f"Error loading CSV data: {str(e)}")
            raise
    
    def get_active_codes(self) -> pd.DataFrame:
        """Get all currently active laboratory codes"""
        if self.df is None:
            raise ValueError("Data not loaded")
        
        current_date = pd.Timestamp.now()
        
        # Active codes: gyldig_fra <= now AND (gyldig_til is null OR gyldig_til >= now)
        active_mask = (
            (self.df['gyldig_fra'] <= current_date) &
            (self.df['gyldig_til'].isna() | (self.df['gyldig_til'] >= current_date))
        )
        
        return self.df[active_mask].copy()
    
    def get_historical_codes(self) -> pd.DataFrame:
        """Get all historical (no longer active) laboratory codes"""
        if self.df is None:
            raise ValueError("Data not loaded")
        
        current_date = pd.Timestamp.now()
        
        # Historical codes: gyldig_til < now
        historical_mask = (
            self.df['gyldig_til'].notna() &
            (self.df['gyldig_til'] < current_date)
        )
        
        return self.df[historical_mask].copy()
    
    def get_codes_by_domain(self, domain: str) -> pd.DataFrame:
        """
        Get codes by medical domain (fagområde)
        
        Args:
            domain: Medical domain name (e.g., 'Medisinsk biokjemi')
        """
        if self.df is None:
            raise ValueError("Data not loaded")
        
        domain_mask = (
            self.df['primært_fagområde'].str.contains(domain, case=False, na=False) |
            self.df['sekundært_fagområde'].str.contains(domain, case=False, na=False)
        )
        
        return self.df[domain_mask].copy()
    
    def search_codes(self, search_term: str, columns: List[str] = None) -> pd.DataFrame:
        """
        Search for codes containing a specific term
        
        Args:
            search_term: Term to search for
            columns: List of columns to search in (default: all text columns)
        """
        if self.df is None:
            raise ValueError("Data not loaded")
        
        if columns is None:
            # Search in main descriptive columns
            columns = [
                'kode', 'norsk_bruksnavn', 'kodedefinisjon', 
                'komponent', 'system', 'egenskapsart'
            ]
        
        # Create search mask across specified columns
        search_mask = pd.Series([False] * len(self.df))
        
        for col in columns:
            if col in self.df.columns:
                search_mask |= self.df[col].str.contains(
                    search_term, case=False, na=False
                )
        
        return self.df[search_mask].copy()
    
    def get_domain_statistics(self) -> Dict[str, Any]:
        """Get statistical breakdown by medical domain"""
        if self.df is None:
            raise ValueError("Data not loaded")
        
        domain_stats = {}
        
        # Count by primary domain
        primary_counts = self.df['primært_fagområde'].value_counts()
        
        # Count active vs historical by domain
        active_df = self.get_active_codes()
        historical_df = self.get_historical_codes()
        
        for domain in primary_counts.index:
            domain_total = primary_counts[domain]
            domain_active = len(active_df[active_df['primært_fagområde'] == domain])
            domain_historical = len(historical_df[historical_df['primært_fagområde'] == domain])
            
            domain_stats[domain] = {
                'total': domain_total,
                'active': domain_active,
                'historical': domain_historical,
                'percentage': (domain_total / len(self.df)) * 100
            }
        
        return domain_stats
    
    def export_filtered_data(self, filtered_df: pd.DataFrame, 
                           output_path: str, format: str = 'csv') -> str:
        """
        Export filtered data to file
        
        Args:
            filtered_df: Filtered DataFrame to export
            output_path: Output file path
            format: Export format ('csv', 'excel', 'json')
        """
        output_file = Path(output_path)
        
        if format.lower() == 'csv':
            filtered_df.to_csv(output_file, index=False, encoding='utf-8')
        elif format.lower() == 'excel':
            filtered_df.to_excel(output_file, index=False, engine='openpyxl')
        elif format.lower() == 'json':
            filtered_df.to_json(output_file, orient='records', indent=2)
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        logger.info(f"Exported {len(filtered_df):,} records to {output_file}")
        return str(output_file)
    
    def generate_fsh_codesystem(self, output_path: str = None) -> str:
        """
        Generate FSH CodeSystem definition from CSV data
        
        Args:
            output_path: Output file path (default: auto-generated)
        """
        if self.df is None:
            raise ValueError("Data not loaded")
        
        if output_path is None:
            output_path = "nlk_codesystem_from_csv.fsh"
        
        # Get active codes only
        active_df = self.get_active_codes()
        
        # Remove duplicates based on code
        unique_codes = active_df.drop_duplicates(subset=['kode'], keep='first')
        
        logger.info(f"Generating FSH for {len(unique_codes):,} unique active codes")
        
        # Generate FSH content
        fsh_content = f'''// Norwegian Laboratory Codebook (Norsk Laboratoriekodeverk)
// Generated from CSV: {self.csv_path.name}
// Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
// Active concepts: {len(unique_codes)}

CodeSystem: NorskLaboratoriekodeverk
Id: norsk-laboratoriekodeverk
Title: "Norsk Laboratoriekodeverk"
Description: "Norwegian Laboratory Codebook - comprehensive terminology for laboratory medicine in Norway"
* ^url = "http://hl7.no/fhir/ig/nlk-test/CodeSystem/norsk-laboratoriekodeverk"
* ^version = "7280.77"
* ^status = #active
* ^experimental = false
* ^date = "{pd.Timestamp.now().strftime('%Y-%m-%d')}"
* ^publisher = "Espen"
* ^contact.name = "Espen"
* ^jurisdiction = urn:iso:std:iso:3166#NO "Norway"
* ^caseSensitive = true
* ^content = #complete
* ^count = {len(unique_codes)}

'''
        
        # Add concept definitions
        for _, row in unique_codes.iterrows():
            code = str(row['kode']).strip()
            display = str(row['norsk_bruksnavn']).strip() if pd.notna(row['norsk_bruksnavn']) else code
            
            # Clean display name for FSH
            display = display.replace('"', '\\"')
            
            fsh_content += f'* #{code} "{display}"\n'
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(fsh_content)
        
        logger.info(f"Generated FSH CodeSystem: {output_path}")
        return output_path

def main():
    """Example usage of the NLK data processor"""
    
    # Initialize processor with CSV file
    csv_file = "../nlk-test/resources/csv_output/norsk_laboratoriekodeverk_7280.77-clean_processing.csv"
    
    if not Path(csv_file).exists():
        print(f"CSV file not found: {csv_file}")
        print("Please run the Excel to CSV conversion first.")
        return
    
    print("🔬 Norwegian Laboratory Codebook - CSV Data Processor")
    print("=" * 60)
    
    # Load data
    processor = NLKDataProcessor(csv_file)
    
    # Get basic statistics
    total_codes = len(processor.df)
    active_codes = len(processor.get_active_codes())
    historical_codes = len(processor.get_historical_codes())
    
    print(f"\n📊 Dataset Overview:")
    print(f"   Total codes: {total_codes:,}")
    print(f"   Active codes: {active_codes:,}")
    print(f"   Historical codes: {historical_codes:,}")
    
    # Domain statistics
    print(f"\n🧬 Medical Domain Breakdown:")
    domain_stats = processor.get_domain_statistics()
    for domain, stats in domain_stats.items():
        print(f"   {domain}: {stats['total']:,} codes ({stats['percentage']:.1f}%)")
    
    # Generate FSH CodeSystem
    print(f"\n🍣 Generating FSH CodeSystem...")
    fsh_file = processor.generate_fsh_codesystem("nlk_from_csv.fsh")
    print(f"   Created: {fsh_file}")
    
    print(f"\n✅ Processing completed successfully!")

if __name__ == "__main__":
    main()