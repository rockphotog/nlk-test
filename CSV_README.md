# Norwegian Laboratory Codebook - CSV Data Processing

This directory contains optimized CSV datasets and processing tools for the Norwegian Laboratory Codebook (Norsk Laboratoriekodeverk).

## 📁 File Structure

```text
nlk-test/resources/csv_output/
├── norsk_laboratoriekodeverk_7280.77-clean_full.csv          # Full dataset (UTF-8 with BOM)
├── norsk_laboratoriekodeverk_7280.77-clean_processing.csv    # Processing-optimized (UTF-8)
└── norsk_laboratoriekodeverk_7280.77-clean_summary.txt       # Dataset summary

scripts/
├── convert_excel_to_csv.py    # Excel to CSV conversion script
├── process_nlk_csv.py         # CSV data processing utilities
├── validate_csv_quality.py    # CSV quality validator
├── example_csv_validation.py  # Validation examples
└── csv_validator_examples.py  # Usage examples and patterns
```

## 📊 Dataset Overview

- **Total Records**: 11,395 laboratory codes
- **Active Codes**: 9,686 currently valid codes  
- **Historical Codes**: 1,709 retired/replaced codes
- **Data Size**: ~3MB (CSV), 12MB (in memory)
- **Columns**: 17 metadata fields per code

### Medical Domain Distribution

| Domain | Codes | Percentage |
|--------|-------|------------|
| Immunologi og transfusjonsmedisin | 3,231 | 28.4% |
| Medisinsk biokjemi | 2,881 | 25.3% |
| Klinisk farmakologi | 2,642 | 23.2% |
| Medisinsk mikrobiologi | 2,547 | 22.4% |
| Medisinsk genetikk | 67 | 0.6% |
| Patologi | 27 | 0.2% |

## 🔧 Data Schema

The CSV files contain the following standardized columns:

| Column | Description | Type | Coverage |
|--------|-------------|------|----------|
| `kode` | Laboratory code identifier | String | 100% |
| `gyldig_fra` | Valid from date | DateTime | 100% |
| `gyldig_til` | Valid until date | DateTime | 15.1% |
| `erstattes_av` | Replaced by code | String | 10.7% |
| `endringsdato` | Last change date | DateTime | 82.7% |
| `norsk_bruksnavn` | Norwegian display name | String | 100% |
| `kodedefinisjon` | Code definition | String | 93.1% |
| `komponent` | Laboratory component | String | 93.1% |
| `komponent_spesifikasjon` | Component specification | String | 30.7% |
| `system` | Biological system | String | 93.1% |
| `system_spesifikasjon` | System specification | String | 22.3% |
| `egenskapsart` | Property type | String | 92.9% |
| `egenskapsart_spesifikasjon` | Property specification | String | 59.0% |
| `enhet` | Unit of measurement | String | 51.7% |
| `primært_fagområde` | Primary medical domain | String | 100% |
| `sekundært_fagområde` | Secondary medical domain | String | 4.2% |
| `gruppering` | Code grouping | String | 86.0% |

## 🚀 Quick Start

### 1. Convert Excel to CSV

```bash
# Activate virtual environment
source .venv/bin/activate

# Convert Excel to optimized CSV formats
cd scripts
python convert_excel_to_csv.py "path/to/excel_file.xlsx" "output_directory"
```

### 2. Process CSV Data

```python
# From the scripts directory
from process_nlk_csv import NLKDataProcessor

# Initialize processor
processor = NLKDataProcessor("../nlk-test/resources/csv_output/processing_file.csv")

# Get active codes only
active_codes = processor.get_active_codes()

# Search for specific terms
diabetes_codes = processor.search_codes("diabetes")

# Get codes by medical domain
biochemistry = processor.get_codes_by_domain("Medisinsk biokjemi")

# Export filtered data
processor.export_filtered_data(active_codes, "active_codes.csv")

# Generate FSH CodeSystem
processor.generate_fsh_codesystem("nlk_codesystem.fsh")
```

### 3. Validate CSV Quality

```bash
# From the scripts directory
cd scripts

# Basic validation
python validate_csv_quality.py "../nlk-test/resources/csv_output/your_file.csv"

# Validation with auto-clean and report
python validate_csv_quality.py "../nlk-test/resources/csv_output/your_file.csv" --clean --report-file report.txt

# Run validation examples
python example_csv_validation.py
```

### 4. Basic Data Analysis

