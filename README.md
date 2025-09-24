# Norsk Laboratoriekodeverk (NLK) - FHIR Implementation Guide

This repository contains a FHIR Implementation Guide for publishing an experimental version of the **Norsk Laboratoriekodeverk (NLK)** - the Norwegian Laboratory Codebook.

## Purpose

The main purpose of this implementation guide is to publish an experimental FHIR CodeSystem for the Norsk Laboratoriekodeverk (NLK), making this comprehensive Norwegian laboratory terminology available in a standardized FHIR format.

## What You'll Find Here

### 🧬 CodeSystem: Norsk Laboratoriekodeverk

- **Complete terminology**: 11,395 laboratory codes covering all aspects of Norwegian laboratory medicine
- **Current active codes**: 9,679 actively used codes
- **Version**: 7280.77 (derived from the source Excel file)
- **Coverage**: Six major medical domains:
  - Medisinsk biokjemi (Medical Biochemistry) - 2,881 codes
  - Immunologi og transfusjonsmedisin (Immunology and Transfusion Medicine) - 3,231 codes  
  - Medisinsk mikrobiologi (Medical Microbiology) - 2,547 codes
  - Klinisk farmakologi (Clinical Pharmacology) - 2,642 codes
  - Medisinsk genetikk (Medical Genetics) - 67 codes
  - Patologi (Pathology) - 27 codes

### 📋 Rich Metadata

Each code includes comprehensive metadata:

- **Valid from/to dates**: Lifecycle management
- **Code definitions**: Technical NPU-style definitions
- **Components**: What is being measured
- **Systems**: Specimen/system types (Blood, Urine, etc.)
- **Properties**: Type of measurement (concentration, activity, etc.)
- **Units**: Measurement units
- **Groupings**: Clinical categorization
- **Replacement codes**: Version management

### 🔧 Technical Implementation

- **Source**: Generated from `Norsk Laboratoriekodeverk 7280.77.xlsx`
- **Format**: FHIR Shorthand (FSH)
- **Build tool**: SUSHI + HL7 FHIR IG Publisher
- **FHIR Version**: 4.0.1
- **Dependencies**: hl7.fhir.no.basis 2.2.0

## Repository Structure

```text
📁 nlk-test/                    # Main IG directory
├── 📄 ig.ini                   # IG Publisher configuration
├── 📄 sushi-config.yaml        # SUSHI configuration
├── 📄 nlk-test.codesystem.fsh  # Main CodeSystem definition (224k+ lines)
└── 📁 input/                   # IG input files
    ├── 📁 fsh/                  # FSH source files
    ├── 📁 images/              # Documentation images
    └── 📁 pagecontent/         # Narrative content

📁 resources/                   # Source data
└── 📄 Norsk Laboratoriekodeverk 7280.77.xlsx  # Original Excel source

📁 documentation/               # Project documentation
└── Various .md files with setup and usage instructions
```

## Getting Started

### Prerequisites

- Node.js and npm
- SUSHI (FHIR Shorthand compiler)
- HL7 FHIR IG Publisher

### Building the Implementation Guide

1. **Install dependencies:**

   ```bash
   npm install -g fsh-sushi
   ```

2. **Compile FSH to FHIR:**

   ```bash
   cd nlk-test
   sushi .
   ```

3. **Build the Implementation Guide:**

   ```bash
   _genonce.sh  # or equivalent for your platform
   ```

## Usage

Once built, the Implementation Guide will provide:

- **Browsable CodeSystem**: All NLK codes with search and filter capabilities
- **FHIR API endpoints**: For programmatic access to the terminology
- **Documentation**: Comprehensive guide for implementers
- **Examples**: Sample usage in FHIR resources

## Status

🚧 **Experimental** - This is an experimental implementation for evaluation and testing purposes.

## Contributing

This project serves as a template for Norwegian FHIR Implementation Guides. See the [documentation](documentation/) folder for detailed instructions on:

- Using this repository as a template
- Configuration and customization
- Automated workflows and deployment

## License

See [LICENSE](LICENSE) file for details.

## Contact

**Publisher**: Espen  
**Jurisdiction**: Norway (NO)

---

**Source Data**: Generated from Norsk Laboratoriekodeverk 7280.77.xlsx on 2025-09-24
