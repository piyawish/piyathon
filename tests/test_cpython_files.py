# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
Integration tests for Piyathon translation using CPython standard library files.

This module tests the bidirectional translation capabilities of the Piyathon
translator using actual Python files from the CPython standard library. It ensures
that Python code can be translated to Piyathon and back while preserving the
original functionality and structure.

Key Components:
    - File list management for CPython test files
    - Translation consistency verification
    - UTF-8 encoding handling
    - Automated test file generation

Dependencies:
    - pytest: For test parameterization and execution
    - PiyathonTranslator: Core translation functionality
    - pathlib: For cross-platform path handling

Integration Points:
    - Reads from cpython_file_list.txt for test cases
    - Outputs translated files to tests/translated/ directory
    - Uses shared test_logger fixture from conftest.py
"""


from pathlib import Path
import pytest
from piyathon.piyathon_translator import PiyathonTranslator


def read_cpython_file_list():
    """
    Read the list of CPython files to be tested from cpython_file_list.txt.

    The file should contain one Python file path per line, relative to the
    project root directory.

    Returns:
        list[str]: List of file paths to test. Empty list if file is not found
                  or cannot be read.

    Side Effects:
        - Prints error messages to stdout if file cannot be accessed
        - Uses UTF-8 encoding for file reading

    Example:
        >>> files = read_cpython_file_list()
        >>> print(files)
        ['../cpython/Lib/abc.py', '../cpython/Lib/aifc.py', ...]
    """
    file_path = "tests/cpython_file_list.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []
    except IOError:
        print(f"Error: Unable to read {file_path}.")
        return []


@pytest.mark.parametrize("py_file", read_cpython_file_list())
def test_translation_consistency(py_file, test_logger):
    """
    Test bidirectional translation consistency for a given Python file.

    This test ensures that translating a Python file to Piyathon and back
    produces the exact same Python code, verifying the translator's accuracy
    and reversibility.

    Args:
        py_file (str): Path to the Python file to test
        test_logger: Logger fixture from conftest.py

    Test Flow:
        1. Read and clean original Python code
        2. Translate Python → Piyathon
        3. Save Piyathon translation
        4. Translate Piyathon → Python
        5. Compare final Python with original

    Side Effects:
        - Creates directory structure under tests/translated/
        - Writes .pi files to the translated directory
        - Logs debug information about translations
        - Skips files with UTF-8 decoding errors

    Known Limitations:
        - Assumes UTF-8 encoding for all files
        - Whitespace differences may affect comparison
        - May skip files with encoding issues
    """
    # Read the original .py file
    try:
        with open(py_file, "r", encoding="utf-8") as file:
            original_py_code = file.read()
    except UnicodeDecodeError:
        test_logger.error(f"Error: Unable to decode {py_file} using UTF-8 encoding.")
        return  # Skip this file and continue with the next one

    original_py_code = PiyathonTranslator.clean_whitespaces(original_py_code)

    translator = PiyathonTranslator()

    # Translate .py to .pi
    translated_pi_code = translator.python_to_piyathon(original_py_code)

    # Create the target directory structure
    translated_dir = Path("tests") / "translated"
    # Remove "../" from the path and get just the cpython part onwards
    clean_path = Path(py_file.replace("../", ""))
    target_pi_file = translated_dir / clean_path.with_suffix(".pi")
    target_pi_file.parent.mkdir(parents=True, exist_ok=True)

    # Save the translated Piyathon code
    target_pi_file.write_text(translated_pi_code, encoding="utf-8")

    # Translate .pi to .py
    translated_py_code = translator.piyathon_to_python(translated_pi_code)

    translated_py_code = PiyathonTranslator.clean_whitespaces(translated_py_code)

    test_logger.debug("Original Python code:\n%s", original_py_code)
    test_logger.debug("Translated Python code:\n%s", translated_py_code)

    # Assert that the translated .py code matches the original .py code
    assert (
        original_py_code == translated_py_code
    ), f"The Python code translation is not consistent for {py_file}."
