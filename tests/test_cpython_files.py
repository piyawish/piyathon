# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import pytest
from piyathon.piyathon_translator import PiyathonTranslator


def read_cpython_file_list():
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

    # Translate .pi to .py
    translated_py_code = translator.piyathon_to_python(translated_pi_code)

    translated_py_code = PiyathonTranslator.clean_whitespaces(translated_py_code)

    test_logger.debug("Original Python code:\n%s", original_py_code)
    test_logger.debug("Translated Python code:\n%s", translated_py_code)

    # Assert that the translated .py code matches the original .py code
    assert (
        original_py_code == translated_py_code
    ), f"The Python code translation is not consistent for {py_file}."
