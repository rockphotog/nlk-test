#!/usr/bin/env python3
"""
CSV Data Quality Validator and Cleaner

This script validates and cleans CSV files converted from hand-written Excel spreadsheets,
identifying and optionally fixing common data quality issues.

Author: Data Quality Team
Date: September 2024
"""

import pandas as pd
import numpy as np
import re
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


@dataclass
class ValidationIssue:
    """Represents a data quality issue found during validation."""
    issue_type: str
    severity: str  # 'critical', 'warning', 'info'
    description: str
    location: str  # row/column reference
    current_value: Any
    suggested_fix: Optional[Any] = None
    count: int = 1


@dataclass
class ValidationReport:
    """Contains all validation results and statistics."""
    total_rows: int = 0
    total_columns: int = 0
    issues: List[ValidationIssue] = field(default_factory=list)
    cleaned_rows: int = 0
    duplicate_rows_found: int = 0
    empty_rows_found: int = 0
    whitespace_issues_found: int = 0
    encoding_issues_found: int = 0
    date_format_issues: int = 0
    
    def add_issue(self, issue: ValidationIssue) -> None:
        """Add a validation issue to the report."""
        self.issues.append(issue)
    
    def get_issues_by_severity(self, severity: str) -> List[ValidationIssue]:
        """Get all issues of a specific severity level."""
        return [issue for issue in self.issues if issue.severity == severity]
    
    def get_summary(self) -> Dict[str, int]:
        """Get a summary of issues by type."""
        summary = {}
        for issue in self.issues:
            summary[issue.issue_type] = summary.get(issue.issue_type, 0) + issue.count
        return summary


