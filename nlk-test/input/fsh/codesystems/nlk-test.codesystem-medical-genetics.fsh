// Norwegian Laboratory Codebook (Norsk Laboratoriekodeverk) - Enhanced with Complete Properties
// Generated from: norsk_laboratoriekodeverk_7280.77-clean_full_deduplicated.csv
// Generated on: 2025-09-24 14:06:01
// Total concepts: 103
// Active concepts: 83
// Retired concepts: 1709

CodeSystem: NorskLaboratoriekodeverkMedicalGenetics
Id: norsk-laboratoriekodeverk-medical-genetics
Title: "Norsk Laboratoriekodeverk - Medical Genetics"
Description: "Norwegian Laboratory Codebook - Medical Genetics domain subset with complete metadata properties"
* ^url = "http://hl7.no/fhir/ig/nlk-test/CodeSystem/norsk-laboratoriekodeverk-medical-genetics"
* ^version = "7280.77"
* ^status = #draft
* ^experimental = true
* ^date = "2025-09-24"
* ^publisher = "Espen"
* ^contact.name = "Espen"
* ^jurisdiction = urn:iso:std:iso:3166#NO "Norway"
* ^caseSensitive = true
* ^content = #complete
* ^count = 103

// Properties for additional metadata
* ^property[0].code = #validFrom
* ^property[=].description = "Valid from date"
* ^property[=].type = #dateTime

* ^property[+].code = #validTo
* ^property[=].description = "Valid to date"
* ^property[=].type = #dateTime

* ^property[+].code = #replacedBy
* ^property[=].description = "Code that replaces this code"
* ^property[=].type = #code

* ^property[+].code = #changeDate
* ^property[=].description = "Date of last change"
* ^property[=].type = #dateTime

* ^property[+].code = #codeDefinition
* ^property[=].description = "Technical code definition"
* ^property[=].type = #string

* ^property[+].code = #component
* ^property[=].description = "Component being measured"
* ^property[=].type = #string

* ^property[+].code = #componentSpec
* ^property[=].description = "Component specification"
* ^property[=].type = #string

* ^property[+].code = #system
* ^property[=].description = "System/specimen type"
* ^property[=].type = #string

* ^property[+].code = #systemSpec
* ^property[=].description = "System specification"
* ^property[=].type = #string

* ^property[+].code = #propertyType
* ^property[=].description = "Type of property measured"
* ^property[=].type = #string

* ^property[+].code = #propertySpec
* ^property[=].description = "Property specification"
* ^property[=].type = #string

* ^property[+].code = #unit
* ^property[=].description = "Unit of measurement"
* ^property[=].type = #string

* ^property[+].code = #primaryDomain
* ^property[=].description = "Primary medical domain"
* ^property[=].type = #string

* ^property[+].code = #secondaryDomain
* ^property[=].description = "Secondary medical domain"
* ^property[=].type = #string

* ^property[+].code = #grouping
* ^property[=].description = "Grouping category"
* ^property[=].type = #string

// Concepts with complete properties
* #NOR15177 "DNA-Mitokondriegenom-sekvensering"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"

