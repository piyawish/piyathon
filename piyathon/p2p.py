# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
เครื่องมือแปลงโค้ด Piyathon ผ่านคำสั่งในเทอร์มินัล

โมดูลนี้ให้อินเตอร์เฟซแบบคำสั่งในเทอร์มินัลสำหรับการแปลงโค้ดสองทิศทาง
ระหว่างไฟล์ซอร์สโค้ด Python (.py) และ Piyathon (.pi) ทำหน้าที่เป็นเครื่องมือแปลงโค้ด
แบบสแตนด์อโลนโดยไม่มีการรันโค้ด

ฟังก์ชันหลัก:
    - แปลงไฟล์ซอร์สโค้ด Python เป็นรูปแบบ Piyathon
    - แปลงไฟล์ซอร์สโค้ด Piyathon เป็นรูปแบบ Python
    - ตรวจสอบนามสกุลไฟล์และจัดการข้อผิดพลาด
    - รักษาโครงสร้างและการจัดรูปแบบโค้ดระหว่างการแปล

Dependencies:
    - sys: สำหรับการทำงานระดับระบบและการจัดการการออก
    - os: สำหรับการจัดการพาธและการทำงานกับไฟล์
    - argparse: สำหรับแยกวิเคราะห์อาร์กิวเมนต์คำสั่ง
    - piyathon_translator: สำหรับการแปลงโค้ดสองทิศทาง

จุดเชื่อมต่อ:
    - ทำงานร่วมกับ PiyathonTranslator สำหรับการแปลงโค้ด
    - เชื่อมต่อกับระบบไฟล์สำหรับการอ่าน/เขียนโค้ด
    - สามารถใช้เป็นส่วนหนึ่งของไปป์ไลน์การสร้าง/แปลโค้ด

ตัวอย่างการใช้งาน:
    # แปลง Python เป็น Piyathon
    $ python -m piyathon.p2p input.py output.pi

    # แปลง Piyathon เป็น Python
    $ python -m piyathon.p2p input.pi output.py

ข้อจำกัดที่ทราบ:
    - ประมวลผลทีละหนึ่งไฟล์
    - ไม่รองรับการแปลทั้งไดเรกทอรี
    - การจัดการข้อผิดพลาดแบบพื้นฐานสำหรับการทำงานกับไฟล์
