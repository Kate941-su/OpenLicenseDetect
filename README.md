# OpenLicenseDetect

A Python tool for automatically detecting and managing Open Source Software (OSS) licenses in your projects.

## 📋 Abstract

OpenLicenseDetect is a command-line tool that scans directories for LICENSE files, automatically detects the license type, extracts metadata (author, year, license text), and generates structured JSON output. It's designed to help developers and organizations maintain compliance with OSS licensing requirements by providing a comprehensive overview of all licenses used in their projects.

## 🎯 Purpose

The primary purpose of this project is to **manage OSS licenses** by:

- **Automatically detecting OSS license files** in project directories (including node_modules)
- **Parsing license content** to identify license types (MIT, Apache-2.0, GPL, BSD, etc.)
- **Extracting metadata** such as copyright holders, years, and license text
- **Generating formatted JSON files** for easy integration with compliance tools
- **Supporting future YAML output** for enhanced flexibility

### Supported License Types

- MIT
- Apache-2.0
- GPL-2.0, GPL-3.0
- BSD-2-Clause, BSD-3-Clause
- ISC
- LGPL-2.1, LGPL-3.0
- MPL-2.0
- EPL-2.0
- CDDL-1.1
- CC0-1.0
- AGPL-3.0
- Unlicense
- Other (fallback for unrecognized licenses)

## 🚀 How to Use

### Prerequisites

- Python 3.9 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd OpenLicenseDetect
   ```

2. **Set up virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Basic Usage

1. **Scan current directory:**
   ```bash
   python main.py
   ```

2. **Scan specific directory:**
   ```bash
   python main.py /path/to/your/project
   python main.py ./node_modules
   ```

3. **Use with verbose output:**
   ```bash
   python main.py -v /path/to/project
   python main.py --verbose
   ```

4. **Get help:**
   ```bash
   python main.py -h
   ```

### Output

The tool generates `oss_license_detect_intermediate.json` containing:

```json
{
  "library_object_list": [
    {
      "author": "Copyright Holder Name",
      "year": 2023,
      "oss_type": "MIT",
      "raw_license_text": "Full license text..."
    }
  ],
  "total_libraries": 15,
  "library_paths": ["path/to/library1", "path/to/library2"]
}
```

### Programmatic Usage

```python
from src.library_object_manager.library_object_manager import LibraryObjectManager

# Create manager instance
manager = LibraryObjectManager("/path/to/project")

# Crawl for LICENSE files
manager.crawling_library_directory()

# Generate JSON output
manager.generate_file()
```

## 🧪 How to Test

### Run All Tests

```bash
# Activate virtual environment first
source venv/bin/activate

# Run all tests
python -m pytest test_licenses.py -v
```

### Run Specific Tests

```bash
# Run a specific test method
python -m pytest test_licenses.py::TestLicenseParsing::test_license_directory_exists -v

# Run tests by keyword
python -m pytest test_licenses.py -k "mit" -v

# Run with coverage
python -m pytest test_licenses.py --cov=src --cov-report=html
```

### Test Individual License Detection

```bash
# Test MIT license detection
python -m pytest test_licenses.py::TestLicenseParsing::test_mit_license_detection -v

# Test Apache license detection
python -m pytest test_licenses.py::TestLicenseParsing::test_apache_license_detection -v
```

### Development Testing

```bash
# Run linting
flake8 src/ test_licenses.py

# Run type checking
mypy src/

# Format code
black src/ test_licenses.py

# Sort imports
isort src/ test_licenses.py
```

## 📁 Project Structure

```
OpenLicenseDetect/
├── src/
│   ├── library_object_manager/
│   │   └── library_object_manager.py    # Main crawling and management logic
│   ├── reader/
│   │   └── library_reader.py            # License parsing and detection
│   ├── model/
│   │   └── oss_type.py                  # License type enumeration
│   └── constant.py                      # Constants (LICENSE filename)
├── license/                             # Sample license files for testing
│   ├── mit/
│   ├── apache-2/
│   └── ...
├── example/
│   └── python/
│       └── example.py                   # JSON parsing examples
├── test_licenses.py                     # Test suite
├── main.py                              # CLI entry point
├── requirements.txt                     # Python dependencies
├── pyproject.toml                       # Project configuration
└── README.md                            # This file
```

## 🔧 Configuration

The project uses `pyproject.toml` for configuration:

- **Black**: Code formatting (88 character line length)
- **MyPy**: Type checking with strict settings
- **Pytest**: Testing configuration with coverage
- **isort**: Import sorting

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📈 Future Features

- [ ] YAML output support
- [ ] Enhanced license detection algorithms
- [ ] Integration with package managers (npm, pip, etc.)
- [ ] Web interface for license management
- [ ] License compliance reporting
- [ ] Support for additional license types

## 🐛 Issues and Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-repo/issues) page
2. Create a new issue with detailed information
3. Include the output of `python main.py -v` for debugging

## 📊 Example Output

```bash
$ python main.py ./node_modules -v
Crawling directory: /path/to/project/node_modules
Full LICENSE path: /path/to/project/node_modules/@ampproject/remapping/LICENSE
Full LICENSE path: /path/to/project/node_modules/@babel/plugin-syntax-jsx/LICENSE
...
Total libraries found: 15
License detection completed successfully!
```

---

**Made with ❤️ for the open source community**
