# Scripts Directory

This directory contains all Python scripts for processing and validating the Norwegian Laboratory Codebook (NLK) data.

## 📁 Scripts Overview

### Data Conversion

- **`convert_excel_to_csv.py`** - Converts Excel files to optimized CSV formats
  - Supports multiple encoding options
  - Generates both full and processing-optimized CSV files
  - Creates data summaries and optional Parquet output

### Data Processing

- **`process_nlk_csv.py`** - Main processor for NLK CSV data
  - Analytics and statistics
  - Data filtering and search
  - FSH CodeSystem generation
  - Export utilities

### Data Quality

- **`validate_csv_quality.py`** - Comprehensive CSV quality validator
  - Detects duplicates, whitespace issues, encoding problems
  - Automatic data cleaning
  - Detailed quality reports
  - Command-line and programmatic interfaces

### Examples and Usage

- **`example_csv_validation.py`** - Demonstrates CSV validation workflows
  - Real examples using NLK data
  - Sample problematic data creation
  - Quality assessment patterns

- **`csv_validator_examples.py`** - Usage patterns and best practices
  - Command-line usage examples
  - Programmatic usage patterns
  - Workflow recommendations

### Sample Data

- **`samples/`** - Directory containing sample data files
  - `sample_problematic_data.csv` - Example CSV with common data quality issues
  - `sample_problematic_data_cleaned.csv` - Automatically cleaned version
  - `sample_problematic_data_quality_report.txt` - Detailed quality analysis report

## 🚀 Quick Start

### Prerequisites

```bash
# Activate virtual environment (from project root)
source .venv/bin/activate

# Navigate to scripts directory
cd scripts
```

### Convert Excel to CSV

```bash
python convert_excel_to_csv.py "../nlk-test/resources/Norsk Laboratoriekodeverk 7280.77-clean.xlsx" "../nlk-test/resources/csv_output"
```

### Validate CSV Quality

```bash
python validate_csv_quality.py "../nlk-test/resources/csv_output/norsk_laboratoriekodeverk_7280.77-clean_full.csv" --clean
```

### Process NLK Data

```bash
python process_nlk_csv.py
```

### Run Examples

```bash
python example_csv_validation.py
python csv_validator_examples.py
```

## 📊 Typical Workflow

1. **Convert** Excel to CSV using `convert_excel_to_csv.py`
2. **Validate** CSV quality using `validate_csv_quality.py`  
3. **Process** data for analytics using `process_nlk_csv.py`
4. **Generate** FSH CodeSystems for FHIR integration

## 🔧 Configuration

All scripts use relative paths from the `scripts/` directory:

- Input files: `../nlk-test/resources/`
- Output files: `../nlk-test/resources/csv_output/`
- Sample files: `samples/` (within scripts directory)
- Reports: `../` (project root)

## 💡 Tips

- Always run scripts from the `scripts/` directory
- Use the `--help` flag for detailed command-line options
- Check example scripts for usage patterns
- Activate the virtual environment before running scripts

## 📚 Documentation

See the main [CSV_README.md](../CSV_README.md) for comprehensive documentation about data processing workflows and best practices.
