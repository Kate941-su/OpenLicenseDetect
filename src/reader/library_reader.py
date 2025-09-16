

from dataclasses import dataclass
import json
import re
from src.model.oss_type import OSSType
from src.constant import license_file_name

@dataclass
class LibraryObject:
    author: str
    year: int
    oss_type: OSSType
    raw_license_text: str
    _output_file_name: str = "oss_license_detect_intermediate"

    def __init__(self, path_to_license_text: str):
        with open(path_to_license_text, "r") as f:
            license_text = f.read()
        self.oss_type = self._detect_license_type(license_text)
        self.author = self._extract_author(license_text)
        self.year = self._extract_year(license_text)
        self.raw_license_text = license_text
    
    def _detect_license_type(self, license_text: str) -> OSSType:
        """Detect the license type from the license text."""
        license_text_lower = license_text.lower()
        
        # MIT License detection
        if "mit license" in license_text_lower or "permission is hereby granted" in license_text_lower:
            return OSSType.MIT
        
        # Apache License detection
        if "apache license" in license_text_lower or "apache-2.0" in license_text_lower:
            return OSSType.APACHE_2_0
        
        # GPL detection
        if "gnu general public license" in license_text_lower or "gpl" in license_text_lower:
            if "version 3" in license_text_lower or "gpl-3" in license_text_lower:
                return OSSType.GPL_3_0
            elif "version 2" in license_text_lower or "gpl-2" in license_text_lower:
                return OSSType.GPL_2_0
        
        # BSD detection
        if "bsd 3-clause" in license_text_lower or "3 clause" in license_text_lower:
            return OSSType.BSD_3_CLAUSE
        if "bsd 2-clause" in license_text_lower or "2 clause" in license_text_lower:
            return OSSType.BSD_2_CLAUSE
    
        # ISC License detection
        if "isc license" in license_text_lower or "internet systems consortium" in license_text_lower:
            return OSSType.ISC
        
        # Unlicense detection
        if "unlicense" in license_text_lower or "public domain" in license_text_lower:
            return OSSType.UNLICENSE
            
        # Default to OTHER if no specific license is detected
        return OSSType.OTHER
    
    def _extract_author(self, license_text: str) -> str:
        """Extract author name from copyright notice."""
        # Look for copyright patterns
        copyright_patterns = [
            r"copyright\s+\(c\)\s+\d+\s+(.+)",
            r"copyright\s+©\s+\d+\s+(.+)",
            r"copyright\s+\d+\s+(.+)",
            r"©\s+\d+\s+(.+)"
        ]
        
        for pattern in copyright_patterns:
            match = re.search(pattern, license_text, re.IGNORECASE)
            if match:
                author = match.group(1).strip()
                # Clean up the author name (remove extra text)
                author = re.sub(r'\s+all rights reserved.*$', '', author, flags=re.IGNORECASE)
                return author
        
        return "Unknown"
    
    def _extract_year(self, license_text: str) -> int:
        """Extract year from copyright notice."""
        # Look for year patterns in copyright notices
        year_patterns = [
            r"copyright\s+\(c\)\s+(\d{4})",
            r"copyright\s+©\s+(\d{4})",
            r"copyright\s+(\d{4})",
            r"©\s+(\d{4})"
        ]
        
        for pattern in year_patterns:
            match = re.search(pattern, license_text, re.IGNORECASE)
            if match:
                return int(match.group(1))
        
        # If no year found, return current year as default
        import datetime
        return datetime.datetime.now().year

    def parse_license_text(self):
        """Parse the license text from the raw license text."""
        self.raw_license_text = self.raw_license_text.split(license_file_name)

    def generate_file(self):
        """Generate a JSON file with the library information and license text."""
        data = {
            "author": self.author,
            "year": self.year,
            "oss_type": self.oss_type.value,
            "raw_license_text": self.raw_license_text
        }
        
        with open(f"{self._output_file_name}.json", "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)