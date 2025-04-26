# Universal Config Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Tired of manually converting configuration files between JSON, YAML, TOML, .env, and others?** This simple command-line tool aims to make your life easier by automating the conversion process.

`config-converter` allows you to effortlessly switch between common configuration formats, saving you time and reducing potential errors.

## Goals

*   Provide a **single, reliable CLI tool** for converting between the most popular configuration formats.
*   Ensure the conversion process is **accurate and preserves data structure**.
*   Maintain a **simple and intuitive user interface**.
*   Build a **community-driven tool** that adapts to new formats and user needs.

## Features & Roadmap

Here's what the tool can do and what's planned for the future:

*   [x] **Command-Line Interface (CLI):** Easy-to-use commands via `click`.
*   [x] **Core Conversion Logic:** Foundation for loading and saving data.
*   [x] **JSON Support:** Convert to/from JSON (`.json`).
*   [x] **YAML Support:** Convert to/from YAML (`.yaml`, `.yml`).
*   [x] **TOML Support:** Convert to/from TOML (`.toml`).
*   [x] **.env Support:** Convert to/from environment variable files (`.env`).
*   [x] **INI Support:** Convert to/from INI files (`.ini`).
*   [x] **XML Support:** Convert to/from XML files (`.xml`).
*   [ ] **Comment Preservation:** Attempt to keep comments intact during conversion (where applicable, e.g., YAML).
*   [ ] **Data Validation:** Option to validate input/output against a schema.
*   [x] **Basic Unit Tests:** Initial tests for core functionality.
*   [ ] **Comprehensive Test Suite:** More tests covering edge cases and all formats.
*   [ ] **Pre-commit Hooks:** Ensure code quality and consistency.
*   [x] **PyPI Packaging:** Make it easily installable via `pip install config-converter`.
*   [x] **GitHub Actions CI:** Automate testing on pushes and pull requests.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/config-converter.git # Replace with your repo URL later
    cd config-converter
    ```
2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate # On Windows use `.venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    # Also install pytest for running tests
    pip install pytest
    ```

## Usage

Convert a file from one format to another:

```bash
python -m config_converter.main --input-file <input_path> --source-format <format> --target-format <format> --output-file <output_path>
```

**Example:** Convert `config.json` to `config.yaml`:

```bash
python -m config_converter.main -i config.json -s json -t yaml -o config.yaml
```

Supported formats currently: `json`, `yaml`, `toml`, `env`, `ini`, `xml`.

## Contributing

Contributions are welcome! If you'd like to help improve `config-converter`, please feel free to:

*   Report bugs or suggest features by opening an issue.
*   Submit pull requests with bug fixes or new features (especially those on the roadmap!).
*   Improve the documentation.

Please check the `CONTRIBUTING.md` file (to be created) for more detailed guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file (to be created) for details.
