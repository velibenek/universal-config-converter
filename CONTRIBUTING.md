# Contributing to Universal Config Converter

Thank you for your interest in contributing to this project!

## Reporting Issues

If you find a bug or have a feature request, please check the existing [issues](https://github.com/velibenek/universal-config-converter/issues) first. If your issue is not listed, feel free to open a new one. Please provide as much detail as possible, including:

*   Steps to reproduce the bug.
*   Expected behavior.
*   Actual behavior.
*   Your operating system and Python version.
*   Any relevant configuration files or schemas (please remove sensitive data).

## Submitting Pull Requests

1.  **Fork the repository** and create a new branch for your feature or bug fix.
2.  **Install development dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up pre-commit hooks:**
    ```bash
    pre-commit install
    ```
4.  **Make your changes.** Please ensure your code passes the pre-commit checks before committing.
5.  **Add tests** for your changes in the `tests/` directory.
6.  **Ensure all tests pass:**
    ```bash
    pytest
    ```
7.  **Update the README.md** or other documentation if necessary.
8.  **Push your branch** to your fork.
9.  **Open a pull request** against the `main` branch of the original repository.

Please provide a clear description of your changes in the pull request.

## Code Style

This project uses `black` for code formatting and `flake8` for linting. Please ensure your contributions adhere to the style enforced by the pre-commit hooks.

Thank you again for your contribution!
