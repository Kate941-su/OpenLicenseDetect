#!/usr/bin/env python3
"""
Pytest tests for license parsing functionality.
This module tests the LibraryObject license parsing with various license files.
"""

import os
import pytest
import json
from pathlib import Path
from src.reader.library_reader import LibraryObject
from src.model.oss_type import OSSType


class TestLicenseParsing:
    """Test class for license parsing functionality."""
    
    @pytest.fixture
    def licenses_dir(self):
        """Fixture providing the path to the license directory."""
        return "license"
    
    @pytest.fixture
    def license_files(self, licenses_dir):
        """Fixture providing list of license directories."""
        if not os.path.exists(licenses_dir):
            pytest.skip(f"License directory {licenses_dir} not found")
        
        # Get all license directories (not .txt files)
        license_dirs = [d for d in os.listdir(licenses_dir) 
                       if os.path.isdir(os.path.join(licenses_dir, d))]
        
        if not license_dirs:
            pytest.skip(f"No license directories found in {licenses_dir}")
        
        return license_dirs
    
    def test_license_directory_exists(self, licenses_dir):
        """Test that the license directory exists."""
        assert os.path.exists(licenses_dir), f"License directory {licenses_dir} should exist"
    
    def test_license_files_exist(self, license_files):
        """Test that license files are found."""
        assert len(license_files) > 0, "Should have at least one license directory"
        assert len(license_files) >= 10, f"Expected at least 10 license directories, found {len(license_files)}"
    
    @pytest.mark.parametrize("license_name", [
        "mit", "apache-2", "bsd-3", "gpl-3", "isc", "unlicense",
        "bsd-2", "gpl-2", "lgpl-2", "lgpl-3", "mpl-2", "epl-2", 
        "cddl-1", "cc0-1", "agpl-3"
    ])
    def test_license_parsing(self, licenses_dir, license_name):
        """Test parsing of individual license files."""
        license_path = os.path.join(licenses_dir, license_name, "LICENSE")
        
        # Skip if license file doesn't exist
        if not os.path.exists(license_path):
            pytest.skip(f"License file {license_path} not found")
        
        # Read the license file
        # Parse the license using LibraryObject
        library = LibraryObject(license_path)
        
        # Basic assertions
        assert library.author is not None
        assert library.year is not None
        assert library.oss_type is not None
        assert library.raw_license_text is not None
        assert len(library.raw_license_text) > 0
        
        # Test JSON generation
        json_file_name = f"{library._output_file_name}.json"
        library.generate_file()
        
        # Verify JSON file was created
        assert os.path.exists(json_file_name)
        
        # Verify JSON content
        with open(json_file_name, 'r') as f:
            json_data = json.load(f)
        
        assert json_data["author"] == library.author
        assert json_data["year"] == library.year
        assert json_data["oss_type"] == library.oss_type.value
        assert json_data["raw_license_text"] == library.raw_license_text
        
        # Clean up generated JSON file
        os.remove(json_file_name)
    
    def test_mit_license_detection(self, licenses_dir):
        """Test specific MIT license detection."""
        mit_path = os.path.join(licenses_dir, "mit", "LICENSE")
        
        if not os.path.exists(mit_path):
            pytest.skip("MIT license file not found")
        
        library = LibraryObject(mit_path)
        
        assert library.oss_type == OSSType.MIT
        assert "Kaito Kitaya" in library.author or "Open Source Project" in library.author
        assert library.year == 2023
    
    def test_apache_license_detection(self, licenses_dir):
        """Test specific Apache license detection."""
        apache_path = os.path.join(licenses_dir, "apache-2", "LICENSE")
        
        if not os.path.exists(apache_path):
            pytest.skip("Apache license file not found")
        
        library = LibraryObject(apache_path)
        assert library.oss_type == OSSType.APACHE_2_0
        assert library.year is not None
    
    def test_gpl_license_detection(self, licenses_dir):
        """Test specific GPL license detection."""
        gpl_path = os.path.join(licenses_dir, "gpl-3", "LICENSE")
        
        if not os.path.exists(gpl_path):
            pytest.skip("GPL license file not found")
        
        library = LibraryObject(gpl_path)
        
        assert library.oss_type == OSSType.GPL_3_0
        assert library.year is not None
    
    @pytest.mark.parametrize("license_name", [
        "bsd-3", "bsd-2"
    ])
    def test_bsd_license_detection(self, licenses_dir, license_name):
        """Test specific BSD license detection."""
        bsd_path = os.path.join(licenses_dir, license_name, "LICENSE")
        
        if not os.path.exists(bsd_path):
            pytest.skip("BSD license file not found")
        
        library = LibraryObject(bsd_path)
        
        assert library.oss_type == OSSType.BSD_3_CLAUSE if license_name == "bsd-3" else OSSType.BSD_2_CLAUSE
        assert library.year is not None
    
    def test_isc_license_detection(self, licenses_dir):
        """Test specific ISC license detection."""
        isc_path = os.path.join(licenses_dir, "isc", "LICENSE")
        
        if not os.path.exists(isc_path):
            pytest.skip("ISC license file not found")
        
        library = LibraryObject(isc_path)
        
        assert library.oss_type == OSSType.ISC
        assert library.year is not None
    
    def test_unlicense_detection(self, licenses_dir):
        """Test specific Unlicense detection."""
        unlicense_path = os.path.join(licenses_dir, "unlicense", "LICENSE")
        
        if not os.path.exists(unlicense_path):
            pytest.skip("Unlicense file not found")
        
        library = LibraryObject(unlicense_path)
        print(library.oss_type)
        assert library.oss_type == OSSType.UNLICENSE
        assert library.year is not None
    
    def test_json_generation_format(self, licenses_dir):
        """Test that generated JSON has the correct format."""
        mit_path = os.path.join(licenses_dir, "mit", "LICENSE")
        if not os.path.exists(mit_path):
            pytest.skip("MIT license file not found")
        library = LibraryObject(mit_path)
        library.generate_file()
        json_file = "oss_license_detect_intermediate.json"
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            
            # Check required fields
            required_fields = ["author", "year", "oss_type", "raw_license_text"]
            for field in required_fields:
                assert field in json_data, f"JSON should contain {field} field"
            
            # Check data types
            assert isinstance(json_data["author"], str)
            assert isinstance(json_data["year"], int)
            assert isinstance(json_data["oss_type"], str)
            assert isinstance(json_data["raw_license_text"], str)
            
        finally:
            # Clean up
            if os.path.exists(json_file):
                os.remove(json_file)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