* #NOR25416 "Ce-Dyrkning"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2018-12-31T23:59:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25420 "RNA-Ekspresjonsprofilering"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Undersøkelse av genekspresjonsmønster"
  * ^property[+].code = #system
  * ^property[=].valueString = "RNA"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25437 "DNA-Sangersekvensering, enkeltgen"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Sangersekvensering av et spesifikt gen"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25438 "DNA-Sangersekvensering, eksoner"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Sangersekvensering av ett eller flere utvalgte eksoner"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25439 "DNA-Gensekvensering analysepakke"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2017-10-23T00:00:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25440 "DNA-Sangersekvensering, variant"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Sangersekvensering av en kjent DNA-sekvensvariant"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25441 "DNA-Analysepakke DNA-sekvensvarianter"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2023-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Undersøkelse av flere kjente DNA-sekvensvarianter"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25442 "DNA-Haplotyping"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Haplotyping for å påvise lokus for et sykdomsgen"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25443 "DNA-Metyleringsprofilering"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25444 "DNA-Eksomsekvensering"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25445 "DNA-Genomsekvensering"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25446 "DNA-Genetisk screening"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2017-11-30T23:59:00+00:00"
  * ^property[+].code = #replacedBy
  * ^property[=].valueCode = #NOR25441
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25463 "DNA-Kopitallsanalyse gen, MLPA"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Undersøkelse for å påvise kopitallsvariasjon vha Multiplex Ligation-dependent Probe Amplification"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25464 "Ce-Kromosomalt rearrangement, FISH"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Undersøkelse av kromosomale rearrangementer i celler vha Fluorescence In Situ Hybridization"
  * ^property[+].code = #system
  * ^property[=].valueString = "Celler"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25465 "Ce-Mikroskopisk-karyotyping"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2023-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Lysmikroskopisk kromosomanalyse av celler"
  * ^property[+].code = #system
  * ^property[=].valueString = "Celler"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25466 "B-Mikroskopisk-karyotyping"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2023-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Lysmikroskopisk kromosomanalyse av blod"
  * ^property[+].code = #system
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25467 "Ce-Mikroskopisk-karyotyping, kreftceller"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Lysmikroskopisk kromosomanalyse av kreftceller"
  * ^property[+].code = #system
  * ^property[=].valueString = "Celler"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25468 "DNA-Helgenomisk kopitallsanalyse"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2019-03-22T00:00:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25469 "DNA-Helgenomisk homozygositetsanalyse"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25470 "Ce-Kromosomidentitet"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2017-10-23T00:00:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25506 "DNA-Kromatinanalyse"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25507 "DNA-Metyleringstest, metyleringssensitiv MLPA"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Undersøkelse for å påvise metyleringsmønster vha metyleringssensitiv Multiplex Ligation-dependent Probe Amplification"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25510 "B-DNA"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2018-12-31T23:59:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2013-11-13T00:00:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25511 "Ce-DNA"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2018-12-31T23:59:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2013-11-13T00:00:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25512 "B-RNA"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2018-12-31T23:59:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2013-11-13T00:00:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25513 "Ce-RNA"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2018-12-31T23:59:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2013-11-13T00:00:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25808 "RNA-Sangersekvensering, eksoner"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2016-11-01T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Sangersekvensering av ett eller flere utvalgte eksoner"
  * ^property[+].code = #system
  * ^property[=].valueString = "RNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR25809 "DNA-Fragmentanalyse"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2016-11-01T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2023-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35056 "DNA-Helgenomisk kopitallsanalyse fam.ktr."
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2018-09-24T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2018-11-23T00:00:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35057 "DNA-Eksom-/genomsekvensering fam.ktr."
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2018-09-24T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2018-11-23T00:00:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35103 "DNA-Gensekvensering analysepakke inkl. kopitallsanalyse"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2019-03-22T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35104 "DNA-Eksomsekvensering inkl. kopitallsanalyse"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2019-03-22T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35105 "DNA-Genomsekvensering inkl. kopitallsanalyse"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2019-03-22T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2022-12-31T23:59:00+00:00"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35218 "B-DNA ekstraksjon og lagring"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2021-05-25T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Ekstraksjon og lagring av DNA fra blodceller"
  * ^property[+].code = #system
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35219 "Ce-DNA ekstraksjon og lagring"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2021-05-25T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Ekstraksjon og lagring av DNA fra andre celler"
  * ^property[+].code = #system
  * ^property[=].valueString = "Celler"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35220 "B-RNA ekstraksjon og lagring"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2021-05-25T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Ekstraksjon og lagring av RNA fra blodceller"
  * ^property[+].code = #system
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35221 "Ce-RNA ekstraksjon og lagring"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2021-05-25T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Ekstraksjon og lagring av RNA fra andre celler"
  * ^property[+].code = #system
  * ^property[=].valueString = "Celler"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35222 "Ce-Dyrkning og lagring"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2021-05-25T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Dyrkning og lagring av celler"
  * ^property[+].code = #system
  * ^property[=].valueString = "Celler"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35223 "B-Dyrkning og lagring"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2021-05-25T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Dyrkning og lagring av blodceller"
  * ^property[+].code = #system
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35245 "RNA-NGS-transkriptom"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-03-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2023-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Neste generasjons sekvensering av hele transkriptomet"
  * ^property[+].code = #system
  * ^property[=].valueString = "RNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35255 "DNA-Anriket panel, NGS"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Neste generasjons sekvensering av flere gener for en gitt sykdom/syndrom (panel)"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35256 "DNA-Heleksom, NGS"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Neste generasjons sekvensering av hele eksomet"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35257 "DNA-Helgenom, NGS"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Neste generasjons sekvensering av hele genomet"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35258 "Tolkning, 1-10 gener eller kjente varianter"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Tolkning av genpanel, 1-10 gener eller kjente varianter"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN/HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35259 "Tolkning, 11-99 gener"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Tolkning av genpanel, 11-99 gener"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN/HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35260 "Tolkning, over 100 gener"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Tolkning av genpanel, over 100 gener"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN/HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35261 "Tolkning inkl. kopitall, 1-10 gener eller kjente varianter"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Tolkning av genpanel, inkludert kopitallsanalyse, 1-10 gener eller kjente varianter"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN/HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35262 "Tolkning inkl. kopitall, 11-99 gener"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Tolkning av genpanel, inkludert kopitallsanalyse, 11-99 gener"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN/HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35263 "Tolkning inkl. kopitall, over 100 gener"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Tolkning av genpanel, inkludert kopitallsanalyse, over 100 gener"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN/HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35264 "Retolkning av en eller flere varianter"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Retolkning av en eller flere varianter"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN/HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35265 "DNA-Heleksom, fam.ktr., NGS"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Neste generasjons sekvensering av hele eksomet, familiekontroll"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35266 "DNA-Helgenom, fam.ktr., NGS"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Neste generasjons sekvensering av hele genomet, familiekontroll"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35267 "DNA-Helgenomisk kopitallsanalyse, ArrayCGH"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Helgenomisk analyse mtp kopitallsvariasjon vha Array comparative genomic hybridization"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN/HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35268 "DNA-Helgenomisk kopitallsanalyse, SNParray"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Helgenomisk analyse mtp kopitallsvariasjon vha Single nucleotide polymorphism microarray"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN/HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35269 "DNA-Helgenomisk kopitallsanalyse, fam.ktr., ArrayCGH"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Helgenomisk analyse mtp kopitallsvariasjon, familiekontroll, vha Array comparative genomic hybridization"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN/HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35270 "DNA-Helgenomisk kopitallsanalyse, fam.ktr., SNParray"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Helgenomisk analyse mtp kopitallsvariasjon, familiekontroll, vha Single nucleotide polymorphism microarray"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN/HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35271 "DNA-Helgenomisk metyleringsanalyse, NGS"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Helgenomisk metyleringsanalyse ved Neste generasjons sekvensering"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35272 "DNA-Metyleringsprofilering, matrise"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Metyleringsprofilering, matrise"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35281 "DNA-Digital dråpe PCR"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2023-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Digital dråpe PCR"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35282 "DNA-Optisk mapping sekvensering"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2023-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Optisk mapping sekvensering"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35283 "DNA-PGT Karyomapping, fam.ktr."
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2023-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Preimplantasjonstesting, Karyomapping for haplotyping og påvisning av genetisk sekvensvariant, familiekontroll"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN/HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35284 "Ce-PGT Karyomapping, blastocyst"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2023-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Preimplantasjonstesting, Karyomapping for haplotyping og påvisning av genetisk sekvensvariant, blastocyst"
  * ^property[+].code = #system
  * ^property[=].valueString = "Celler"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "ISCN/HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35285 "DNA-PGT Helgenomisk kopitallsanalyse, fam.ktr."
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2023-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Preimplantasjonstesting, Helgenomisk analyse mtp kopitallsvariasjon, familiekontroll"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35286 "Ce-PGT Helgenomisk kopitallsanalyse, blastocyst"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2023-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Preimplantasjonstesting, Helgenomisk analyse mtp kopitallsvariasjon, blastocyst"
  * ^property[+].code = #system
  * ^property[=].valueString = "Celler"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35287 "DNA-PGT Helgenom, fam.ktr., NGS"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2023-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Preimplantasjonstesting, Neste generasjons sekvensering av hele genomet, familiekontroll"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NOR35288 "Ce-PGT Helgenom blastocyst, NGS"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2023-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Preimplantasjonstesting, Neste generasjons sekvensering av hele genomet, blastocyst"
  * ^property[+].code = #system
  * ^property[=].valueString = "Celler"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "takson"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "HGVS"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"

