import os
import json
from pathlib import Path
from src.reader.library_reader import LibraryObject
from src.constant import license_file_name

class LibraryObjectManager:    
    def __init__(self, library_directory_path: str):
        self.library_object_list = []
        self.library_directory_path = library_directory_path
        self.library_paths = []  # Store library paths

    def crawling_library_directory(self):
        """Crawling the library directory and create LibraryObject instances."""
        if not os.path.exists(self.library_directory_path):
            print(f"Directory {self.library_directory_path} does not exist")
            return

        # Walk through the directory tree to find LICENSE files
        for root, dirs, files in os.walk(self.library_directory_path):
            # Look for LICENSE files in current directory
            if license_file_name in files:
                # Get the full path of the LICENSE file
                license_path = os.path.join(root, license_file_name)
                library_path = root  # The directory containing the LICENSE file
                print(f"Full LICENSE path: {os.path.abspath(license_path)}")
                
                try:
                    # Create LibraryObject and store the library path
                    library_obj = LibraryObject(license_path)
                    library_obj.library_path = library_path  # Add library path to the object
                    
                    self.library_object_list.append(library_obj)
                    self.library_paths.append(library_path)
                    
                except Exception as e:
                    print(f"Error processing {license_path}: {e}")
        
        print(f"Total libraries found: {len(self.library_object_list)}")
        # print(f"Library paths: {self.library_paths}")

    def generate_file(self):
        """Generate a JSON file with the library information and license text."""
        # Convert LibraryObject instances to dictionaries for JSON serialization
        library_data = []
        for i, library_obj in enumerate(self.library_object_list):
            library_dict = {
                "author": library_obj.author,
                "year": library_obj.year,
                "oss_type": library_obj.oss_type.value,
                "raw_license_text": library_obj.raw_license_text
            }
            library_data.append(library_dict)
        
        data = {
            "library_object_list": library_data,
            "total_libraries": len(self.library_object_list),
            "library_paths": self.library_paths
        }
        with open(f"oss_license_detect_intermediate.json", "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)