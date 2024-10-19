# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import glob
import os
import pytest
from piyathon.piyathon_translator import PiyathonTranslator


def get_example_pairs():
    pi_files = glob.glob("examples/*.pi")
    example_pairs = []

    for pi_file in pi_files:
        base_name = os.path.splitext(pi_file)[0]
        py_file = f"{base_name}.py"
        if os.path.exists(py_file):
            example_pairs.append((pi_file, py_file))

    return example_pairs


@pytest.mark.parametrize("pi_file, py_file", get_example_pairs())
def test_translation_consistency(pi_file, py_file):
    # Read the original .pi file
    with open(pi_file, "r", encoding="utf-8") as file:
        original_pi_code = file.read()

    # Read the original .py file
    with open(py_file, "r", encoding="utf-8") as file:
        original_py_code = file.read()

    translator = PiyathonTranslator()

    # Translate .pi to .py
    translated_py_code = translator.piyathon_to_python(original_pi_code)

    # Translate the resulting .py back to .pi
    translated_pi_code = translator.python_to_piyathon(translated_py_code)

    # Assert that the final .pi code matches the original .pi code
    assert (
        original_pi_code == translated_pi_code
    ), f"The .pi code translation is not consistent for {pi_file}."

    # Translate .py to .pi
    translated_back_pi_code = translator.python_to_piyathon(original_py_code)

    # Translate the resulting .pi back to .py
    translated_back_py_code = translator.piyathon_to_python(translated_back_pi_code)

    # Assert that the final .py code matches the original .pycode
    assert (
        original_py_code == translated_back_py_code
    ), f"The Python code translation is not consistent for {py_file}."
