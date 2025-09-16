import src.reader.library_reader as reader
from src.library_object_manager.library_object_manager import LibraryObjectManager

if __name__ == "__main__":
    manager = LibraryObjectManager(library_directory_path="node_modules")
    manager.crawling_library_directory()
    manager.generate_file()
