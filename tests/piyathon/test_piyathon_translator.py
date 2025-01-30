# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
Unit Tests for Piyathon Translator Module

This module contains unit tests for the Piyathon-Python code translation functionality.
It verifies the bidirectional translation capabilities, code formatting preservation,
and handling of various language constructs.

Test Coverage:
    - Basic keyword translation
    - Code formatting and comment preservation
    - Bidirectional translation consistency
    - Complex code structure handling
    - Thai language function names
    - Import statement translation
    - Control flow constructs (if-elif-else, for-in)

Dependencies:
    - pytest: For test framework and fixtures
    - piyathon.piyathon_translator: For code translation functionality
"""

import pytest
from piyathon.piyathon_translator import PiyathonTranslator


@pytest.fixture
def translator():
    """
    Pytest fixture that provides a PiyathonTranslator instance.

    Returns:
        PiyathonTranslator: A fresh instance of the translator for each test
    """
    return PiyathonTranslator()


def test_keyword_translation(translator):
    """
    Test basic keyword translation functionality.

    Verifies that simple conditional statements are correctly translated
    between Piyathon and Python.

    Args:
        translator: PiyathonTranslator fixture

    Assertions:
        - Piyathon code is correctly translated to equivalent Python code
    """
    piyathon_code = "ถ้า x > 0:\n    คืนค่า True"
    expected_python = "if x > 0:\n    return True"
    assert translator.piyathon_to_python(piyathon_code) == expected_python


def test_format_preservation(translator):
    """
    Test preservation of code formatting and comments.

    Verifies that code structure, indentation, and comments are maintained
    during translation between languages.

    Args:
        translator: PiyathonTranslator fixture

    Assertions:
        - Code formatting is preserved
        - Comments remain unchanged
        - Indentation is maintained
    """
    piyathon_code = """
# นี่คือคอมเมนต์
จาก math นำเข้า sqrt

นิยาม test_func():
    x = 10  # นี่คือตัวแปร x

    ถ้า x > 5:
        คืนค่า True
    อื่น:
        คืนค่า False
"""
    python_code = translator.piyathon_to_python(piyathon_code)
    expected_python = """
# นี่คือคอมเมนต์
from math import sqrt

def test_func():
    x = 10  # นี่คือตัวแปร x

    if x > 5:
        return True
    else:
        return False
"""
    assert python_code == expected_python


def test_bidirectional_translation(translator):
    """
    Test consistency of bidirectional translation.

    Verifies that code translated from Piyathon to Python and back
    matches the original Piyathon code.

    Args:
        translator: PiyathonTranslator fixture

    Assertions:
        - Round-trip translation preserves code exactly
    """
    original_piyathon = "สำหรับ i ใน ช่วง(5):\n    พิมพ์(i)"
    python = translator.piyathon_to_python(original_piyathon)
    translated_piyathon = translator.python_to_piyathon(python)
    assert original_piyathon == translated_piyathon


def test_function_name_in_thai(translator):
    """
    Test handling of Thai language function names.

    Verifies that function names written in Thai are preserved
    during translation between languages.

    Args:
        translator: PiyathonTranslator fixture

    Assertions:
        - Thai function names remain unchanged
        - Function definition syntax is correctly translated
    """
    piyathon_code = "นิยาม ภาษาไทย():\n    คืนค่า 'This is a function named in Thai'"
    expected_python = "def ภาษาไทย():\n    return 'This is a function named in Thai'"
    assert translator.piyathon_to_python(piyathon_code) == expected_python


def test_complex_code_translation(translator):
    """
    Test translation of complex code structures.

    Verifies that the translator can handle more complex code patterns
    like recursive functions and string formatting.

    Args:
        translator: PiyathonTranslator fixture

    Assertions:
        - Complex code structures are correctly translated
        - String formatting is preserved
        - Recursive function calls are handled correctly
    """
    piyathon_code = """
นิยาม fibonacci(n):
    ถ้า n <= 1:
        คืนค่า n
    อื่น:
        คืนค่า fibonacci(n-1) + fibonacci(n-2)

สำหรับ i ใน ช่วง(10):
    พิมพ์(f"fibonacci({i}) = {fibonacci(i)}")
