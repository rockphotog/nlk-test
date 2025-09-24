#!/usr/bin/env python3
"""
FSH CodeSystem Validation Script

This script validates FSH (FHIR Shorthand) CodeSystem files for:
- Syntax correctness
- Structure compliance
- Property consistency
- Code duplication
- Missing required elements
- Common FSH issues
"""

import re
import logging
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict, Counter
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FSHValidator:
    """Validates FSH CodeSystem files for syntax and structure."""
    
    def __init__(self, fsh_file: str):
        """Initialize validator with FSH file path."""
        self.fsh_file = Path(fsh_file)
        self.content = ""
        self.lines = []
        self.issues = []
        self.warnings = []
        self.concepts = {}
        self.properties = {}
        
    def load_file(self) -> bool:
        """Load and parse FSH file."""
        try:
            logger.info(f"Loading FSH file: {self.fsh_file}")
            
            with open(self.fsh_file, 'r', encoding='utf-8') as f:
                self.content = f.read()
                self.lines = self.content.splitlines()
            
            logger.info(f"Loaded {len(self.lines)} lines")
            return True
            
        except Exception as e:
            logger.error(f"Error loading FSH file: {e}")
            return False
    
    def add_issue(self, line_num: int, issue_type: str, message: str, severity: str = "ERROR"):
        """Add validation issue."""
        self.issues.append({
            'line': line_num,
            'type': issue_type,
            'message': message,
            'severity': severity
        })
    
    def add_warning(self, line_num: int, message: str):
        """Add validation warning."""
        self.warnings.append({
            'line': line_num,
            'message': message
        })
    
    def validate_codesystem_header(self) -> bool:
        """Validate CodeSystem header structure."""
        logger.info("Validating CodeSystem header...")
        
        required_elements = [
            'CodeSystem:',
            'Id:',
            'Title:',
            'Description:',
            '* ^url',
            '* ^version',
            '* ^status',
            '* ^content',
            '* ^count'
        ]
        
        found_elements = set()
        
        for i, line in enumerate(self.lines[:100], 1):  # Check first 100 lines
            line = line.strip()
            
            for element in required_elements:
                if element in line:
                    found_elements.add(element)
        
        missing_elements = set(required_elements) - found_elements
        
        if missing_elements:
            for element in missing_elements:
                self.add_issue(0, "MISSING_REQUIRED", f"Missing required CodeSystem element: {element}")
            return False
        
        logger.info("✅ CodeSystem header validation passed")
        return True
    
    def validate_property_definitions(self) -> bool:
        """Validate property definitions."""
        logger.info("Validating property definitions...")
        
        property_pattern = r'^\* \^property\[.*?\]\.code = #(\w+)'
        property_type_pattern = r'^\* \^property\[.*?\]\.type = #(\w+)'
        property_desc_pattern = r'^\* \^property\[.*?\]\.description = "([^"]*)"'
        
        properties_found = {}
        current_property = None
        
        for i, line in enumerate(self.lines, 1):
            line = line.strip()
            
            # Property code
            match = re.match(property_pattern, line)
            if match:
                prop_code = match.group(1)
                current_property = prop_code
                properties_found[prop_code] = {'line': i, 'type': None, 'description': None}
                continue
            
            # Property type
            match = re.match(property_type_pattern, line)
            if match and current_property:
                prop_type = match.group(1)
                if current_property in properties_found:
                    properties_found[current_property]['type'] = prop_type
                continue
            
            # Property description
            match = re.match(property_desc_pattern, line)
            if match and current_property:
                description = match.group(1)
                if current_property in properties_found:
                    properties_found[current_property]['description'] = description
                continue
        
        # Validate property completeness
        valid_types = {'code', 'string', 'dateTime', 'integer', 'boolean', 'decimal'}
        
        for prop_code, prop_info in properties_found.items():
            if not prop_info['type']:
                self.add_issue(prop_info['line'], "MISSING_PROPERTY_TYPE", 
                             f"Property '{prop_code}' missing type definition")
            elif prop_info['type'] not in valid_types:
                self.add_warning(prop_info['line'], 
                               f"Property '{prop_code}' has non-standard type: {prop_info['type']}")
            
            if not prop_info['description']:
                self.add_warning(prop_info['line'], 
                               f"Property '{prop_code}' missing description")
        
        self.properties = properties_found
        logger.info(f"✅ Found {len(properties_found)} property definitions")
        return True
    
    def validate_concepts(self) -> bool:
        """Validate concept definitions."""
        logger.info("Validating concept definitions...")
        
        concept_pattern = r'^\* #([A-Za-z0-9_-]+) "([^"]*)"'
        property_pattern = r'^\s*\* \^property\[\+\]$'
        code_pattern = r'^\s*\* code = #(\w+)$'
        value_pattern = r'^\s*\* value(String|Code|DateTime|Integer|Boolean|Decimal) = (.+)$'
        
        concepts_found = {}
        current_concept = None
        current_property = None
        duplicate_codes = []
        
        for i, line in enumerate(self.lines, 1):
            line_stripped = line.strip()
            
            # New concept
            match = re.match(concept_pattern, line_stripped)
            if match:
                concept_code = match.group(1)
                concept_display = match.group(2)
                
                if concept_code in concepts_found:
                    duplicate_codes.append((concept_code, i, concepts_found[concept_code]['line']))
                
                current_concept = concept_code
                concepts_found[concept_code] = {
                    'line': i,
                    'display': concept_display,
                    'properties': {}
                }
                continue
            
            # Property start
            if re.match(property_pattern, line_stripped) and current_concept:
                current_property = {'code': None, 'value': None, 'line': i}
                continue
            
            # Property code
            match = re.match(code_pattern, line_stripped)
            if match and current_concept and current_property:
                prop_code = match.group(1)
                current_property['code'] = prop_code
                continue
            
            # Property value
            match = re.match(value_pattern, line_stripped)
            if match and current_concept and current_property:
                value_type = match.group(1)
                value = match.group(2)
                current_property['value'] = {'type': value_type, 'content': value}
                
                # Add completed property to concept
                if current_property['code']:
                    prop_code = current_property['code']
                    if prop_code not in concepts_found[current_concept]['properties']:
                        concepts_found[current_concept]['properties'][prop_code] = []
                    concepts_found[current_concept]['properties'][prop_code].append(current_property)
                
                current_property = None
                continue
        
        # Report duplicates
        for code, line1, line2 in duplicate_codes:
            self.add_issue(line1, "DUPLICATE_CONCEPT", 
                         f"Concept '{code}' duplicated (first occurrence at line {line2})")
        
        # Validate concept properties
        for concept_code, concept_info in concepts_found.items():
            # Check for required properties (if any)
            if not concept_info['display']:
                self.add_issue(concept_info['line'], "MISSING_DISPLAY", 
                             f"Concept '{concept_code}' missing display name")
            
            # Validate property usage
            for prop_code, prop_instances in concept_info['properties'].items():
                if prop_code not in self.properties:
                    self.add_warning(concept_info['line'], 
                                   f"Concept '{concept_code}' uses undefined property '{prop_code}'")
        
        self.concepts = concepts_found
        logger.info(f"✅ Found {len(concepts_found)} concepts")
        
        if duplicate_codes:
            logger.warning(f"❌ Found {len(duplicate_codes)} duplicate concepts")
            return False
        
        return True
    
    def validate_syntax(self) -> bool:
        """Validate basic FSH syntax."""
        logger.info("Validating FSH syntax...")
        
        syntax_issues = []
        
        for i, line in enumerate(self.lines, 1):
            line_stripped = line.strip()
            
            # Skip empty lines and comments
            if not line_stripped or line_stripped.startswith('//'):
                continue
            
            # Check for common syntax issues
            
            # Unescaped quotes in strings
            if '"' in line_stripped:
                # Count quotes to check for unescaped quotes
                quote_count = line_stripped.count('"')
                escaped_quote_count = line_stripped.count('\\"')
                effective_quotes = quote_count - escaped_quote_count
                
                if effective_quotes % 2 != 0:
                    self.add_issue(i, "SYNTAX_ERROR", "Unmatched quotes in line")
            
            # Invalid characters in codes
            if line_stripped.startswith('* #'):
                code_match = re.match(r'^\* #([^\s"]+)', line_stripped)
                if code_match:
                    code = code_match.group(1)
                    if not re.match(r'^[A-Za-z0-9_.-]+$', code):
                        self.add_issue(i, "INVALID_CODE", f"Invalid characters in code: {code}")
            
            # Missing required elements
            if '* ^property[' in line_stripped and 'code =' not in line_stripped and 'type =' not in line_stripped:
                if not any('code =' in self.lines[j].strip() or 'type =' in self.lines[j].strip() 
                          for j in range(max(0, i-1), min(len(self.lines), i+3))):
                    self.add_issue(i, "INCOMPLETE_PROPERTY", "Property definition incomplete")
        
        logger.info("✅ Syntax validation completed")
        return len([issue for issue in self.issues if issue['severity'] == 'ERROR']) == 0
    
    def validate_consistency(self) -> bool:
        """Validate data consistency."""
        logger.info("Validating data consistency...")
        
        # Check property usage consistency
        property_usage = defaultdict(list)
        
        for concept_code, concept_info in self.concepts.items():
            for prop_code in concept_info['properties']:
                property_usage[prop_code].append(concept_code)
        
        # Report unused properties
        defined_props = set(self.properties.keys())
        used_props = set(property_usage.keys())
        unused_props = defined_props - used_props
        
        for prop in unused_props:
            self.add_warning(self.properties[prop]['line'], 
                           f"Property '{prop}' defined but never used")
        
        # Report undefined but used properties
        undefined_props = used_props - defined_props
        for prop in undefined_props:
            self.add_issue(0, "UNDEFINED_PROPERTY", f"Property '{prop}' used but not defined")
        
        logger.info(f"✅ Consistency validation completed")
        return True
    
    def generate_statistics(self) -> Dict:
        """Generate validation statistics."""
        stats = {
            'total_lines': len(self.lines),
            'total_concepts': len(self.concepts),
            'total_properties_defined': len(self.properties),
            'total_property_instances': sum(len(concept['properties']) for concept in self.concepts.values()),
            'errors': len([issue for issue in self.issues if issue['severity'] == 'ERROR']),
            'warnings': len(self.warnings),
            'property_usage': {}
        }
        
        # Calculate property usage statistics
        for prop_code in self.properties.keys():
            usage_count = sum(1 for concept in self.concepts.values() 
                            if prop_code in concept['properties'])
            stats['property_usage'][prop_code] = {
                'count': usage_count,
                'percentage': (usage_count / len(self.concepts) * 100) if self.concepts else 0
            }
        
        return stats
    
    def run_validation(self) -> bool:
        """Run complete validation."""
        logger.info("🔍 Starting FSH CodeSystem validation...")
        
        if not self.load_file():
            return False
        
        # Run validation steps
        valid_header = self.validate_codesystem_header()
        valid_properties = self.validate_property_definitions()
        valid_concepts = self.validate_concepts()
        valid_syntax = self.validate_syntax()
        valid_consistency = self.validate_consistency()
        
        # Generate statistics
        stats = self.generate_statistics()
        
        # Print results
        self.print_results(stats)
        
        # Return overall validation result
        return all([valid_header, valid_properties, valid_concepts, valid_syntax, valid_consistency])
    
    def print_results(self, stats: Dict):
        """Print validation results."""
        print("\n" + "=" * 80)
        print("🧬 FSH CodeSystem Validation Results")
        print("=" * 80)
        
        # Statistics
        print(f"\n📊 File Statistics:")
        print(f"   Total lines: {stats['total_lines']:,}")
        print(f"   Total concepts: {stats['total_concepts']:,}")
        print(f"   Properties defined: {stats['total_properties_defined']}")
        print(f"   Property instances: {stats['total_property_instances']:,}")
        
        # Issues
        print(f"\n🔍 Validation Issues:")
        print(f"   Errors: {stats['errors']}")
        print(f"   Warnings: {len(self.warnings)}")
        
        # Print errors
        if self.issues:
            print(f"\n❌ Errors Found:")
            for issue in self.issues:
                if issue['severity'] == 'ERROR':
                    print(f"   Line {issue['line']}: [{issue['type']}] {issue['message']}")
        
        # Print warnings (first 10)
        if self.warnings:
            print(f"\n⚠️  Warnings (showing first 10):")
            for warning in self.warnings[:10]:
                print(f"   Line {warning['line']}: {warning['message']}")
            
            if len(self.warnings) > 10:
                print(f"   ... and {len(self.warnings) - 10} more warnings")
        
        # Property usage
        print(f"\n📋 Property Usage:")
        for prop_code, usage in sorted(stats['property_usage'].items()):
            print(f"   {prop_code}: {usage['count']:,} concepts ({usage['percentage']:.1f}%)")
        
        # Overall result
        if stats['errors'] == 0:
            print(f"\n✅ FSH CodeSystem validation PASSED")
        else:
            print(f"\n❌ FSH CodeSystem validation FAILED ({stats['errors']} errors)")
        
        if self.warnings:
            print(f"⚠️  {len(self.warnings)} warnings found (review recommended)")


def main():
    """Main validation function."""
    
    # Default FSH file path
    fsh_file = "/Users/espen/git/nlk-test/nlk-test/input/fsh/codesystems/nlk-test.codesystem-detailed.fsh"
    
    # Allow command line argument
    if len(sys.argv) > 1:
        fsh_file = sys.argv[1]
    
    if not Path(fsh_file).exists():
        print(f"❌ FSH file not found: {fsh_file}")
        return False
    
    print("🔍 FSH CodeSystem Validator")
    print("=" * 40)
    print(f"Validating: {fsh_file}")
    
    # Run validation
    validator = FSHValidator(fsh_file)
    success = validator.run_validation()
    
    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)