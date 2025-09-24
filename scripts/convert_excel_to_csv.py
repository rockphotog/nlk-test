#!/usr/bin/env python3
"""
Convert Norwegian Laboratory Codebook Excel to optimized CSV format
Handles large datasets efficiently with proper encoding and data validation
"""

import pandas as pd
import numpy as np
import sys
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def convert_excel_to_csv(excel_path: str, output_dir: str = "output") -> dict:
    """
    Convert Excel file to optimized CSV format for large dataset processing
    
    Args:
        excel_path: Path to input Excel file
        output_dir: Directory for output files
        
    Returns:
        dict: Conversion statistics and file paths
    """
    
    try:
        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        logger.info(f"Reading Excel file: {excel_path}")
        
        # Read Excel file with optimizations for large datasets
        df = pd.read_excel(
            excel_path,
            engine='openpyxl',  # Better for .xlsx files
            dtype=str,  # Read all as strings initially to preserve data
            na_filter=False  # Don't convert to NaN, keep empty strings
        )
        
        logger.info(f"Loaded {len(df)} rows and {len(df.columns)} columns")
        
        # Data cleaning and optimization
        logger.info("Cleaning and optimizing data...")
        
        # Remove completely empty rows
        df = df.dropna(how='all')
        
        # Strip whitespace from all string columns
        df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
        
        # Replace empty strings with None for better CSV handling
        df = df.replace('', None)
        
        # Standardize column names (remove special characters, spaces)
        df.columns = [
            col.strip()
            .replace(' ', '_')
            .replace('(', '')
            .replace(')', '')
            .replace('-', '_')
            .replace('/', '_')
            .lower()
            for col in df.columns
        ]
        
        logger.info(f"Cleaned column names: {list(df.columns)}")
        
        # Generate output files
        base_name = Path(excel_path).stem.replace(' ', '_').lower()
        
        # 1. Full dataset CSV (UTF-8 with BOM for Excel compatibility)
        full_csv_path = output_path / f"{base_name}_full.csv"
        df.to_csv(
            full_csv_path,
            index=False,
            encoding='utf-8-sig',  # UTF-8 with BOM for Excel compatibility
            quoting=1,  # Quote all fields to handle special characters
            lineterminator='\n'  # Consistent line endings
        )
        logger.info(f"Saved full dataset: {full_csv_path}")
        
        # 2. Optimized CSV for processing (UTF-8, minimal quoting)
        processing_csv_path = output_path / f"{base_name}_processing.csv"
        df.to_csv(
            processing_csv_path,
            index=False,
            encoding='utf-8',
            quoting=0,  # Minimal quoting for faster processing
            lineterminator='\n'
        )
        logger.info(f"Saved processing-optimized CSV: {processing_csv_path}")
        
        # 3. Parquet format for high-performance analytics (optional)
        try:
            parquet_path = output_path / f"{base_name}.parquet"
            # Convert back to appropriate types for Parquet
            df_parquet = df.copy()
            
            # Try to optimize data types
            for col in df_parquet.columns:
                # Try to convert to numeric where possible
                try:
                    df_parquet[col] = pd.to_numeric(df_parquet[col], errors='ignore')
                except:
                    pass
            
            df_parquet.to_parquet(parquet_path, index=False, engine='pyarrow')
            logger.info(f"Saved Parquet format: {parquet_path}")
        except ImportError:
            logger.warning("Parquet support not available (install pyarrow for Parquet output)")
            parquet_path = None
        
        # 4. Generate data summary
        summary_path = output_path / f"{base_name}_summary.txt"
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(f"Norwegian Laboratory Codebook - Data Summary\n")
            f.write(f"Generated: {pd.Timestamp.now()}\n")
            f.write(f"Source: {excel_path}\n\n")
            
            f.write(f"Dataset Statistics:\n")
            f.write(f"- Total records: {len(df):,}\n")
            f.write(f"- Total columns: {len(df.columns)}\n")
            f.write(f"- Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB\n\n")
            
            f.write(f"Column Information:\n")
            for i, col in enumerate(df.columns, 1):
                non_null = df[col].count()
                f.write(f"{i:2d}. {col:<30} - {non_null:,} non-null values\n")
            
            f.write(f"\nData Quality:\n")
            f.write(f"- Duplicate rows: {df.duplicated().sum():,}\n")
            f.write(f"- Rows with all nulls: {df.isnull().all(axis=1).sum():,}\n")
            
            # Sample of first few rows for validation
            f.write(f"\nSample Data (first 3 rows):\n")
            f.write(df.head(3).to_string())
        
        logger.info(f"Saved data summary: {summary_path}")
        
        # Return conversion statistics
        return {
            'success': True,
            'input_file': excel_path,
            'output_files': {
                'full_csv': str(full_csv_path),
                'processing_csv': str(processing_csv_path),
                'parquet': str(parquet_path) if parquet_path else None,
                'summary': str(summary_path)
            },
            'statistics': {
                'rows': len(df),
                'columns': len(df.columns),
                'memory_mb': df.memory_usage(deep=True).sum() / 1024**2,
                'duplicates': df.duplicated().sum(),
                'column_names': list(df.columns)
            }
        }
        
    except Exception as e:
        logger.error(f"Error converting file: {str(e)}")
        return {
            'success': False,
            'error': str(e),
            'input_file': excel_path
        }

def main():
    """Main function for command line usage"""
    if len(sys.argv) < 2:
        print("Usage: python convert_excel_to_csv.py <excel_file> [output_directory]")
        print("Example: python convert_excel_to_csv.py 'Norsk Laboratoriekodeverk 7280.77.xlsx' csv_output")
        return
    
    excel_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "csv_output"
    
    if not Path(excel_file).exists():
        print(f"Error: Excel file '{excel_file}' not found")
        return
    
    print(f"Converting {excel_file} to CSV format...")
    result = convert_excel_to_csv(excel_file, output_dir)
    
    if result['success']:
        print("\n✅ Conversion completed successfully!")
        print(f"📊 Statistics:")
        print(f"   - Records: {result['statistics']['rows']:,}")
        print(f"   - Columns: {result['statistics']['columns']}")
        print(f"   - Memory: {result['statistics']['memory_mb']:.2f} MB")
        print(f"\n📁 Output files:")
        for file_type, path in result['output_files'].items():
            if path:
                print(f"   - {file_type}: {path}")
    else:
        print(f"❌ Conversion failed: {result['error']}")

if __name__ == "__main__":
    main()