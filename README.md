# Universal Config Converter

[![PyPI version](https://badge.fury.io/py/universal-config-converter.svg)](https://badge.fury.io/py/universal-config-converter)
[![Python CI](https://github.com/velibenek/universal-config-converter/actions/workflows/python-ci.yml/badge.svg)](https://github.com/velibenek/universal-config-converter/actions/workflows/python-ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Tired of manually converting configuration files between different formats like JSON, YAML, TOML, .env, INI, and XML?** This simple command-line tool aims to automate the conversion process, making your life easier.

`universal-config-converter` allows you to effortlessly switch between common configuration formats, saving you time and reducing potential errors.

## Key Features

*   **Wide Format Support:** Convert between JSON, YAML, TOML, .env, INI, and XML.
*   **Command-Line Interface (CLI):** Easy and intuitive usage powered by `click`.
*   **Data Validation:** Option to validate input and output data against a JSON schema.
*   **Comment Preservation (Partial):** Attempts to preserve comments in YAML (using `ruamel.yaml`) and TOML (using `tomlkit`) formats (comments are generally lost in other formats).
*   **Flexibility:** Convert formats or simply validate files against a schema with a single command.

## Installation

### From PyPI (Recommended)

The easiest way to install is using `pip`:

```bash
pip install universal-config-converter
```

### Development Setup (For contributing or trying the latest changes)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/velibenek/universal-config-converter.git
    cd universal-config-converter
    ```
2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    python3 -m venv .venv
    # On Linux/macOS:
    source .venv/bin/activate
    # On Windows:
    # .venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -e .[dev]
    ```
    *(This installs the project in editable mode along with development dependencies like pytest.)*

## Usage

The basic command structure is:

```bash
config-converter -i <input_path> -s <source_format> -t <target_format> -o <output_path> [options]
```

**Arguments:**

*   `-i`, `--input-path`: Path to the input file.
*   `-s`, `--source-format`: Format of the input file (`json`, `yaml`, `toml`, `env`, `ini`, `xml`).
*   `-t`, `--target-format`: Desired output format (`json`, `yaml`, `toml`, `env`, `ini`, `xml`).
*   `-o`, `--output-path`: Path where the output file will be saved.

**Options:**

*   `--input-schema`: Path to a JSON schema file to validate the input against.
*   `--output-schema`: Path to a JSON schema file to validate the output against before saving.
*   `--help`: Show the help message and exit.

**Examples:**

1.  **Convert JSON to YAML:**
    ```bash
    config-converter -i config.json -s json -t yaml -o config.yaml
    ```

2.  **Convert YAML to TOML:**
    ```bash
    config-converter -i settings.yaml -s yaml -t toml -o settings.toml
    ```

3.  **Generate JSON from a .env File:**
    ```bash
    config-converter -i .env -s env -t json -o config.json
    ```

4.  **Convert INI to XML:**
    ```bash
    config-converter -i parameters.ini -s ini -t xml -o parameters.xml
    ```

5.  **Convert with Input Validation:** Validate `config.json` against `schema.json` before converting to YAML.
    ```bash
    config-converter -i config.json -s json -t yaml -o config.yaml --input-schema schema.json
    ```

6.  **Convert with Output Validation:** Convert JSON to YAML and validate the result against `schema.json` before saving.
    ```bash
    config-converter -i config.json -s json -t yaml -o config.yaml --output-schema schema.json
    ```

7.  **Validate Input Only:** Check if `config.toml` conforms to `schema.json` (no output file is written if `-o` is omitted).
    ```bash
    config-converter -i config.toml -s toml --input-schema schema.json
    ```

## Supported Formats

Currently supported formats: `json`, `yaml`, `toml`, `env`, `ini`, `xml`.

## Contributing

Contributions are welcome! If you'd like to help improve `universal-config-converter`, please feel free to:

*   Report bugs or suggest features by opening an [Issue](https://github.com/velibenek/universal-config-converter/issues).
*   Submit pull requests with bug fixes or new features.
*   Improve the documentation.

Please refer to the [`CONTRIBUTING.md`](CONTRIBUTING.md) file for more detailed guidelines.

## License

This project is licensed under the MIT License - see the [`LICENSE`](LICENSE) file for details.

## Links

*   [GitHub Repository](https://github.com/velibenek/universal-config-converter)
*   [PyPI Package](https://pypi.org/project/universal-config-converter/)
*   [Issue Tracker](https://github.com/velibenek/universal-config-converter/issues)
