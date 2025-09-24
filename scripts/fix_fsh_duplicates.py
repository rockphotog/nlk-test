#!/usr/bin/env python3
"""
Fix FSH duplicate concepts by handling temporal versions appropriately.

For concepts with the same code but different validity periods, we need to:
1. Keep the currently valid version (without end date or with future end date)
2. Mark historical versions as inactive or with appropriate properties
3. Ensure no duplicate concept codes in the final FSH
"""

import pandas as pd
import sys
from pathlib import Path
from datetime import datetime

def load_csv_data(csv_path):
    """Load and analyze the CSV data for duplicates."""
    print(f"Loading CSV data from: {csv_path}")
    
    # Load CSV
    df = pd.read_csv(csv_path)
    print(f"Total rows: {len(df)}")
    
    # Find duplicates by code (first column)
    code_column = df.columns[0]
    duplicates = df[df.duplicated(subset=[code_column], keep=False)]
    
    if len(duplicates) > 0:
        print(f"\nFound {len(duplicates)} duplicate rows for {duplicates[code_column].nunique()} unique codes")
        
        # Group by code and show details
        for code in duplicates[code_column].unique():
            code_rows = df[df[code_column] == code]
            print(f"\nCode {code} has {len(code_rows)} versions:")
            for idx, row in code_rows.iterrows():
                valid_from = row.iloc[1] if pd.notna(row.iloc[1]) else "None"
                valid_to = row.iloc[2] if pd.notna(row.iloc[2]) else "None" 
                print(f"  Row {idx}: Valid from {valid_from} to {valid_to}")
    
    return df, duplicates

def select_active_versions(df):
    """
    For duplicate codes, select the active version:
    - Prefer versions without end date (currently active)
    - If multiple versions without end date, prefer the one with latest start date
    - If all versions have end dates, prefer the one with latest end date
    """
    code_column = df.columns[0]
    valid_from_column = df.columns[1]  
    valid_to_column = df.columns[2]
    
    # Find duplicates
    duplicates = df[df.duplicated(subset=[code_column], keep=False)]
    duplicate_codes = duplicates[code_column].unique()
    
    # Start with all non-duplicate rows
    result_df = df[~df[code_column].isin(duplicate_codes)].copy()
    
    print(f"\nProcessing {len(duplicate_codes)} duplicate codes...")
    
    for code in duplicate_codes:
        code_rows = df[df[code_column] == code].copy()
        
        # Convert dates for comparison
        code_rows['valid_from_dt'] = pd.to_datetime(code_rows[valid_from_column], errors='coerce')
        code_rows['valid_to_dt'] = pd.to_datetime(code_rows[valid_to_column], errors='coerce')
        
        # Rule 1: Prefer versions without end date (active)
        active_versions = code_rows[code_rows['valid_to_dt'].isna()]
        
        if len(active_versions) > 0:
            # If multiple active versions, choose the one with latest start date
            if len(active_versions) > 1:
                selected = active_versions.loc[active_versions['valid_from_dt'].idxmax()]
                print(f"  {code}: Selected active version with latest start date")
            else:
                selected = active_versions.iloc[0]
                print(f"  {code}: Selected single active version")
        else:
            # Rule 2: All versions have end dates, choose the one with latest end date
            selected = code_rows.loc[code_rows['valid_to_dt'].idxmax()]
            print(f"  {code}: Selected version with latest end date")
        
        # Add selected version to result
        result_df = pd.concat([result_df, selected.to_frame().T], ignore_index=True)
    
    # Remove temporary columns
    result_df = result_df.drop(columns=['valid_from_dt', 'valid_to_dt'], errors='ignore')
    
    print(f"\nReduced from {len(df)} to {len(result_df)} rows")
    return result_df

def main():
    csv_path = Path("nlk-test/resources/csv_output/norsk_laboratoriekodeverk_7280.77-clean_full_cleaned.csv")
    
    if not csv_path.exists():
        print(f"Error: CSV file not found: {csv_path}")
        return 1
    
    # Load and analyze data
    df, duplicates = load_csv_data(csv_path)
    
    if len(duplicates) == 0:
        print("No duplicates found in CSV data")
        return 0
    
    # Select active versions
    cleaned_df = select_active_versions(df)
    
    # Save cleaned CSV
    output_path = csv_path.parent / "norsk_laboratoriekodeverk_7280.77-clean_full_deduplicated.csv"
    cleaned_df.to_csv(output_path, index=False)
    print(f"\nSaved deduplicated CSV to: {output_path}")
    
    # Verify no duplicates remain
    code_column = cleaned_df.columns[0]
    remaining_duplicates = cleaned_df[cleaned_df.duplicated(subset=[code_column], keep=False)]
    
    if len(remaining_duplicates) == 0:
        print("✓ No duplicates remain in cleaned data")
    else:
        print(f"⚠ Warning: {len(remaining_duplicates)} duplicates still remain!")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())