class CSVQualityValidator:
    """Main class for validating and cleaning CSV data quality."""
    
    def __init__(self, csv_file_path: str, encoding: str = 'utf-8'):
        """
        Initialize the validator with a CSV file.
        
        Args:
            csv_file_path: Path to the CSV file to validate
            encoding: File encoding (default: utf-8)
        """
        self.csv_file_path = Path(csv_file_path)
        self.encoding = encoding
        self.df: Optional[pd.DataFrame] = None
        self.original_df: Optional[pd.DataFrame] = None
        self.report = ValidationReport()
        
        # Common patterns for validation
        self.email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        self.phone_pattern = re.compile(r'^[\+]?[1-9][\d\s\-\(\)]{7,15}$')
        self.whitespace_patterns = {
            'leading_trailing': re.compile(r'^\s+|\s+$'),
            'multiple_spaces': re.compile(r'\s{2,}'),
            'tabs': re.compile(r'\t'),
            'newlines': re.compile(r'[\n\r]'),
            'non_breaking_space': re.compile(r'\u00a0'),
        }
    
    def load_csv(self) -> bool:
        """
        Load the CSV file with error handling for common encoding issues.
        
        Returns:
            bool: True if successfully loaded, False otherwise
        """
        encodings_to_try = [self.encoding, 'utf-8', 'utf-8-sig', 'latin1', 'cp1252']
        
        for encoding in encodings_to_try:
            try:
                self.df = pd.read_csv(
                    self.csv_file_path,
                    encoding=encoding,
                    dtype=str,  # Load everything as strings initially
                    na_values=['', 'NULL', 'null', 'N/A', 'n/a', 'NA', 'na'],
                    keep_default_na=True
                )
                self.original_df = self.df.copy()
                self.encoding = encoding
                
                self.report.total_rows = len(self.df)
                self.report.total_columns = len(self.df.columns)
                
                if encoding != encodings_to_try[0]:
                    self.report.add_issue(ValidationIssue(
                        issue_type="encoding_detection",
                        severity="warning",
                        description=f"File encoding detected as {encoding}, not {encodings_to_try[0]}",
                        location="file_level",
                        current_value=encoding,
                        suggested_fix=f"Consider re-saving with {encoding} encoding"
                    ))
                
                return True
                
            except (UnicodeDecodeError, pd.errors.ParserError) as e:
                if encoding == encodings_to_try[-1]:
                    self.report.add_issue(ValidationIssue(
                        issue_type="file_loading_error",
                        severity="critical",
                        description=f"Could not load CSV file with any encoding: {str(e)}",
                        location="file_level",
                        current_value=str(e)
                    ))
                    return False
                continue
        
        return False
    
    def validate_duplicates(self) -> None:
        """Check for duplicate rows (exact and near-duplicates)."""
        if self.df is None:
            return
        
        # Exact duplicates
        duplicated_mask = self.df.duplicated()
        exact_duplicates = duplicated_mask.sum()
        
        if exact_duplicates > 0:
            self.report.duplicate_rows_found = exact_duplicates
            duplicate_indices = self.df[duplicated_mask].index.tolist()
            
            self.report.add_issue(ValidationIssue(
                issue_type="exact_duplicates",
                severity="warning",
                description=f"Found {exact_duplicates} exact duplicate rows",
                location=f"Rows: {duplicate_indices[:10]}{'...' if len(duplicate_indices) > 10 else ''}",
                current_value=exact_duplicates,
                suggested_fix="Remove duplicate rows",
                count=exact_duplicates
            ))
        
        # Near-duplicates (same key column values but different in other columns)
        if len(self.df.columns) > 1:
            # Assume first column is a key column
            key_column = self.df.columns[0]
            if not self.df[key_column].isna().all():
                duplicate_keys = self.df[key_column].duplicated()
                near_duplicates = duplicate_keys.sum()
                
                if near_duplicates > 0:
                    duplicate_key_indices = self.df[duplicate_keys].index.tolist()
                    self.report.add_issue(ValidationIssue(
                        issue_type="duplicate_keys",
                        severity="warning",
                        description=f"Found {near_duplicates} duplicate values in key column '{key_column}'",
                        location=f"Rows: {duplicate_key_indices[:10]}{'...' if len(duplicate_key_indices) > 10 else ''}",
                        current_value=near_duplicates,
                        suggested_fix=f"Review and consolidate records with duplicate {key_column} values",
                        count=near_duplicates
                    ))
    
    def validate_empty_rows_columns(self) -> None:
        """Check for completely empty rows and columns."""
        if self.df is None:
            return
        
        # Empty rows (all values are NaN)
        empty_rows_mask = self.df.isna().all(axis=1)
        empty_rows = empty_rows_mask.sum()
        
        if empty_rows > 0:
            self.report.empty_rows_found = empty_rows
            empty_row_indices = self.df[empty_rows_mask].index.tolist()
            
            self.report.add_issue(ValidationIssue(
                issue_type="empty_rows",
                severity="warning",
                description=f"Found {empty_rows} completely empty rows",
                location=f"Rows: {empty_row_indices}",
                current_value=empty_rows,
                suggested_fix="Remove empty rows",
                count=empty_rows
            ))
        
        # Empty columns (all values are NaN)
        empty_columns = []
        for col in self.df.columns:
            if self.df[col].isna().all():
                empty_columns.append(col)
        
        if empty_columns:
            self.report.add_issue(ValidationIssue(
                issue_type="empty_columns",
                severity="info",
                description=f"Found {len(empty_columns)} completely empty columns",
                location=f"Columns: {empty_columns}",
                current_value=empty_columns,
                suggested_fix="Consider removing empty columns",
                count=len(empty_columns)
            ))
    
    def validate_whitespace_issues(self) -> None:
        """Check for various whitespace problems in string columns."""
        if self.df is None:
            return
        
        whitespace_issues = 0
        
        for col in self.df.columns:
            # Skip if column is all NaN
            if self.df[col].isna().all():
                continue
            
            # Convert to string and check for whitespace issues
            string_series = self.df[col].astype(str)
            
            for pattern_name, pattern in self.whitespace_patterns.items():
                problematic_values = string_series[
                    string_series.str.contains(pattern, regex=True, na=False)
                ].index.tolist()
                
                if problematic_values:
                    issue_count = len(problematic_values)
                    whitespace_issues += issue_count
                    
                    severity = "warning" if pattern_name in ['leading_trailing', 'multiple_spaces'] else "info"
                    
                    self.report.add_issue(ValidationIssue(
                        issue_type=f"whitespace_{pattern_name}",
                        severity=severity,
                        description=f"Found {issue_count} values with {pattern_name.replace('_', ' ')} in column '{col}'",
                        location=f"Column: {col}, Rows: {problematic_values[:5]}{'...' if len(problematic_values) > 5 else ''}",
                        current_value=issue_count,
                        suggested_fix=f"Clean {pattern_name.replace('_', ' ')} whitespace",
                        count=issue_count
                    ))
        
        self.report.whitespace_issues_found = whitespace_issues
    
    def validate_column_names(self) -> None:
        """Check for issues with column names."""
        if self.df is None:
            return
        
        issues_found = []
        
        for i, col in enumerate(self.df.columns):
            # Check for unnamed columns
            if col.startswith('Unnamed:'):
                issues_found.append(f"Column {i}: {col}")
                self.report.add_issue(ValidationIssue(
                    issue_type="unnamed_column",
                    severity="warning",
                    description=f"Found unnamed column: {col}",
                    location=f"Column index {i}",
                    current_value=col,
                    suggested_fix=f"Provide meaningful name for column {i}"
                ))
            
            # Check for duplicate column names
            duplicate_count = list(self.df.columns).count(col)
            if duplicate_count > 1:
                self.report.add_issue(ValidationIssue(
                    issue_type="duplicate_column_names",
                    severity="warning",
                    description=f"Column name '{col}' appears {duplicate_count} times",
                    location=f"Column: {col}",
                    current_value=duplicate_count,
                    suggested_fix=f"Rename duplicate columns to unique names"
                ))
            
            # Check for whitespace in column names
            if col != col.strip():
                self.report.add_issue(ValidationIssue(
                    issue_type="column_name_whitespace",
                    severity="info",
                    description=f"Column name has leading/trailing whitespace: '{col}'",
                    location=f"Column: {col}",
                    current_value=col,
                    suggested_fix=f"Trim whitespace: '{col.strip()}'"
                ))
    
    def validate_data_types(self) -> None:
        """Check for potential data type issues and inconsistencies."""
        if self.df is None:
            return
        
        for col in self.df.columns:
            if self.df[col].isna().all():
                continue
            
            # Get non-null values
            non_null_values = self.df[col].dropna()
            if len(non_null_values) == 0:
                continue
            
            # Check for mixed data types (numbers stored as text, etc.)
            numeric_pattern = re.compile(r'^-?(\d{1,3}(,\d{3})*|\d+)(\.\d+)?$')
            date_patterns = [
                re.compile(r'^\d{4}-\d{2}-\d{2}$'),  # YYYY-MM-DD
                re.compile(r'^\d{2}/\d{2}/\d{4}$'),  # MM/DD/YYYY
                re.compile(r'^\d{2}\.\d{2}\.\d{4}$'), # DD.MM.YYYY
            ]
            
            # Convert to string for pattern matching
            str_values = non_null_values.astype(str)
            
            # Check if values look like numbers but are stored as text
            potential_numbers = str_values[str_values.str.match(numeric_pattern, na=False)]
            if len(potential_numbers) > len(str_values) * 0.8 and len(potential_numbers) > 5:
                self.report.add_issue(ValidationIssue(
                    issue_type="potential_numeric_column",
                    severity="info",
                    description=f"Column '{col}' contains values that look like numbers but are stored as text",
                    location=f"Column: {col}",
                    current_value="text",
                    suggested_fix="Convert to numeric data type",
                    count=len(potential_numbers)
                ))
            
            # Check for potential date columns
            for date_pattern in date_patterns:
                potential_dates = str_values[str_values.str.match(date_pattern, na=False)]
                if len(potential_dates) > len(str_values) * 0.8 and len(potential_dates) > 5:
                    self.report.add_issue(ValidationIssue(
                        issue_type="potential_date_column",
                        severity="info",
                        description=f"Column '{col}' contains values that look like dates",
                        location=f"Column: {col}",
                        current_value="text",
                        suggested_fix="Convert to datetime data type",
                        count=len(potential_dates)
                    ))
                    break
    
    def validate_consistency(self) -> None:
        """Check for data consistency issues."""
        if self.df is None:
            return
        
        for col in self.df.columns:
            if self.df[col].isna().all():
                continue
            
            non_null_values = self.df[col].dropna().astype(str)
            if len(non_null_values) == 0:
                continue
            
            # Check for inconsistent capitalization
            unique_values = set(non_null_values)
            lower_values = set(val.lower() for val in unique_values)
            
            if len(unique_values) != len(lower_values) and len(unique_values) > 1:
                inconsistent_count = len(unique_values) - len(lower_values)
                self.report.add_issue(ValidationIssue(
                    issue_type="inconsistent_capitalization",
                    severity="info",
                    description=f"Column '{col}' has {inconsistent_count} values with inconsistent capitalization",
                    location=f"Column: {col}",
                    current_value=inconsistent_count,
                    suggested_fix="Standardize capitalization",
                    count=inconsistent_count
                ))
            
            # Check for common typos or variations
            if len(unique_values) < 50:  # Only for categorical-like columns
                # Simple similarity check for potential typos
                values_list = list(unique_values)
                potential_typos = []
                
                for i, val1 in enumerate(values_list):
                    for val2 in values_list[i+1:]:
                        # Simple Levenshtein-like check
                        if abs(len(val1) - len(val2)) <= 2:
                            common_chars = set(val1.lower()) & set(val2.lower())
                            if len(common_chars) >= min(len(val1), len(val2)) * 0.8:
                                potential_typos.append((val1, val2))
                
                if potential_typos:
                    self.report.add_issue(ValidationIssue(
                        issue_type="potential_typos",
                        severity="info",
                        description=f"Column '{col}' has potentially similar values that might be typos",
                        location=f"Column: {col}",
                        current_value=potential_typos[:3],  # Show first 3 examples
                        suggested_fix="Review and standardize similar values",
                        count=len(potential_typos)
                    ))
    
    def clean_data(self) -> pd.DataFrame:
        """
        Apply automatic fixes for common issues.
        
        Returns:
            pd.DataFrame: Cleaned dataframe
        """
        if self.df is None:
            return pd.DataFrame()
        
        cleaned_df = self.df.copy()
        
        # Remove exact duplicates
        initial_rows = len(cleaned_df)
        cleaned_df = cleaned_df.drop_duplicates()
        removed_duplicates = initial_rows - len(cleaned_df)
        
        # Remove completely empty rows
        cleaned_df = cleaned_df.dropna(how='all')
        
        # Clean column names
        cleaned_df.columns = [col.strip() for col in cleaned_df.columns]
        
        # Clean whitespace in string columns
        for col in cleaned_df.columns:
            if cleaned_df[col].dtype == 'object':
                # Remove leading/trailing whitespace
                cleaned_df[col] = cleaned_df[col].astype(str).str.strip()
                
                # Replace multiple spaces with single space
                cleaned_df[col] = cleaned_df[col].str.replace(r'\s+', ' ', regex=True)
                
                # Replace special whitespace characters
                cleaned_df[col] = cleaned_df[col].str.replace(r'[\u00a0\t]', ' ', regex=True)
                
                # Convert back to NaN if originally NaN
                cleaned_df[col] = cleaned_df[col].replace('nan', pd.NA)
        
        self.report.cleaned_rows = len(cleaned_df)
        return cleaned_df
    
    def run_full_validation(self) -> ValidationReport:
        """
        Run complete validation process.
        
        Returns:
            ValidationReport: Complete validation report
        """
        print(f"Loading CSV file: {self.csv_file_path}")
        
        if not self.load_csv():
            return self.report
        
        print(f"Loaded {self.report.total_rows:,} rows and {self.report.total_columns} columns")
        print("Running validation checks...")
        
        # Run all validation checks
        self.validate_duplicates()
        self.validate_empty_rows_columns()
        self.validate_whitespace_issues()
        self.validate_column_names()
        self.validate_data_types()
        self.validate_consistency()
        
        return self.report
    
    def generate_report(self, output_file: Optional[str] = None) -> str:
        """
        Generate a detailed validation report.
        
        Args:
            output_file: Optional file to save report to
            
        Returns:
            str: Report content as string
        """
        report_lines = []
        report_lines.append("=" * 80)
        report_lines.append("CSV DATA QUALITY VALIDATION REPORT")
        report_lines.append("=" * 80)
        report_lines.append(f"File: {self.csv_file_path}")
        report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append(f"Encoding: {self.encoding}")
        report_lines.append("")
        
        # Overview
        report_lines.append("OVERVIEW")
        report_lines.append("-" * 40)
        report_lines.append(f"Total Rows: {self.report.total_rows:,}")
        report_lines.append(f"Total Columns: {self.report.total_columns}")
        report_lines.append(f"Total Issues Found: {len(self.report.issues)}")
        report_lines.append("")
        
        # Issue summary
        summary = self.report.get_summary()
        if summary:
            report_lines.append("ISSUE SUMMARY")
            report_lines.append("-" * 40)
            for issue_type, count in sorted(summary.items()):
                report_lines.append(f"{issue_type.replace('_', ' ').title()}: {count}")
            report_lines.append("")
        
        # Issues by severity
        for severity in ['critical', 'warning', 'info']:
            issues = self.report.get_issues_by_severity(severity)
            if issues:
                report_lines.append(f"{severity.upper()} ISSUES")
                report_lines.append("-" * 40)
                for issue in issues:
                    report_lines.append(f"• {issue.description}")
                    report_lines.append(f"  Location: {issue.location}")
                    if issue.suggested_fix:
                        report_lines.append(f"  Suggested Fix: {issue.suggested_fix}")
                    report_lines.append("")
        
        # Recommendations
        report_lines.append("RECOMMENDATIONS")
        report_lines.append("-" * 40)
        
        critical_issues = len(self.report.get_issues_by_severity('critical'))
        warning_issues = len(self.report.get_issues_by_severity('warning'))
        
        if critical_issues > 0:
            report_lines.append("🔴 CRITICAL: Address critical issues before proceeding with data analysis.")
        elif warning_issues > 0:
            report_lines.append("🟡 WARNING: Consider fixing warning issues to improve data quality.")
        else:
            report_lines.append("✅ GOOD: No critical issues found. Data appears to be in good condition.")
        
        report_lines.append("")
        report_lines.append("To clean the data automatically, use the --clean option.")
        
        report_content = "\n".join(report_lines)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report_content)
            print(f"Report saved to: {output_file}")
        
        return report_content


