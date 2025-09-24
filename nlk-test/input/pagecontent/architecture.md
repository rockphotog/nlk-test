# Technical Architecture

This page provides a detailed technical view of the Norwegian Laboratory Codebook (NLK) CodeSystem architecture and its integration within the FHIR ecosystem.

## Complete System Architecture

The following comprehensive diagram shows the full technical architecture of the NLK CodeSystem, including all FHIR base classes, Norwegian-specific extensions, medical domain classifications, and integration patterns:

![NLK CodeSystem Complete Architecture](nlk-test.svg)

*Figure: Complete technical architecture of the Norwegian Laboratory Codebook CodeSystem showing FHIR R4 foundation, domain-specific implementations, and Norwegian healthcare integration patterns.*

## Architecture Components

### FHIR R4 Foundation

The NLK CodeSystem is built upon standard FHIR R4 base classes:

- **CodeSystem**: Core FHIR resource providing the foundation
- **Property**: Metadata definitions for concept properties
- **Concept**: Individual code entries with associated metadata
- **ConceptProperty**: Property values attached to specific concepts

### Norwegian Laboratory Implementation

The Norwegian-specific implementation extends FHIR with:

- **NorskLaboratoriekodeverk**: Main CodeSystem implementation (11,391 codes)
- **NLKProperty**: Extended properties for Norwegian laboratory context
- **NLKConcept**: Laboratory code concepts with Norwegian healthcare metadata

### Medical Domain Classification

Six major medical specialties organize the laboratory codes:

1. **Medisinsk Biokjemi** (Medical Biochemistry) - 2,881 codes
2. **Immunologi og Transfusjonsmedisin** (Immunology & Transfusion Medicine) - 3,231 codes  
3. **Medisinsk Mikrobiologi** (Medical Microbiology) - 2,547 codes
4. **Klinisk Farmakologi** (Clinical Pharmacology) - 2,642 codes
5. **Medisinsk Genetikk** (Medical Genetics) - 67 codes
6. **Patologi** (Pathology) - 27 codes

### FHIR Integration Patterns

The CodeSystem integrates with FHIR workflows through:

- **ObservationProfile**: Laboratory test results using NLK codes
- **DiagnosticReportProfile**: Comprehensive laboratory reports
- **ValueSet**: Curated subsets for specific use cases

### Norwegian Healthcare Context

Integration with Norwegian health ecosystem:

- **HL7 Norway Foundation**: Built on `hl7.fhir.no.basis` package (v2.0.17)
- **National Standards**: Alignment with Norwegian healthcare interoperability requirements
- **Jurisdictional Compliance**: Norway-specific governance and terminology management

## Implementation Benefits

This architecture provides:

- **Standardization**: Consistent laboratory terminology across Norwegian healthcare
- **Interoperability**: FHIR-compliant integration with existing systems
- **Extensibility**: Framework for future laboratory code additions
- **Governance**: Clear ownership and maintenance patterns
- **Quality**: Validated, deduplicated, and version-controlled terminology

## Technical Specifications

- **FHIR Version**: R4 (4.0.1)
- **CodeSystem URL**: `http://hl7.no/fhir/ig/nlk-test/CodeSystem/norsk-laboratoriekodeverk`
- **Version**: 7280.77
- **Status**: Experimental
- **Case Sensitive**: True
- **Content**: Complete (all codes included)

For implementation guidance and examples, see the [Getting Started](index.html#getting-started) section.
