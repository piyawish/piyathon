# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
ชุดทดสอบสำหรับโมดูลแปลภาษา Piyathon

โมดูลนี้ประกอบด้วยชุดทดสอบสำหรับฟังก์ชันการแปลโค้ดระหว่าง Piyathon และ Python
เพื่อตรวจสอบความสามารถในการแปลภาษาทั้งสองทิศทาง การรักษารูปแบบโค้ด
และการจัดการโครงสร้างภาษาต่างๆ

ขอบเขตการทดสอบ:
    - การแปลคำสำคัญพื้นฐาน
    - การรักษารูปแบบโค้ดและคอมเมนต์
    - ความสอดคล้องในการแปลทั้งสองทิศทาง
    - การจัดการโครงสร้างโค้ดที่ซับซ้อน
    - ชื่อฟังก์ชันภาษาไทย
    - การแปลคำสั่ง import
    - โครงสร้างควบคุมการทำงาน (if-elif-else, for-in)

การพึ่งพา:
    - pytest: สำหรับเฟรมเวิร์คและ fixtures การทดสอบ
    - piyathon.piyathon_translator: สำหรับฟังก์ชันการแปลโค้ด
"""

import pytest
from piyathon.piyathon_translator import PiyathonTranslator


@pytest.fixture
def translator():
    """
    Pytest fixture ที่จัดเตรียม instance ของ PiyathonTranslator

    คืนค่า:
        PiyathonTranslator: instance ใหม่ของตัวแปลภาษาสำหรับแต่ละการทดสอบ
    """
    return PiyathonTranslator()


def test_keyword_translation(translator):
    """
    ทดสอบฟังก์ชันการแปลคำสำคัญพื้นฐาน

    ตรวจสอบว่าคำสั่งเงื่อนไขพื้นฐานถูกแปลระหว่าง Piyathon และ Python อย่างถูกต้อง

    อาร์กิวเมนต์:
        translator: fixture ของ PiyathonTranslator

    การตรวจสอบ:
        - โค้ด Piyathon ถูกแปลเป็นโค้ด Python ที่เทียบเท่ากันอย่างถูกต้อง
    """
    piyathon_code = "ถ้า x > 0:\n    คืนค่า True"
    expected_python = "if x > 0:\n    return True"
    assert translator.piyathon_to_python(piyathon_code) == expected_python


def test_format_preservation(translator):
    """
    ทดสอบการรักษารูปแบบโค้ดและคอมเมนต์

    ตรวจสอบว่าโครงสร้างโค้ด การเยื้อง และคอมเมนต์ถูกรักษาไว้
    ระหว่างการแปลภาษา

    อาร์กิวเมนต์:
        translator: fixture ของ PiyathonTranslator

    การตรวจสอบ:
        - รูปแบบโค้ดถูกรักษาไว้
        - คอมเมนต์ไม่เปลี่ยนแปลง
        - การเยื้องถูกรักษาไว้
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
    ทดสอบความสอดคล้องของการแปลทั้งสองทิศทาง

    ตรวจสอบว่าโค้ดที่ถูกแปลจาก Piyathon เป็น Python และกลับมา
    ตรงกับโค้ด Piyathon ต้นฉบับ

    อาร์กิวเมนต์:
        translator: fixture ของ PiyathonTranslator

    การตรวจสอบ:
        - การแปลไป-กลับรักษาโค้ดได้อย่างสมบูรณ์
    """
    original_piyathon = "สำหรับ i ใน ช่วง(5):\n    พิมพ์(i)"
    python = translator.piyathon_to_python(original_piyathon)
    translated_piyathon = translator.python_to_piyathon(python)
    assert original_piyathon == translated_piyathon


def test_function_name_in_thai(translator):
    """
    ทดสอบการจัดการชื่อฟังก์ชันภาษาไทย

    ตรวจสอบว่าชื่อฟังก์ชันที่เขียนเป็นภาษาไทยถูกรักษาไว้
    ระหว่างการแปลภาษา

    อาร์กิวเมนต์:
        translator: fixture ของ PiyathonTranslator

    การตรวจสอบ:
        - ชื่อฟังก์ชันภาษาไทยไม่เปลี่ยนแปลง
        - ไวยากรณ์การประกาศฟังก์ชันถูกแปลอย่างถูกต้อง
    """
    piyathon_code = "นิยาม ภาษาไทย():\n    คืนค่า 'This is a function named in Thai'"
    expected_python = "def ภาษาไทย():\n    return 'This is a function named in Thai'"
    assert translator.piyathon_to_python(piyathon_code) == expected_python


def test_complex_code_translation(translator):
    """
    ทดสอบการแปลโครงสร้างโค้ดที่ซับซ้อน

    ตรวจสอบว่าตัวแปลสามารถจัดการรูปแบบโค้ดที่ซับซ้อนได้
    เช่น ฟังก์ชันเรียกซ้ำและการจัดรูปแบบสตริง

    อาร์กิวเมนต์:
        translator: fixture ของ PiyathonTranslator

    การตรวจสอบ:
        - โครงสร้างโค้ดที่ซับซ้อนถูกแปลอย่างถูกต้อง
        - การจัดรูปแบบสตริงถูกรักษาไว้
        - การเรียกฟังก์ชันซ้ำถูกจัดการอย่างถูกต้อง
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
    ทดสอบการแปลโครงสร้างการควบคุมที่ซ้อนกัน

    ตรวจสอบว่าตัวแปลจัดการคำสั่ง if และลูปที่ซ้อนกัน
    พร้อมรักษาการเยื้องที่เหมาะสม

    อาร์กิวเมนต์:
        translator: fixture ของ PiyathonTranslator

    การตรวจสอบ:
        - โครงสร้างที่ซ้อนกันถูกแปลอย่างถูกต้อง
        - ระดับการเยื้องถูกรักษาไว้
        - ตรรกะการควบคุมการทำงานยังคงสมบูรณ์
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
    ทดสอบการแปลคำสั่ง import

    ตรวจสอบว่าคำสั่ง 'from ... import ...' ถูกแปล
    ระหว่างภาษาอย่างถูกต้อง

    อาร์กิวเมนต์:
        translator: fixture ของ PiyathonTranslator
        test_logger: fixture สำหรับการบันทึกข้อมูลดีบัก

    การตรวจสอบ:
        - คำสั่ง import ถูกแปลอย่างถูกต้องในทั้งสองทิศทาง
        - รายการที่นำเข้าหลายรายการถูกจัดการอย่างถูกต้อง
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
    ทดสอบการแปลโครงสร้าง if-elif-else

    ตรวจสอบว่าคำสั่งเงื่อนไขที่ซับซ้อนถูกแปล
    ระหว่างภาษาอย่างถูกต้อง

    อาร์กิวเมนต์:
        translator: fixture ของ PiyathonTranslator
        test_logger: fixture สำหรับการบันทึกข้อมูลดีบัก

    การตรวจสอบ:
        - โครงสร้าง If-elif-else ถูกแปลอย่างถูกต้อง
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