def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Validate and clean CSV files converted from Excel spreadsheets"
    )
    parser.add_argument("input_file", help="Path to the CSV file to validate")
    parser.add_argument("--encoding", default="utf-8", help="File encoding (default: utf-8)")
    parser.add_argument("--clean", action="store_true", help="Generate cleaned CSV file")
    parser.add_argument("--output-dir", help="Directory for output files (default: same as input)")
    parser.add_argument("--report-file", help="Save validation report to file")
    parser.add_argument("--quiet", action="store_true", help="Suppress progress messages")
    
    args = parser.parse_args()
    
    # Initialize validator
    validator = CSVQualityValidator(args.input_file, args.encoding)
    
    # Run validation
    if not args.quiet:
        print("Starting CSV quality validation...")
    
    report = validator.run_full_validation()
    
    # Generate and display report
    output_dir = Path(args.output_dir) if args.output_dir else Path(args.input_file).parent
    report_file = args.report_file or str(output_dir / f"{Path(args.input_file).stem}_quality_report.txt")
    
    report_content = validator.generate_report(report_file)
    
    if not args.quiet:
        print("\n" + report_content)
    
    # Clean data if requested
    if args.clean:
        cleaned_df = validator.clean_data()
        output_file = output_dir / f"{Path(args.input_file).stem}_cleaned.csv"
        
        cleaned_df.to_csv(output_file, index=False, encoding='utf-8')
        
        if not args.quiet:
            print(f"\nCleaned CSV saved to: {output_file}")
            print(f"Original rows: {report.total_rows:,}")
            print(f"Cleaned rows: {len(cleaned_df):,}")
            print(f"Rows removed: {report.total_rows - len(cleaned_df):,}")
    
    # Exit with appropriate code
    critical_issues = len(report.get_issues_by_severity('critical'))
    sys.exit(1 if critical_issues > 0 else 0)


if __name__ == "__main__":
    main()