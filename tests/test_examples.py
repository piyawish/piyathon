# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
Test suite for verifying Piyathon translation using example files.

This module tests the bidirectional translation capabilities of the Piyathon
translator using paired example files (.py and .pi) from the examples directory.
It ensures that translations are consistent in both directions and that the
semantic meaning of the code is preserved.

Key Components:
    - Example file pair discovery
    - Bidirectional translation verification
    - Round-trip translation testing

Dependencies:
    - pytest: For test parameterization
    - glob: For file pattern matching
    - PiyathonTranslator: Core translation functionality

Data Structures:
    - Example pairs: Tuples of (pi_file, py_file) paths representing
      corresponding Piyathon and Python implementations

Integration Points:
    - Reads from examples/*.pi and examples/*.py
    - Verifies consistency between paired implementations
"""

import glob
import os
import pytest
from piyathon.piyathon_translator import PiyathonTranslator


def get_example_pairs():
    """
    Discover and pair corresponding .pi and .py files from the examples directory.

    Searches for .pi files and attempts to find matching .py files with the same
    base name. Only pairs where both files exist are included in the results.

    Returns:
        list[tuple[str, str]]: List of tuples containing paths to matching
                              (.pi, .py) file pairs.

    Example:
        >>> pairs = get_example_pairs()
        >>> print(pairs)
        [('examples/hello.pi', 'examples/hello.py'),
         ('examples/math.pi', 'examples/math.py')]
    """
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
    """
    Test bidirectional translation consistency between paired example files.

    This test verifies that:
    1. A .pi file can be translated to Python and back to identical Piyathon
    2. A .py file can be translated to Piyathon and back to identical Python

    Args:
        pi_file (str): Path to the Piyathon (.pi) example file
        py_file (str): Path to the corresponding Python (.py) file

    Test Flow:
        1. Test Piyathon → Python → Piyathon translation:
           - Read original .pi file
           - Translate to Python
           - Translate back to Piyathon
           - Compare with original
        2. Test Python → Piyathon → Python translation:
           - Read original .py file
           - Translate to Piyathon
           - Translate back to Python
           - Compare with original

    Known Limitations:
        - Assumes UTF-8 encoding for all files
        - Whitespace sensitivity in comparisons
        - Requires exact matches (no semantic equivalence)
    """
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
