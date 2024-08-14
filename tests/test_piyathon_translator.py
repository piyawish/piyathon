# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import pytest
from piyathon.piyathon_translator import PiyathonTranslator


@pytest.fixture
def translator():
    return PiyathonTranslator()


def test_check_syntax_valid_code(translator):
    valid_code = "print('Hello, world!')"
    assert translator.check_syntax(valid_code) is True


def test_check_syntax_invalid_code(translator):
    invalid_code = "print('Hello, world!'"
    assert translator.check_syntax(invalid_code) is False


def test_transform_to_thai_valid_code(translator):
    python_code = "print('Hello, world!')"
    piyathon_code = "พิมพ์('Hello, world!')"
    assert translator.transform_to_thai(python_code) == piyathon_code


def test_transform_to_thai_invalid_code(translator):
    invalid_code = "print('Hello, world!'"
    assert translator.transform_to_thai(invalid_code) is None


def test_transform_to_thai_keywords(translator):
    python_code = "for i in range(10): print(i)"
    piyathon_code = "สำหรับ i ใน ช่วง(10): พิมพ์(i)"
    assert translator.transform_to_thai(python_code) == piyathon_code


def test_transform_to_thai_handle_from_import(translator):
    python_code = "from math import sqrt"
    piyathon_code = "จาก math นำเข้า sqrt"
    assert translator.transform_to_thai(python_code) == piyathon_code


def test_transform_to_thai_handle_else_elif(translator):
    python_code = """
if x > 0:
    print('positive')
elif x < 0:
    print('negative')
else: print('zero')
"""
    piyathon_code = """
ถ้า x > 0:
    พิมพ์('positive')
หรือถ้า x < 0:
    พิมพ์('negative')
อื่น: พิมพ์('zero')
"""
    assert translator.transform_to_thai(python_code) == piyathon_code


def test_transform_to_thai_handle_for_in(translator):
    python_code = "for i in range(10): print(i)"
    piyathon_code = "สำหรับ i ใน ช่วง(10): พิมพ์(i)"
    assert translator.transform_to_thai(python_code) == piyathon_code
