#!/usr/bin/env python3
"""
Fix FSH Property Syntax

This script converts multi-line property assignments to single-line format
to comply with FHIR Shorthand specification requirements.

Converts from:
  * ^property[+]
    * code = #validFrom
    * valueDateTime = "2013-01-25T00:00:00+00:00"

To:
  * ^property[+].code = #validFrom
  * ^property[=].valueDateTime = "2013-01-25T00:00:00+00:00"
"""

import re
import sys
from pathlib import Path
from datetime import datetime


def fix_fsh_property_syntax(content: str) -> str:
    """
    Fix FSH property syntax by converting multi-line to single-line format.
    """
    lines = content.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a property start line
        if re.match(r'^\s*\* \^property\[\+\]$', line):
            indent = len(line) - len(line.lstrip())
            base_indent = ' ' * indent
            
            # Look ahead for code and value lines
            code_line = None
            value_line = None
            
            # Check next two lines for code and value
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line.startswith('* code = #'):
                    code_line = next_line
                    code_value = next_line.replace('* code = #', '')
                    
                    # Look for value line
                    if i + 2 < len(lines):
                        value_next_line = lines[i + 2].strip()
                        if value_next_line.startswith('* value'):
                            value_line = value_next_line
                            value_content = value_next_line.replace('* ', '')
                            
                            # Create fixed lines
                            fixed_lines.append(f"{base_indent}* ^property[+].code = #{code_value}")
                            fixed_lines.append(f"{base_indent}* ^property[=].{value_content}")
                            
                            # Skip the processed lines
                            i += 3
                            continue
            
            # If we couldn't match the pattern, keep the original line
            fixed_lines.append(line)
            i += 1
        else:
            # Keep non-property lines as-is
            fixed_lines.append(line)
            i += 1
    
    return '\n'.join(fixed_lines)


def main():
    """Main function to fix FSH file syntax."""
    
    if len(sys.argv) != 3:
        print("Usage: python fix_fsh_syntax.py <input_file> <output_file>")
        print("Example: python fix_fsh_syntax.py input.fsh output.fsh")
        return 1
    
    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])
    
    if not input_file.exists():
        print(f"❌ Error: Input file not found: {input_file}")
        return 1
    
    print(f"🔧 Fixing FSH property syntax...")
    print(f"📖 Reading: {input_file}")
    
    # Read the input file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return 1
    
    # Count original patterns
    original_patterns = len(re.findall(r'^\s*\* \^property\[\+\]$', content, re.MULTILINE))
    print(f"📊 Found {original_patterns:,} multi-line property patterns to fix")
    
    # Fix the syntax
    fixed_content = fix_fsh_property_syntax(content)
    
    # Count remaining patterns (should be 0)
    remaining_patterns = len(re.findall(r'^\s*\* \^property\[\+\]$', fixed_content, re.MULTILINE))
    
    # Write the output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return 1
    
    print(f"💾 Fixed file written to: {output_file}")
    print(f"✅ Conversion complete!")
    print(f"📈 Statistics:")
    print(f"   - Original multi-line patterns: {original_patterns:,}")
    print(f"   - Remaining patterns: {remaining_patterns:,}")
    print(f"   - Fixed patterns: {original_patterns - remaining_patterns:,}")
    
    if remaining_patterns == 0:
        print(f"🎉 All property syntax issues fixed!")
    else:
        print(f"⚠️  Warning: {remaining_patterns} patterns still need fixing")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())