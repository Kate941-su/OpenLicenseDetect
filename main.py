import src.library_reader as reader


if __name__ == "__main__":
    reader = reader.LibraryObject(path_to_license_text="license/lgpl-2/LICENSE")
    print(reader.oss_type.value)