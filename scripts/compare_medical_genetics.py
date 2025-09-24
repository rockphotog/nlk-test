#!/usr/bin/env python3
"""
Compare Medical Genetics codes between CSV source and FSH file
"""

import pandas as pd
import re
import sys

def extract_fsh_codes(fsh_file_path):
    """Extract codes and properties from FSH file"""
    codes = {}
    current_code = None
    
    with open(fsh_file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            
            # Match code definitions: * #NOR15177 "DNA-Mitokondriegenom-sekvensering"
            code_match = re.match(r'^\* #([A-Z0-9]+) "([^"]+)"', line)
            if code_match:
                code_id = code_match.group(1)
                display_name = code_match.group(2)
                codes[code_id] = {
                    'display': display_name,
                    'properties': {},
                    'line': line_num
                }
                current_code = code_id
                continue
            
            # Match property assignments - handle multi-line FSH syntax
            if current_code and '  * ^property[' in line:
                if 'code = #' in line:
                    # This line defines the property code
                    prop_match = re.search(r'code = #(\w+)', line)
                    if prop_match:
                        codes[current_code]['_current_prop'] = prop_match.group(1)
                elif 'valueString = ' in line and '_current_prop' in codes[current_code]:
                    # This line defines the property value
                    value_match = re.search(r'valueString = "([^"]+)"', line)
                    if value_match:
                        prop_name = codes[current_code]['_current_prop']
                        prop_value = value_match.group(1)
                        codes[current_code]['properties'][prop_name] = prop_value
                elif 'valueDateTime = ' in line and '_current_prop' in codes[current_code]:
                    # This line defines the property value
                    value_match = re.search(r'valueDateTime = "([^"]+)"', line)
                    if value_match:
                        prop_name = codes[current_code]['_current_prop']
                        prop_value = value_match.group(1)
                        codes[current_code]['properties'][prop_name] = prop_value
    
    return codes

def load_csv_genetics_codes(csv_file_path):
    """Load Medical Genetics codes from CSV"""
    df = pd.read_csv(csv_file_path)
    
    # Filter for Medical Genetics codes
    genetics_df = df[
        (df['primært_fagområde'] == 'Medisinsk genetikk') |
        (df['sekundært_fagområde'] == 'Medisinsk genetikk')
    ]
    
    return genetics_df

def compare_codes():
    """Compare codes between CSV and FSH"""
    print("🔍 Comparing Medical Genetics codes between CSV and FSH...")
    
    # Load data
    csv_file = "/Users/espen/git/nlk-test/nlk-test/resources/csv_output/norsk_laboratoriekodeverk_7280.77-clean_full_deduplicated.csv"
    fsh_file = "/Users/espen/git/nlk-test/nlk-test/input/fsh/codesystems/nlk-test.codesystem-medical-genetics.fsh"
    
    try:
        csv_codes = load_csv_genetics_codes(csv_file)
        fsh_codes = extract_fsh_codes(fsh_file)
        
        print(f"📊 CSV Medical Genetics codes: {len(csv_codes)}")
        print(f"📊 FSH codes extracted: {len(fsh_codes)}")
        
        # Debug: show first FSH code
        if fsh_codes:
            first_code = list(fsh_codes.keys())[0]
            print(f"🔍 Debug - First FSH code: {first_code}")
            print(f"   Properties: {fsh_codes[first_code]['properties']}")
            print(f"   Line: {fsh_codes[first_code]['line']}")
        
        # Check code coverage
        csv_code_set = set(csv_codes['kode'].tolist())
        fsh_code_set = set(fsh_codes.keys())
        
        missing_in_fsh = csv_code_set - fsh_code_set
        extra_in_fsh = fsh_code_set - csv_code_set
        
        if missing_in_fsh:
            print(f"❌ Missing in FSH: {len(missing_in_fsh)} codes")
            for code in list(missing_in_fsh)[:5]:
                print(f"   - {code}")
        else:
            print("✅ All CSV codes present in FSH")
            
        if extra_in_fsh:
            print(f"❌ Extra in FSH: {len(extra_in_fsh)} codes")
            for code in list(extra_in_fsh)[:5]:
                print(f"   - {code}")
        else:
            print("✅ No extra codes in FSH")
        
        # Detailed comparison of first 5 codes
        print("\n🔬 Detailed comparison (first 5 codes):")
        for i, (_, csv_row) in enumerate(csv_codes.head(5).iterrows()):
            code = csv_row['kode']
            print(f"\n📋 {code} - {csv_row['norsk_bruksnavn']}")
            
            if code in fsh_codes:
                fsh_code = fsh_codes[code]
                
                # Compare display names
                csv_display = str(csv_row['norsk_bruksnavn'])
                fsh_display = fsh_code['display']
                if csv_display == fsh_display:
                    print(f"   ✅ Display: '{fsh_display}'")
                else:
                    print(f"   ❌ Display mismatch:")
                    print(f"      CSV: '{csv_display}'")
                    print(f"      FSH: '{fsh_display}'")
                
                # Compare dates
                if pd.notna(csv_row['gyldig_fra']):
                    csv_from = str(csv_row['gyldig_fra']).replace(' ', 'T') + '+00:00'
                    fsh_from = fsh_code['properties'].get('validFrom', 'missing')
                    if csv_from == fsh_from:
                        print(f"   ✅ ValidFrom: {fsh_from}")
                    else:
                        print(f"   ❌ ValidFrom mismatch: CSV='{csv_from}' FSH='{fsh_from}'")
                
                # Compare primary domain
                csv_primary = str(csv_row['primært_fagområde'])
                fsh_primary = fsh_code['properties'].get('primaryDomain', 'missing')
                if csv_primary == fsh_primary:
                    print(f"   ✅ Primary Domain: '{fsh_primary}'")
                else:
                    print(f"   ❌ Primary Domain mismatch: CSV='{csv_primary}' FSH='{fsh_primary}'")
            else:
                print(f"   ❌ Code not found in FSH")
        
        print(f"\n🏆 SUMMARY:")
        print(f"   Total codes: {len(csv_codes)} (CSV) vs {len(fsh_codes)} (FSH)")
        print(f"   Code coverage: {'✅ Perfect' if len(missing_in_fsh) == 0 and len(extra_in_fsh) == 0 else '❌ Issues found'}")
        
    except Exception as e:
        print(f"❌ Error during comparison: {e}")
        return False
    
    return True

if __name__ == "__main__":
    compare_codes()