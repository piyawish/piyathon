# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import logging
import pytest
from piyathon.piyathon_translator import PiyathonTranslator

# Set up logging
logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def setup_logging(caplog):
    caplog.set_level(logging.DEBUG)


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
    piyathon_code = "จาก math นำเข้า sqrt, sin, cos, tan"
    python_code = "from math import sqrt, sin, cos, tan"

    translated_python_code = translator.piyathon_to_python(piyathon_code)
    logger.debug(translated_python_code)
    assert translated_python_code == python_code

    translated_piyathon_code = translator.python_to_piyathon(python_code)
    logger.debug(translated_piyathon_code)
    assert translated_piyathon_code == piyathon_code


def test_if_elif_else_translation(translator):
    piyathon_code = """
ถ้า x < 0:
    พิมพ์("ลบ")
หรือถ้า x == 0:
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
    logger.debug(translated_python_code)
    assert translated_python_code == python_code
    translated_piyathon_code = translator.python_to_piyathon(translated_python_code)
    logger.debug(translated_piyathon_code)
    assert translated_piyathon_code == piyathon_code

    translated_piyathon_code = translator.python_to_piyathon(python_code)
    logger.debug(translated_piyathon_code)
    assert translated_piyathon_code == piyathon_code
    translated_python_code = translator.piyathon_to_python(translated_piyathon_code)
    logger.debug(translated_python_code)
    assert translated_python_code == python_code


def test_for_in_translation(translator):
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
    logger.debug("Piyathon to Python:\n%s", translated_python)
    logger.debug("Python to Piyathon:\n%s", translated_piyathon)
