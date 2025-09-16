import argparse
import sys
import os
import src.reader.library_reader as reader
from src.library_object_manager.library_object_manager import LibraryObjectManager


def main():
    parser = argparse.ArgumentParser(description="Crawl LICENSE files in a directory")
    parser.add_argument(
        "path", 
        nargs="?", 
        default=".", 
        help="Path to the directory to crawl for LICENSE files (default: current directory)"
    )
    parser.add_argument(
        "-v", "--verbose", 
        action="store_true", 
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Check if path exists
    if not os.path.exists(args.path):
        print(f"Error: Path '{args.path}' does not exist")
        sys.exit(1)
    
    # Check if path is a directory
    if not os.path.isdir(args.path):
        print(f"Error: '{args.path}' is not a directory")
        sys.exit(1)
    
    if args.verbose:
        print(f"Crawling directory: {os.path.abspath(args.path)}")
    
    manager = LibraryObjectManager(library_directory_path=args.path)
    manager.crawling_library_directory()
    manager.generate_file()
    
    if args.verbose:
        print("License detection completed successfully!")


if __name__ == "__main__":
    main()
