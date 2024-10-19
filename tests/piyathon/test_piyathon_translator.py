# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import pytest
from piyathon.piyathon_translator import PiyathonTranslator


@pytest.fixture
def translator():
    return PiyathonTranslator()


def test_keyword_translation(translator):
    piyathon_code = "ถ้า x > 0:\n    คืนค่า True"
    expected_python = "if x > 0:\n    return True"
    assert translator.piyathon_to_python(piyathon_code) == expected_python


def test_format_preservation(translator):
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
    original_piyathon = "สำหรับ i ใน ช่วง(5):\n    พิมพ์(i)"
    python = translator.piyathon_to_python(original_piyathon)
    translated_piyathon = translator.python_to_piyathon(python)
    assert original_piyathon == translated_piyathon


def test_function_name_in_thai(translator):
    piyathon_code = "นิยาม ภาษาไทย():\n    คืนค่า 'This is a function named in Thai'"
    expected_python = "def ภาษาไทย():\n    return 'This is a function named in Thai'"
    assert translator.piyathon_to_python(piyathon_code) == expected_python


@pytest.mark.skip(reason="Not implemented yet")
def test_syntax_error_detection(translator):
    piyathon_code_with_error = "ถ้า x > 0\n    พิมพ์(x)  # Missing colon"
    with pytest.raises(SyntaxError):
        translator.piyathon_to_python(piyathon_code_with_error)


def test_complex_code_translation(translator):
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


@pytest.mark.skip(reason="Not implemented yet")
def test_error_line_number(translator):
    piyathon_code_with_error = """
นิยาม test():
    x = 10
    y = 20
    ถ้า x > y  # Missing colon
        คืนค่า x
    อื่น:
        คืนค่า y
"""
    with pytest.raises(SyntaxError) as excinfo:
        translator.piyathon_to_python(piyathon_code_with_error)
    assert excinfo.value.lineno == 5  # The error should be on line 5


def test_nested_structures(translator):
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


def test_from_import_translation(translator):
    # piyathon_code = "จาก math นำเข้า sqrt"
    # python_code = "from math import sqrt"

    piyathon_code = "จาก math นำเข้า sqrt, sin, cos, tan, pi, floor, ceil, log, exp"
    python_code = "from math import sqrt, sin, cos, tan, pi, floor, ceil, log, exp"

    translated_python_code = translator.piyathon_to_python(piyathon_code)
    print()
    print(translated_python_code)
    assert translated_python_code == python_code

    translated_piyathon_code = translator.python_to_piyathon(python_code)
    print(translated_piyathon_code)
    assert translated_piyathon_code == piyathon_code
