# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
การทดสอบการทำงานร่วมกันของการแปลภาษา Piyathon โดยใช้ไฟล์จากไลบรารีมาตรฐานของ CPython

โมดูลนี้ทดสอบความสามารถในการแปลภาษาสองทิศทางของตัวแปลภาษา Piyathon
โดยใช้ไฟล์ Python จริงจากไลบรารีมาตรฐานของ CPython เพื่อให้มั่นใจว่า
โค้ด Python สามารถแปลงเป็น Piyathon และกลับมาได้โดยยังคงรักษา
ฟังก์ชันการทำงานและโครงสร้างเดิมไว้

ส่วนประกอบหลัก:
    - การจัดการรายการไฟล์สำหรับไฟล์ทดสอบ CPython
    - การตรวจสอบความสอดคล้องของการแปล
    - การจัดการการเข้ารหัส UTF-8
    - การสร้างไฟล์ทดสอบอัตโนมัติ

Dependencies:
    - pytest: สำหรับการพาราเมเตอร์ไรซ์และการรันการทดสอบ
    - PiyathonTranslator: ฟังก์ชันหลักในการแปลภาษา
    - pathlib: สำหรับการจัดการพาธที่ทำงานข้ามแพลตฟอร์ม

จุดเชื่อมต่อ:
    - อ่านจาก cpython_file_list.txt สำหรับเคสทดสอบ
    - ส่งออกไฟล์ที่แปลแล้วไปยังไดเรกทอรี tests/translated/
    - ใช้ test_logger fixture ที่แชร์จาก conftest.py
"""


from pathlib import Path
import pytest
from piyathon.piyathon_translator import PiyathonTranslator


def read_cpython_file_list():
    """
    อ่านรายการไฟล์ CPython ที่จะทดสอบจาก cpython_file_list.txt

    ไฟล์ควรมีพาธของไฟล์ Python หนึ่งบรรทัดต่อหนึ่งไฟล์
    โดยเป็นพาธที่สัมพันธ์กับไดเรกทอรีรากของโปรเจค

    Returns:
        list[str]: รายการพาธของไฟล์ที่จะทดสอบ รายการว่างถ้าไม่พบไฟล์
                  หรือไม่สามารถอ่านไฟล์ได้

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
