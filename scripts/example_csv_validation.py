#!/usr/bin/env python3
"""
Example usage of CSV Quality Validator

This script demonstrates how to use the CSV quality validator
on the NLK dataset and other CSV files.
"""

from validate_csv_quality import CSVQualityValidator
import pandas as pd
from pathlib import Path


def validate_nlk_csv():
    """Validate the NLK CSV file and generate a report."""
    print("=== Validating Norwegian Laboratory Codebook CSV ===\n")
    
    # Path to the NLK CSV file
    csv_path = "../nlk-test/resources/csv_output/norsk_laboratoriekodeverk_7280.77-clean_full.csv"
    
    if not Path(csv_path).exists():
        print(f"❌ CSV file not found: {csv_path}")
        print("Please run convert_excel_to_csv.py first to create the CSV file.")
        return
    
    # Initialize validator
    validator = CSVQualityValidator(csv_path)
    
    # Run validation
    report = validator.run_full_validation()
    
    # Display summary
    print(f"📊 Validation Summary:")
    print(f"   Total Rows: {report.total_rows:,}")
    print(f"   Total Columns: {report.total_columns}")
    print(f"   Issues Found: {len(report.issues)}")
    print(f"   Duplicate Rows: {report.duplicate_rows_found}")
    print(f"   Empty Rows: {report.empty_rows_found}")
    print(f"   Whitespace Issues: {report.whitespace_issues_found}")
    print()
    
    # Show issues by severity
    critical = report.get_issues_by_severity('critical')
    warnings = report.get_issues_by_severity('warning')
    info = report.get_issues_by_severity('info')
    
    if critical:
        print(f"🔴 Critical Issues ({len(critical)}):")
        for issue in critical[:3]:  # Show first 3
            print(f"   • {issue.description}")
        print()
    
    if warnings:
        print(f"🟡 Warning Issues ({len(warnings)}):")
        for issue in warnings[:3]:  # Show first 3
            print(f"   • {issue.description}")
        print()
    
    if info:
        print(f"ℹ️  Info Issues ({len(info)}):")
        for issue in info[:3]:  # Show first 3
            print(f"   • {issue.description}")
        print()
    
    # Generate detailed report
    report_file = "../nlk_quality_report.txt"
    validator.generate_report(report_file)
    print(f"📄 Detailed report saved to: {report_file}")
    
    # Clean the data if there are issues to fix
    if warnings or critical:
        print("\n🧹 Cleaning data...")
        cleaned_df = validator.clean_data()
        
        output_file = "../nlk-test/resources/csv_output/norsk_laboratoriekodeverk_7280.77-clean_validated.csv"
        cleaned_df.to_csv(output_file, index=False, encoding='utf-8')
        
        print(f"✅ Cleaned CSV saved to: {output_file}")
        print(f"   Original rows: {report.total_rows:,}")
        print(f"   Cleaned rows: {len(cleaned_df):,}")
        print(f"   Rows removed: {report.total_rows - len(cleaned_df):,}")


def create_sample_problematic_csv():
    """Create a sample CSV with common data quality issues for testing."""
    print("=== Creating Sample Problematic CSV for Testing ===\n")
    
    # Sample data with various quality issues
    sample_data = {
        'ID': ['001', '002', '003', '004', '004', '005', '  006  ', '', '007'],
        'Name': ['John Doe', 'jane smith', 'JANE SMITH', 'Bob  Wilson', 'Bob Wilson', 'Alice Brown\t', '  Charlie Davis  ', 'NULL', 'Eve White\n'],
        'Email': ['john@test.com', 'jane.smith@email', 'invalid-email', 'bob@company.com', 'bob@company.com', 'alice@test.com', '', 'N/A', 'eve@test.com'],
        'Age': ['25', '30.0', 'thirty', '45', '45', '22', '35', '', '28'],
        'Date': ['2023-01-15', '15/01/2023', '2023/01/15', '2023-01-20', '2023-01-20', 'invalid-date', '', '2023-01-25', '2023-01-30'],
        'Notes': ['Good employee', 'needs training', 'NEEDS TRAINING', 'experienced worker', 'experienced worker', '', '   great performance   ', 'na', 'new hire'],
        'Unnamed: 6': ['', '', '', '', '', '', '', '', '']  # Empty column
    }
    
    df = pd.DataFrame(sample_data)
    
    # Add some completely empty rows
    empty_row = pd.DataFrame([{col: '' for col in df.columns}] * 2)
    df = pd.concat([df, empty_row], ignore_index=True)
    
    # Save the problematic CSV
    output_file = "samples/sample_problematic_data.csv"
    df.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"📁 Sample problematic CSV created: {output_file}")
    print("This file contains:")
    print("   • Duplicate rows")
    print("   • Inconsistent capitalization")
    print("   • Leading/trailing whitespace")
    print("   • Multiple spaces")
    print("   • Tab characters")
    print("   • Empty rows and columns")
    print("   • Invalid email formats")
    print("   • Mixed data types")
    print("   • Various null representations")
    print()
    
    return output_file


def validate_sample_csv(csv_file):
    """Validate the sample CSV and show the issues found."""
    print(f"=== Validating Sample CSV: {csv_file} ===\n")
    
    # Initialize validator
    validator = CSVQualityValidator(csv_file)
    
    # Run validation
    report = validator.run_full_validation()
    
    # Show all issues found
    print("🔍 Issues Found:")
    for issue in report.issues:
        severity_emoji = {'critical': '🔴', 'warning': '🟡', 'info': 'ℹ️'}
        print(f"{severity_emoji.get(issue.severity, '•')} {issue.description}")
        if issue.suggested_fix:
            print(f"   💡 Fix: {issue.suggested_fix}")
        print()
    
    # Clean and save
    print("🧹 Applying automatic fixes...")
    cleaned_df = validator.clean_data()
    
    cleaned_file = csv_file.replace('.csv', '_cleaned.csv')
    cleaned_df.to_csv(cleaned_file, index=False, encoding='utf-8')
    
    print(f"✅ Cleaned file saved: {cleaned_file}")
    print(f"   Original rows: {len(validator.original_df):,}")
    print(f"   Cleaned rows: {len(cleaned_df):,}")
    
    # Generate detailed report
    report_file = csv_file.replace('.csv', '_quality_report.txt')
    validator.generate_report(report_file)
    print(f"📄 Detailed report: {report_file}")


def main():
    """Main function to run validation examples."""
    print("CSV Quality Validator - Examples\n")
    
    # Example 1: Validate NLK CSV if it exists
    nlk_path = Path("../nlk-test/resources/csv_output/norsk_laboratoriekodeverk_7280.77-clean_full.csv")
    if nlk_path.exists():
        validate_nlk_csv()
        print("\n" + "="*80 + "\n")
    
    # Example 2: Create and validate sample problematic data
    sample_file = create_sample_problematic_csv()
    validate_sample_csv(sample_file)
    
    print("\n🎉 All examples completed!")
    print("\nTo validate your own CSV files:")
    print("   python validate_csv_quality.py your_file.csv --clean --report-file report.txt")


if __name__ == "__main__":
    main()