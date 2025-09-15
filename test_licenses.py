#!/usr/bin/env python3
"""
Test script to demonstrate license parsing functionality.
This script reads license files from the licenses directory and parses them.
"""

import os
from src.library_reader import LibraryObject

def test_license_parsing():
    """Test license parsing with sample files."""
    licenses_dir = "license"
    
    if not os.path.exists(licenses_dir):
        print(f"Error: {licenses_dir} directory not found!")
        return
    
    # Get all license files
    license_files = [f for f in os.listdir(licenses_dir) if f.endswith('.txt')]
    
    if not license_files:
        print(f"No license files found in {licenses_dir} directory!")
        return
    
    print(f"Found {len(license_files)} license files to test:")
    print("-" * 50)
    
    for license_file in license_files:
        file_path = os.path.join(licenses_dir, license_file)
        library_name = os.path.splitext(license_file)[0]
        
        try:
            # Read the license file
            with open(file_path, 'r', encoding='utf-8') as f:
                license_text = f.read()
            
            # Parse the license using LibraryObject
            library = LibraryObject.from_license_text(library_name, license_text)
            
            # Display results
            print(f"File: {license_file}")
            print(f"  Library Name: {library.library_name}")
            print(f"  Author: {library.author}")
            print(f"  Year: {library.year}")
            print(f"  License Type: {library.oss_type.value}")
            print(f"  License Text Length: {len(library.raw_license_text)} characters")
            print()
            
            # Generate JSON file
            library.generate_file()
            print(f"  ✓ Generated {library.library_name}.json")
            print("-" * 50)
            
        except Exception as e:
            print(f"Error processing {license_file}: {e}")
            print("-" * 50)

if __name__ == "__main__":
    test_license_parsing()
