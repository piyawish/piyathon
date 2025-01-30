# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
อินเตอร์เฟซคำสั่งและสภาพแวดล้อมการรันของ Piyathon

โมดูลนี้เป็นจุดเริ่มต้นหลักของภาษาโปรแกรม Piyathon โดยให้ฟังก์ชันการทำงาน
ของอินเตอร์เฟซคำสั่งและสภาพแวดล้อมการรันสำหรับไฟล์ซอร์สโค้ด Piyathon (.pi)

ฟังก์ชันหลัก:
    - แยกวิเคราะห์อาร์กิวเมนต์คำสั่งสำหรับไฟล์ซอร์สโค้ด Piyathon
    - อ่านและตรวจสอบซอร์สโค้ด Piyathon
    - แปลงโค้ด Piyathon เป็น Python โดยใช้ PiyathonTranslator
    - ตั้งค่าสภาพแวดล้อมการรันพร้อมพาธไลบรารีที่กำหนดเอง
    - รันโค้ด Python ที่แปลงแล้วในเนมสเปซแยก

Dependencies:
    - sys: สำหรับการทำงานระดับระบบและการจัดการการออก
    - os: สำหรับการจัดการพาธและการทำงานกับไฟล์
    - argparse: สำหรับแยกวิเคราะห์อาร์กิวเมนต์คำสั่ง
    - piyathon_translator: สำหรับการแปลงโค้ดจาก Piyathon เป็น Python

จุดเชื่อมต่อ:
    - ทำงานร่วมกับ PiyathonTranslator สำหรับการแปลงโค้ด
    - เชื่อมต่อกับไลบรารีมาตรฐาน Piyathon ในไดเรกทอรี Lib
    - ทำงานกับคำสั่งสำหรับการรับไฟล์และการรันโค้ด

ข้อจำกัดที่ทราบ:
    - ประมวลผลเฉพาะไฟล์ .pi เดี่ยว (ยังไม่รองรับการนำเข้าโมดูล)
    - รันในเนมสเปซแยกที่มีขอบเขตโกลบอลจำกัด
    - การจัดการข้อผิดพลาดแบบพื้นฐานด้วยการจับข้อผิดพลาดทั่วไป
"""

import sys
import os
import argparse
from .piyathon_translator import PiyathonTranslator
from . import __version__


def parse_arguments():
    """
    แยกวิเคราะห์และตรวจสอบอาร์กิวเมนต์คำสั่งสำหรับการรัน Piyathon

    Returns:
        argparse.Namespace: อาร์กิวเมนต์คำสั่งที่แยกวิเคราะห์แล้วซึ่งประกอบด้วย:
            - source_file (str): พาธของไฟล์ซอร์สโค้ด Piyathon (.pi)
            - version (bool): แฟล็กสำหรับแสดงข้อมูลเวอร์ชัน
    """
    parser = argparse.ArgumentParser(
        description=f"Piyathon {__version__}\n"
        "Copyright (c) 2024, Piyawish Piyawat\n"
        "Licensed under the MIT License",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("source_file", help="Piyathon source file (.pi)")
    parser.add_argument(
        "-v", "--version", action="version", version=f"Piyathon {__version__}"
    )
    return parser.parse_args()


def main():
    """
    จุดเริ่มต้นหลักของตัวแปลภาษา Piyathon

    ฟังก์ชันนี้จัดการกระบวนการรัน Piyathon ทั้งหมด:
    1. แยกวิเคราะห์อาร์กิวเมนต์คำสั่ง
    2. ตรวจสอบนามสกุลไฟล์ซอร์สโค้ด
    3. อ่านและประมวลผลไฟล์ซอร์สโค้ด
    4. แปลงโค้ด Piyathon เป็น Python
    5. ตั้งค่าสภาพแวดล้อมการรัน
    6. รันโค้ดที่แปลงแล้ว

    ผลกระทบข้างเคียง:
        - แก้ไข sys.path เพื่อรวมไลบรารีมาตรฐาน Piyathon
        - สร้างและเติมเนมสเปซใหม่สำหรับการรัน
        - เขียนไปยัง stdout/stderr สำหรับการรายงานข้อผิดพลาด

    รหัสออก:
        - 0: การรันสำเร็จ
        - 1: สภาวะข้อผิดพลาดต่างๆ (ไม่พบไฟล์, นามสกุลไม่ถูกต้อง, ฯลฯ)
    """
    args = parse_arguments()
    source_file = args.source_file

    if not source_file.endswith(".pi"):
        print("Error: The source file must have a .pi extension")
        sys.exit(1)

    try:
        with open(source_file, "r", encoding="utf-8") as file:
            piyathon_code = file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{source_file}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Unable to read input file '{source_file}'.")
        sys.exit(1)

    translator = PiyathonTranslator()
    python_code = translator.piyathon_to_python(piyathon_code)

    if python_code is None:
        print("Execution aborted due to errors in the Piyathon input file.")
        sys.exit(1)

    # Get the absolute path to the current file's directory and append 'Lib'
    lib_path = os.path.join(os.path.dirname(__file__), "Lib")

    # Inject the absolute path into sys.path
    sys.path.insert(0, lib_path)

    # Create a new namespace for execution
    namespace = {"__name__": "__main__"}

    try:
        exec(python_code, namespace)  # pylint: disable=exec-used
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error during execution: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