"""

import sys
import os
import argparse
from .piyathon_translator import PiyathonTranslator


def parse_arguments():
    """
    แยกวิเคราะห์และตรวจสอบอาร์กิวเมนต์คำสั่งสำหรับการแปลงไฟล์

    Returns:
        argparse.Namespace: Parsed command-line arguments containing:
            - source_file (str): Path to the source file (.py or .pi)
            - destination_file (str): Path to the output file (.pi or .py)

    Example:
        >>> args = parse_arguments()
        >>> print(args.source_file, args.destination_file)
        'input.py' 'output.pi'
    """
    parser = argparse.ArgumentParser(
        description="Translate between Python and Piyathon files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("source_file", help="Source file (.py or .pi)")
    parser.add_argument("destination_file", help="Destination file (.py or .pi)")
    return parser.parse_args()


def validate_extensions(source_file, destination_file):
    """
    ตรวจสอบความถูกต้องของนามสกุลไฟล์ต้นทางและปลายทาง

    ตรวจสอบว่านามสกุลไฟล์ต้นทางและปลายทางถูกต้องตามที่กำหนด (.py หรือ .pi)
    และตรวจสอบว่าการแปลงระหว่างนามสกุลเป็นไปตามที่อนุญาต

    Args:
        source_file: พาธของไฟล์ต้นทาง
        destination_file: พาธของไฟล์ปลายทาง

    Returns:
        tuple: (นามสกุลไฟล์ต้นทาง, นามสกุลไฟล์ปลายทาง)

    Raises:
        ValueError: เมื่อนามสกุลไฟล์ไม่ถูกต้องหรือการแปลงไม่ได้รับอนุญาต
    """
    source_ext = os.path.splitext(source_file)[1]
    dest_ext = os.path.splitext(destination_file)[1]

    if source_ext == dest_ext:
        print(
            "Error: Source and destination files must have different extensions (.py or .pi)"
        )
        sys.exit(1)

    if source_ext not in [".py", ".pi"] or dest_ext not in [".py", ".pi"]:
        print("Error: Both files must have either .py or .pi extensions")
        sys.exit(1)


def read_source_file(source_file):
    """
    อ่านเนื้อหาจากไฟล์ต้นทาง

    Args:
        source_file: พาธของไฟล์ที่ต้องการอ่าน

    Returns:
        str: เนื้อหาของไฟล์ต้นทาง

    Raises:
        FileNotFoundError: เมื่อไม่พบไฟล์ต้นทาง
        IOError: เมื่อเกิดข้อผิดพลาดในการอ่านไฟล์
    """
    try:
        with open(source_file, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{source_file}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Unable to read input file '{source_file}'.")
        sys.exit(1)


def translate_code(source_code, source_ext, dest_ext):
    """
    แปลงโค้ดระหว่าง Python และ Piyathon

    Args:
        source_code: โค้ดต้นทางที่ต้องการแปล
        source_ext: นามสกุลไฟล์ต้นทาง
        dest_ext: นามสกุลไฟล์ปลายทาง

    Returns:
        tuple: (โค้ดที่แปลแล้ว, ประเภทการแปล)

    Raises:
        ValueError: เมื่อนามสกุลไฟล์ไม่ถูกต้องหรือการแปลงไม่ได้รับอนุญาต
    """
    translator = PiyathonTranslator()

    if source_ext == ".py" and dest_ext == ".pi":
        translated_code = translator.python_to_piyathon(source_code)
        translation_type = "Python to Piyathon"
    elif source_ext == ".pi" and dest_ext == ".py":
        translated_code = translator.piyathon_to_python(source_code)
        translation_type = "Piyathon to Python"
    else:
        print("Error: Invalid file extension combination")
        sys.exit(1)

    if translated_code is None:
        if source_ext == ".py":
            print("Translation aborted due to syntax errors in the Python input file.")
        else:
            print("Translation aborted due to errors in the Piyathon input file.")
        sys.exit(1)

    return translated_code, translation_type


def write_translated_code(destination_file, translated_code, translation_type):
    """
    เขียนโค้ดที่แปลแล้วลงในไฟล์ปลายทาง

    Args:
        destination_file: พาธของไฟล์ปลายทาง
        translated_code: โค้ดที่แปลแล้ว
        translation_type: ประเภทการแปล (py2pi หรือ pi2py)

    Raises:
        IOError: เมื่อเกิดข้อผิดพลาดในการเขียนไฟล์
    """
    try:
        with open(destination_file, "w", encoding="utf-8") as file:
            file.write(translated_code)
        print(f"{translation_type} translation completed.")
        print(f"Translated code has been written to '{destination_file}'.")
    except IOError:
        print(f"Error: Unable to write to output file '{destination_file}'.")
        sys.exit(1)


def main():
    """
    Main entry point for the translation tool.

    This function orchestrates the entire translation process:
    1. Parses command-line arguments
    2. Validates file extensions
    3. Reads the source file
    4. Performs the translation
    5. Writes the result to the destination file

    Side Effects:
        - File system operations (read/write)
        - Stdout/stderr output for status and errors
        - Process exit codes for success/failure

    Example:
        $ python -m piyathon.p2p input.py output.pi
    """
    args = parse_arguments()
    validate_extensions(args.source_file, args.destination_file)
    source_code = read_source_file(args.source_file)
    source_ext = os.path.splitext(args.source_file)[1]
    dest_ext = os.path.splitext(args.destination_file)[1]
    translated_code, translation_type = translate_code(
        source_code, source_ext, dest_ext
    )
    write_translated_code(args.destination_file, translated_code, translation_type)


if __name__ == "__main__":
    main()