"""
    expected_python = (
        piyathon_code.replace("นิยาม", "def")
        .replace("ถ้า", "if")
        .replace("คืนค่า", "return")
        .replace("อื่น", "else")
        .replace("สำหรับ", "for")
        .replace("ใน", "in")
        .replace("ช่วง", "range")
        .replace("พิมพ์", "print")
    )
    assert translator.piyathon_to_python(piyathon_code) == expected_python


def test_nested_structures(translator):
    """
    Test translation of nested control structures.

    Verifies that the translator correctly handles nested if statements
    and loops while maintaining proper indentation.

    Args:
        translator: PiyathonTranslator fixture

    Assertions:
        - Nested structures are correctly translated
        - Indentation levels are preserved
        - Control flow logic remains intact
    """
    piyathon_code = """
นิยาม nested_func(x):
    ถ้า x > 0:
        สำหรับ i ใน ช่วง(x):
            ถ้า i % 2 == 0:
                คืนค่า i
    คืนค่า None
"""
    expected_python = """
def nested_func(x):
    if x > 0:
        for i in range(x):
            if i % 2 == 0:
                return i
    return None
"""
    assert translator.piyathon_to_python(piyathon_code) == expected_python


def test_from_import_translation(translator, test_logger):
    """
    Test translation of import statements.

    Verifies that 'from ... import ...' statements are correctly
    translated between languages.

    Args:
        translator: PiyathonTranslator fixture
        test_logger: Logger fixture for debugging output

    Assertions:
        - Import statements are correctly translated in both directions
        - Multiple imported items are handled correctly
    """
    piyathon_code = "จาก math นำเข้า sqrt, sin, cos, tan"
    python_code = "from math import sqrt, sin, cos, tan"

    translated_python_code = translator.piyathon_to_python(piyathon_code)
    test_logger.debug(translated_python_code)
    assert translated_python_code == python_code

    translated_piyathon_code = translator.python_to_piyathon(python_code)
    test_logger.debug(translated_piyathon_code)
    assert translated_piyathon_code == piyathon_code


def test_if_elif_else_translation(translator, test_logger):
    """
    Test translation of if-elif-else constructs.

    Verifies that complex conditional statements are correctly
    translated between languages.

    Args:
        translator: PiyathonTranslator fixture
        test_logger: Logger fixture for debugging output

    Assertions:
        - If-elif-else structures are correctly translated
        - Conditional expressions are preserved
        - Bidirectional translation is consistent
    """
    piyathon_code = """
ถ้า x < 0:
    พิมพ์("ลบ")
อื่นถ้า x == 0:
    พิมพ์("ศูนย์")
อื่น:
    พิมพ์("บวก")
"""
    python_code = """
if x < 0:
    print("ลบ")
elif x == 0:
    print("ศูนย์")
else:
    print("บวก")
"""

    translated_python_code = translator.piyathon_to_python(piyathon_code)
    test_logger.debug(translated_python_code)
    assert translated_python_code == python_code
    translated_piyathon_code = translator.python_to_piyathon(translated_python_code)
    test_logger.debug(translated_piyathon_code)
    assert translated_piyathon_code == piyathon_code

    translated_piyathon_code = translator.python_to_piyathon(python_code)
    test_logger.debug(translated_piyathon_code)
    assert translated_piyathon_code == piyathon_code
    translated_python_code = translator.piyathon_to_python(translated_piyathon_code)
    test_logger.debug(translated_python_code)
    assert translated_python_code == python_code


def test_for_in_translation(translator, test_logger):
    """
    Test translation of for-in loop constructs.

    Verifies that for loops and list comprehensions are correctly
    translated between languages.

    Args:
        translator: PiyathonTranslator fixture
        test_logger: Logger fixture for debugging output

    Assertions:
        - For-in loops are correctly translated
        - List literals are preserved
        - String formatting in loops is handled correctly
    """
    piyathon_code = """
สำหรับ ตัว ใน [1, 2, 3, 4, 5]:
    พิมพ์(f"ค่าปัจจุบัน: {ตัว}")
"""
    python_code = """
for ตัว in [1, 2, 3, 4, 5]:
    print(f"ค่าปัจจุบัน: {ตัว}")
"""

    # Test Piyathon to Python translation
    translated_python = translator.piyathon_to_python(piyathon_code)
    assert translated_python == python_code

    # Test Python to Piyathon translation
    translated_piyathon = translator.python_to_piyathon(python_code)
    assert translated_piyathon == piyathon_code

    # Log the translations for debugging
    test_logger.debug("Piyathon to Python:\n%s", translated_python)
    test_logger.debug("Python to Piyathon:\n%s", translated_piyathon)
