#!/usr/bin/env python3
"""
CSV Quality Validator Usage Examples

This script shows common usage patterns for the CSV quality validator.
"""

import pandas as pd
from validate_csv_quality import CSVQualityValidator


def show_usage_examples():
    """Demonstrate common usage patterns."""
    
    print("🔍 CSV Quality Validator - Usage Examples")
    print("=" * 60)
    
    print("\n1. Basic Validation (Command Line):")
    print("   python validate_csv_quality.py your_file.csv")
    
    print("\n2. Validation with Auto-Clean:")
    print("   python validate_csv_quality.py your_file.csv --clean")
    
    print("\n3. Custom Output Directory:")
    print("   python validate_csv_quality.py your_file.csv --clean --output-dir /path/to/output")
    
    print("\n4. Save Report to Specific File:")
    print("   python validate_csv_quality.py your_file.csv --report-file quality_report.txt")
    
    print("\n5. Programmatic Usage:")
    print("""
   from validate_csv_quality import CSVQualityValidator
   
   validator = CSVQualityValidator("your_file.csv")
   report = validator.run_full_validation()
   
   # Check issues
   critical = report.get_issues_by_severity('critical')
   if critical:
       print("⚠️  Critical issues found!")
   
   # Clean data
   cleaned_df = validator.clean_data()
   cleaned_df.to_csv("cleaned_file.csv", index=False)
    """)
    
    print("\n6. Common Issues Detected:")
    issues = [
        "✓ Exact duplicate rows",
        "✓ Duplicate key values", 
        "✓ Empty rows and columns",
        "✓ Leading/trailing whitespace",
        "✓ Multiple consecutive spaces",
        "✓ Tab characters and newlines",
        "✓ Non-breaking spaces",
        "✓ Inconsistent capitalization",
        "✓ Potential data type mismatches",
        "✓ Invalid column names",
        "✓ Encoding issues",
        "✓ Potential typos/similar values"
    ]
    
    for issue in issues:
        print(f"   {issue}")
    
    print("\n7. Automatic Fixes Applied:")
    fixes = [
        "• Remove exact duplicate rows",
        "• Remove completely empty rows", 
        "• Trim leading/trailing whitespace",
        "• Replace multiple spaces with single space",
        "• Replace tabs/newlines with spaces",
        "• Clean column names (trim whitespace)",
        "• Handle various null representations"
    ]
    
    for fix in fixes:
        print(f"   {fix}")


def check_nlk_data_quality():
    """Show specific quality insights for the NLK dataset."""
    
    csv_path = "../nlk-test/resources/csv_output/norsk_laboratoriekodeverk_7280.77-clean_full.csv"
    
    print("\n" + "=" * 60)
    print("🏥 NLK Dataset Quality Analysis")
    print("=" * 60)
    
    try:
        # Load the data
        df = pd.read_csv(csv_path)
        
        print(f"\n📊 Dataset Overview:")
        print(f"   Total Records: {len(df):,}")
        print(f"   Total Columns: {len(df.columns)}")
        print(f"   Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
        
        # Check data completeness
        print(f"\n📈 Data Completeness:")
        completeness = (1 - df.isnull().sum() / len(df)) * 100
        for col in df.columns:
            print(f"   {col:25} {completeness[col]:5.1f}%")
        
        # Check for potential data quality issues
        print(f"\n🔍 Quick Quality Check:")
        
        # Duplicates in key column
        key_col = 'kode'
        duplicates = df[key_col].duplicated().sum()
        print(f"   Duplicate {key_col} values: {duplicates}")
        
        # Empty values
        total_nulls = df.isnull().sum().sum()
        print(f"   Total null values: {total_nulls:,}")
        
        # Whitespace issues (sample check)
        sample_text_col = 'norsk_bruksnavn'
        if sample_text_col in df.columns:
            whitespace_issues = df[sample_text_col].astype(str).str.contains(r'^\s+|\s+$|  |\t|\n').sum()
            print(f"   Whitespace issues in {sample_text_col}: {whitespace_issues}")
        
        print(f"\n✅ Overall Assessment:")
        if duplicates == 0 and total_nulls < len(df) * len(df.columns) * 0.1:
            print("   🟢 Good - Data quality appears high")
        elif duplicates > 0 or total_nulls > len(df) * len(df.columns) * 0.2:
            print("   🟡 Fair - Some quality issues detected")
        else:
            print("   🔴 Poor - Significant quality issues found")
        
        print(f"\n💡 Recommendations:")
        if duplicates > 0:
            print(f"   • Review {duplicates} duplicate {key_col} values")
        if total_nulls > 1000:
            print(f"   • Investigate {total_nulls:,} missing values")
        print(f"   • Run full validation: python validate_csv_quality.py \"{csv_path}\"")
        
    except FileNotFoundError:
        print("   ❌ NLK CSV file not found")
        print("   💡 Run convert_excel_to_csv.py first to create the CSV file")
    except Exception as e:
        print(f"   ❌ Error analyzing data: {e}")


def show_validation_workflow():
    """Show recommended workflow for CSV validation."""
    
    print("\n" + "=" * 60) 
    print("📋 Recommended Validation Workflow")
    print("=" * 60)
    
    steps = [
        ("1. Initial Validation", "Identify all potential issues", 
         "python validate_csv_quality.py your_file.csv"),
        
        ("2. Review Report", "Analyze issues by severity",
         "cat your_file_quality_report.txt"),
        
        ("3. Auto-Clean", "Apply automatic fixes for common issues",
         "python validate_csv_quality.py your_file.csv --clean"),
        
        ("4. Manual Review", "Address remaining issues manually",
         "# Review critical and warning issues"),
        
        ("5. Re-validate", "Confirm all issues are resolved", 
         "python validate_csv_quality.py your_file_cleaned.csv"),
        
        ("6. Data Processing", "Proceed with analysis/processing",
         "# Use cleaned file for further processing")
    ]
    
    for step, description, command in steps:
        print(f"\n{step}: {description}")
        print(f"   Command: {command}")


if __name__ == "__main__":
    show_usage_examples()
    check_nlk_data_quality() 
    show_validation_workflow()
    
    print(f"\n🎯 Next Steps:")
    print(f"   1. Run validation on your CSV files")
    print(f"   2. Review generated reports")
    print(f"   3. Apply fixes as needed")
    print(f"   4. Use cleaned data for processing")
    print(f"\n📚 For more help: python validate_csv_quality.py --help")