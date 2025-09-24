#!/usr/bin/env python3
"""
Extract Medical Genetics codes from the detailed NLK FSH file.
Creates a smaller version containing only codes with primaryDomain = "Medisinsk genetikk"
"""
import re
import sys

def extract_medical_genetics_codes(input_file, output_file):
    """Extract only Medical Genetics codes from the detailed FSH file."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the header section (everything before the first code definition)
    header_match = re.search(r'^(.*?)(^\* #[A-Z0-9]+)', content, re.MULTILINE | re.DOTALL)
    if not header_match:
        print("❌ Could not find FSH header section")
        return False
    
    header = header_match.group(1)
    
    # Split content into individual code blocks using a more specific pattern
    # Each code starts with '* #' followed by properties until the next '* #'
    code_sections = re.split(r'^(\* #[A-Z0-9]+ .*?)$', content, flags=re.MULTILINE)
    
    # Reconstruct code blocks by pairing code definitions with their properties
    code_blocks = []
    for i in range(1, len(code_sections), 2):
        code_def = code_sections[i]
        if i + 1 < len(code_sections):
            properties = code_sections[i + 1]
            code_blocks.append(code_def + properties)
        else:
            code_blocks.append(code_def)
    
    print(f"📊 Found {len(code_blocks)} total code blocks")
    
    # Filter for Medical Genetics codes
    medical_genetics_blocks = []
    for block in code_blocks:
        # Look for primaryDomain = "Medisinsk genetikk" pattern
        if re.search(r'primaryDomain.*?valueString.*?"Medisinsk genetikk"', block, re.DOTALL):
            medical_genetics_blocks.append(block)
    
    print(f"🧬 Found {len(medical_genetics_blocks)} Medical Genetics codes")
    
    if not medical_genetics_blocks:
        print("❌ No Medical Genetics codes found")
        return False
    
    # Update header for the smaller CodeSystem
    updated_header = header.replace(
        'CodeSystem: NorskLaboratoriekodeverkDetailed',
        'CodeSystem: NorskLaboratoriekodeverkMedicalGenetics'
    ).replace(
        'Id: norsk-laboratoriekodeverk-detailed',
        'Id: norsk-laboratoriekodeverk-medical-genetics'
    ).replace(
        'Title: "Norsk Laboratoriekodeverk"',
        'Title: "Norsk Laboratoriekodeverk - Medical Genetics"'
    ).replace(
        'Description: "Norwegian Laboratory Codebook - a comprehensive terminology for laboratory medicine in Norway with complete metadata properties"',
        'Description: "Norwegian Laboratory Codebook - Medical Genetics domain subset with complete metadata properties"'
    ).replace(
        '"http://hl7.no/fhir/ig/nlk-test/CodeSystem/norsk-laboratoriekodeverk-detailed"',
        '"http://hl7.no/fhir/ig/nlk-test/CodeSystem/norsk-laboratoriekodeverk-medical-genetics"'
    ).replace(
        f'* ^count = 11391',
        f'* ^count = {len(medical_genetics_blocks)}'
    )
    
    # Update the comment header
    updated_header = re.sub(
        r'// Total concepts: \d+',
        f'// Total concepts: {len(medical_genetics_blocks)}',
        updated_header
    )
    updated_header = re.sub(
        r'// Active concepts: \d+',
        f'// Active concepts: {len([b for b in medical_genetics_blocks if "validTo" not in b or "validTo.*2[0-9]{3}" in b])}',
        updated_header
    )
    
    # Combine header with Medical Genetics codes
    result = updated_header + '\n'.join(medical_genetics_blocks)
    
    # Write the result
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print(f"✅ Medical Genetics CodeSystem written to: {output_file}")
    print(f"📈 Statistics:")
    print(f"   - Total codes: {len(medical_genetics_blocks)}")
    print(f"   - File size reduced from {len(content):,} to {len(result):,} characters")
    
    return True

def main():
    input_file = '/Users/espen/git/nlk-test/nlk-test/input/fsh/codesystems/nlk-test.codesystem-detailed.fsh'
    output_file = '/Users/espen/git/nlk-test/nlk-test/input/fsh/codesystems/nlk-test.codesystem-medical-genetics.fsh'
    
    print("🧬 Extracting Medical Genetics codes from detailed NLK CodeSystem...")
    print(f"📖 Input: {input_file}")
    print(f"💾 Output: {output_file}")
    
    success = extract_medical_genetics_codes(input_file, output_file)
    
    if success:
        print("🎉 Medical Genetics extraction complete!")
    else:
        print("❌ Extraction failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()