* #NPU19142 "DNA-MT-ATP6"
  * ^definition = "DNA(spec.)—MT-ATP6 gene; seq.var. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2015-03-01T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-ATP6-gen"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "sekvensvariasjon"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU19145 "DNA-MT-ND4"
  * ^definition = "DNA(spec.)—MT-ND4 gene; seq.var. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-ND4-gen"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "sekvensvariasjon"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU19148 "DNA-MT-TK"
  * ^definition = "DNA(spec.)—MT-TK gene; seq.var. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2015-03-01T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TK-gen"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "sekvensvariasjon"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU19149 "DNA-MT-TL1"
  * ^definition = "DNA(spec.)—MT-TL1 gene; seq.var. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2015-03-01T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "sekvensvariasjon"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU19179 "DNA-PYGM-gen"
  * ^definition = "DNA(spec.)—PYGM gene; seq.var. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2022-11-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "PYGM-gen"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "sekvensvariasjon"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU19293 "DNA-MT-ATP6(8993T>G, Leu156Arg)"
  * ^definition = "DNA(spec.)—MT-ATP6 gene(NC_012920.1:g.8993T>G); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-ATP6-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.8993T>G"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU19294 "DNA-MT-ATP6(8993T>C)"
  * ^definition = "DNA(spec.)—MT-ATP6 gene(NC_012920.1:g.8993T>C); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-08-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-ATP6-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.8993T>C"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU19296 "DNA-MT-RNR1(1555A>G)"
  * ^definition = "DNA(spec.)—MT-RNR1 gene(NC_012920.1:g.1555A>G); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-08-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-RNR1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.1555A>G"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU19297 "DNA-MT-TK(8344A>G)"
  * ^definition = "DNA(spec.)—MT-TK gene(NC_012920.1:g.8344A>G); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TK-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.8344A>G"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU19298 "DNA-MT-TL1(3243A>G)"
  * ^definition = "DNA(spec.)—MT-TL1 gene(NC_012920.1:g.3243A>G); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3243A>G"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57092 "DNA(B)-MT-TL1-gen (3243A>G)"
  * ^definition = "DNA(B)—MT-TL1 gene(NC_012920.1:g.3243A>G); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-03-01T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3243A>G"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57093 "DNA(B)-MT-ATP6-gen (8993T>G)"
  * ^definition = "DNA(B)—MT-ATP6 gene(NC_012920.1:g.8993T>G); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-03-01T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-ATP6-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.8993T>G"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57096 "DNA(B)-MT-TK-gen (8344A>G)"
  * ^definition = "DNA(B)—MT-TK gene(NC_012920.1:g.8344A>G); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-03-01T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TK-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.8344A>G"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57605 "DNA-MT-TL1(3256C>T)"
  * ^definition = "DNA(spec.)—MT-TL1 gene(NC_012920.1:g.3256C>T); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-08-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3256C>T"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57612 "DNA-MT-TL1(3271T>C)"
  * ^definition = "DNA(spec.)—MT-TL1 gene(NC_012920.1:g.3271T>C); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-08-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3271T>C"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57613 "DNA-MT-CO1(7445A>G)"
  * ^definition = "DNA(spec.)—MT-CO1 gene(NC_012920.1:g.7445A>G); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-08-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-CO1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.7445A>G"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57614 "DNA-MT-TS1(7471_7472insC)"
  * ^definition = "DNA(spec.)—MT-TS1 gene(NC_012920.1:g.7471_7472insC); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-08-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TS1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.7471_7472insC"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57629 "DNA-MT-TK(8356T>C)"
  * ^definition = "DNA(spec.)—MT-TK gene(NC_012920.1:g.8356T>C); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-08-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TK-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.8356T>C"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57630 "DNA-MT-ND5(13513G>A)"
  * ^definition = "DNA(spec.)—MT-ND5 gene(NC_012920.1:g.13513G>A); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-08-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-ND5-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.13513G>A"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57631 "DNA-MT-ND6(14459G>A)"
  * ^definition = "DNA(spec.)—MT-ND6 gene(NC_012920.1:g.14459G>A); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-08-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-ND6-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.14459G>A"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57632 "DNA-MT-ND1(3460G>A)"
  * ^definition = "DNA(spec.)—MT-ND1 gene(NC_012920.1:g.3460G>A); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-08-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-ND1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3460G>A"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57633 "DNA-MT-ND4(11778G>A)"
  * ^definition = "DNA(spec.)—MT-ND4 gene(NC_012920.1:g.11778G>A); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-08-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-ND4-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.11778G>A"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57634 "DNA-MT-ND6(14484T>C)"
  * ^definition = "DNA(spec.)—MT-ND6 gene(NC_012920.1:g.14484T>C); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-08-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-ND6-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.14484T>C"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57635 "DNA-MT-ATP6(9185(T>C)"
  * ^definition = "DNA(spec.)—MT-ND5 gene(NC_012920.1:g.9185T>C); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-08-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-ND5-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.9185T>C"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57792 "DNA(B)-MT-TL1 gen(3252A>G)"
  * ^definition = "DNA(B)—MT-TL1 gene(NC_012920.1:g.3252A>G); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2017-10-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3252A>G"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU57803 "DNA-MT-TL1 gen(3252A>G)"
  * ^definition = "DNA(spec.)—MT-TL1 gene(NC_012920.1:g.3252A>G); entitic num.(0 1 2) = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2018-02-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3252A>G"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "entitisk antall"
  * ^property[+].code = #propertySpec
  * ^property[=].valueString = "0 1 2"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU58187 "DNA-MT-TL1-gen"
  * ^definition = "DNA(spec.)—MT-TL1 gene(NC_012920.1:g.3271); seq.var. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2018-03-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3271"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "sekvensvariasjon"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU58188 "DNA-MT-TL1-gen"
  * ^definition = "DNA(spec.)—MT-TL1 gene(NC_012920.1:g.3252); seq.var. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2018-03-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3252"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "spesifikasjon"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "sekvensvariasjon"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU58190 "DNA(B)-MT-TL1-gen"
  * ^definition = "DNA(B)—MT-TL1 gene(NC_012920.1:g.3252); seq.var. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2018-03-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3252"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "sekvensvariasjon"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU58191 "DNA(B)-MT-TL1-gen"
  * ^definition = "DNA(B)—MT-TL1 gene(NC_012920.1:g.3271); seq.var. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2018-03-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3271"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "sekvensvariasjon"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU58206 "DNA(B)-MT-TL1-gen (3271T>C)"
  * ^definition = "DNA(B)—MT-TL1 gene(NC_012920.1:g.3271T>C); arb.cont. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2018-03-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3271T>C"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "arbitrært innhold"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU58207 "DNA(B)-MT-TL1-gen (3252A>G)"
  * ^definition = "DNA(B)—MT-TL1 gene(NC_012920.1:g.3252A>G); arb.cont. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2018-03-23T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3252A>G"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "arbitrært innhold"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU58269 "DNA(B)-MT-TL1-gen (3243A>G)"
  * ^definition = "DNA(B)—MT-TL1 gene(NC_012920.1:g.3243A>G); arb.cont. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2018-06-22T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #componentSpec
  * ^property[=].valueString = "NC_012920.1:g.3243A>G"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "arbitrært innhold"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU58272 "DNA(B)-MT-TL1-gen"
  * ^definition = "DNA(B)—MT-TL1 gene; seq.var. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2018-06-22T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TL1-gen"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "sekvensvariasjon"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU58273 "DNA(B)-MT-TK-gen"
  * ^definition = "DNA(B)—MT-TK gene; seq.var. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2018-06-22T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-TK-gen"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "sekvensvariasjon"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"

* #NPU58274 "DNA(B)-MT-ATP6-gen"
  * ^definition = "DNA(B)—MT-ATP6 gene; seq.var. = ?"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2018-06-22T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2024-11-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "MT-ATP6-gen"
  * ^property[+].code = #system
  * ^property[=].valueString = "DNA"
  * ^property[+].code = #systemSpec
  * ^property[=].valueString = "Blod"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "sekvensvariasjon"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"
  * ^property[+].code = #secondaryDomain
  * ^property[=].valueString = "Medisinsk genetikk"
  * ^property[+].code = #grouping
  * ^property[=].valueString = "Genetiske undersøkelser"