```python
import pandas as pd

# Load processing-optimized CSV (from scripts directory)
df = pd.read_csv("../nlk-test/resources/csv_output/processing_file.csv", encoding='utf-8')

# Basic statistics
print(f"Total codes: {len(df):,}")
print(f"Medical domains: {df['primært_fagområde'].nunique()}")
print(f"Date range: {df['gyldig_fra'].min()} to {df['gyldig_til'].max()}")

# Domain breakdown
domain_counts = df['primært_fagområde'].value_counts()
print(domain_counts)
```

## 📈 Performance Optimizations

### CSV Format Advantages

1. **File Size**: 70% smaller than Excel (3MB vs 10MB)
2. **Loading Speed**: 5-10x faster reading with pandas
3. **Memory Usage**: Optimized data types reduce RAM usage
4. **Cross-platform**: Works with any programming language/tool
5. **Version Control**: Text-based format works well with Git
6. **Streaming**: Can process large datasets without loading everything into memory

### Processing Optimizations

- **UTF-8 Encoding**: Universal compatibility, smaller than UTF-16
- **Minimal Quoting**: Faster parsing for processing workflows
- **Standardized Columns**: Clean names for programmatic access
- **Date Parsing**: Proper DateTime objects for temporal queries
- **NULL Handling**: Consistent treatment of missing values

## 🔍 Data Quality

### Validation Results

- ✅ **No duplicate rows**: All records are unique
- ✅ **No empty rows**: All records contain data
- ✅ **Consistent encoding**: UTF-8 throughout
- ✅ **Date validation**: All dates are valid timestamps
- ✅ **Code uniqueness**: Each laboratory code is unique

### Data Completeness

- **Core fields**: 100% complete (kode, gyldig_fra, norsk_bruksnavn, primært_fagområde)
- **Metadata fields**: 50-90% complete depending on field
- **Historical tracking**: Complete validity periods and replacement chains
- **Classification**: Full medical domain coverage

## 🛠️ Advanced Usage

### Custom Filtering

```python
# Get codes valid on specific date
target_date = pd.Timestamp('2024-01-01')
valid_codes = processor.df[
    (processor.df['gyldig_fra'] <= target_date) &
    (processor.df['gyldig_til'].isna() | (processor.df['gyldig_til'] >= target_date))
]

# Find replacement chains
replaced_codes = processor.df[processor.df['erstattes_av'].notna()]

# Get codes with specific units
unit_codes = processor.df[processor.df['enhet'] == 'mmol/L']
```

### Data Export Options

```python
# Export to Excel with multiple sheets by domain
for domain in processor.df['primært_fagområde'].unique():
    domain_codes = processor.get_codes_by_domain(domain)
    filename = f"nlk_{domain.lower().replace(' ', '_')}.xlsx"
    processor.export_filtered_data(domain_codes, filename, 'excel')

# Export JSON for web applications
active_json = processor.export_filtered_data(
    processor.get_active_codes(), 
    "active_codes.json", 
    'json'
)
```

### Integration with FHIR Tools

```python
# Generate FSH with custom properties
processor.generate_fsh_codesystem("custom_nlk.fsh")

# Create ValueSets for specific domains
biochemistry = processor.get_codes_by_domain("Medisinsk biokjemi")
# Export as FSH ValueSet...
```

## 📚 Best Practices

### For Large Dataset Processing

1. **Use processing CSV**: Optimized for pandas/programmatic access
2. **Chunk processing**: For datasets > 100MB, use `pd.read_csv(chunksize=1000)`
3. **Memory monitoring**: Use `df.memory_usage(deep=True)` to track memory
4. **Efficient filtering**: Use boolean indexing instead of loops
5. **Data types**: Convert to optimal types after loading

### For Data Analysis

1. **Date filtering**: Always use proper datetime objects for temporal queries
2. **Text search**: Use vectorized string operations for performance
3. **Groupby operations**: Leverage pandas groupby for domain-level statistics
4. **Export subsets**: Don't process entire dataset if only subset needed

### For Production Use

1. **Validation**: Always validate data after loading
2. **Error handling**: Implement proper exception handling
3. **Logging**: Use structured logging for debugging
4. **Testing**: Unit test data processing functions
5. **Documentation**: Document data transformations and business rules

## 🤝 Contributing

To add new processing functions or improve existing ones:

1. Follow pandas best practices for performance
2. Add proper type hints and documentation
3. Include unit tests for new functionality
4. Update this README with usage examples

## 📄 License

This data processing toolkit is provided under the same license as the Norwegian Laboratory Codebook dataset.
