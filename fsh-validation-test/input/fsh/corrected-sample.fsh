// Norwegian Laboratory Codebook (Norsk Laboratoriekodeverk) - Enhanced with Complete Properties
// Sample for FSH validation testing
// Generated on: 2025-09-24

CodeSystem: NorskLaboratoriekodeverkDetailed
Id: norsk-laboratoriekodeverk-detailed
Title: "Norsk Laboratoriekodeverk Sample"
Description: "Norwegian Laboratory Codebook - sample for validation testing"
* ^url = "http://hl7.no/fhir/ig/nlk-test/CodeSystem/norsk-laboratoriekodeverk-detailed"
* ^version = "7280.77"
* ^status = #active
* ^experimental = true
* ^date = "2025-09-24"
* ^publisher = "Espen"
* ^contact.name = "Espen"
* ^jurisdiction = urn:iso:std:iso:3166#NO "Norway"
* ^caseSensitive = true
* ^content = #complete
* ^count = 3

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

* ^property[+].code = #component
* ^property[=].description = "Component being measured"
* ^property[=].type = #string

* ^property[+].code = #system
* ^property[=].description = "System/specimen type"
* ^property[=].type = #string

* ^property[+].code = #propertyType
* ^property[=].description = "Type of property measured"
* ^property[=].type = #string

* ^property[+].code = #unit
* ^property[=].description = "Unit of measurement"
* ^property[=].type = #string

* ^property[+].code = #primaryDomain
* ^property[=].description = "Primary medical domain"
* ^property[=].type = #string

// Concepts with properties using correct syntax
* #NOR05001 "P-ACE"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #validTo
  * ^property[=].valueDateTime = "2020-02-29T23:59:00+00:00"
  * ^property[+].code = #replacedBy
  * ^property[=].valueCode = #NPU29069
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"

* #NOR05003 "Us-Osmolalitet"
  * ^definition = "Syst(spec.)—Solute; molal.(proc.) = ? mosmol/kg"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
  * ^property[+].code = #changeDate
  * ^property[=].valueDateTime = "2017-02-28T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Oppløste stoffer"
  * ^property[+].code = #system
  * ^property[=].valueString = "Urin"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "molalitet"
  * ^property[+].code = #unit
  * ^property[=].valueString = "mosmol/kg"
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Medisinsk biokjemi"

* #NPU62708 "P-IgE Sander vitreus, f415"
  * ^definition = "P—Walleye pike antibody(IgE); arb.subst.c.(f415; proc.) = ? (p.d.u.)"
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2025-09-23T00:00:00+00:00"
  * ^property[+].code = #component
  * ^property[=].valueString = "Sander vitreus antistoff"
  * ^property[+].code = #system
  * ^property[=].valueString = "Plasma"
  * ^property[+].code = #propertyType
  * ^property[=].valueString = "arbitrær stoffkonsentrasjon"
  * ^property[+].code = #unit
  * ^property[=].valueString = "p.d.e."
  * ^property[+].code = #primaryDomain
  * ^property[=].valueString = "Immunologi og transfusjonsmedisin"