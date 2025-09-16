#!/usr/bin/env python3
"""
JSON Parsing Examples in Python
This file demonstrates various ways to parse and work with JSON data.
"""

import json
import os
from typing import Dict, List, Any


def parse_json_file(file_path: str) -> Dict[str, Any]:
    """
    Parse a JSON file and return the data as a Python dictionary.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        Dict[str, Any]: Parsed JSON data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        raise
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file '{file_path}': {e}")
        raise


def main():
    data = parse_json_file("./oss_license_detect_intermediate.json")
    print(data)


if __name__ == "__main__":
    main()
