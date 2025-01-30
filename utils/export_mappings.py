# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""สคริปต์ยูทิลิตี้สำหรับส่งออกการแมปคำสำคัญระหว่าง Piyathon และ Python

สคริปต์นี้ส่งออกการแมปสองทิศทางระหว่างคำสำคัญของ Piyathon และ Python
ไปยังไฟล์ JSON เพื่อใช้ในเอกสาร เครื่องมือ และการทำงานร่วมกับระบบอื่น

Dependencies:
    - json: สำหรับการทำงานกับไฟล์ JSON
    - sys: สำหรับการจัดการพาธ
    - pathlib: สำหรับการจัดการพาธที่ทำงานข้ามแพลตฟอร์ม
    - piyathon.keywords: แหล่งของพจนานุกรมแมปคำสำคัญ

ผลลัพธ์:
    สร้างไฟล์ 'python_mappings.json' ที่มีพจนานุกรมแมปสองตัว:
    - PI_TO_PY: แมปคำสำคัญ Piyathon ไปยังคำสำคัญ Python
    - PY_TO_PI: แมปคำสำคัญ Python ไปยังคำสำคัญ Piyathon
"""

import json
import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from piyathon.keywords import PI_TO_PY, PY_TO_PI


def export_mappings():
    """ส่งออกการแมปคำสำคัญไปยังไฟล์ JSON

    ส่งออกการแมปคำสำคัญทั้งจาก Piyathon ไป Python และจาก Python ไป Piyathon
    ไปยังไฟล์ JSON ชื่อ 'python_mappings.json' ในไดเรกทอรีปัจจุบัน

    ผลกระทบข้างเคียง:
        - สร้างหรือเขียนทับไฟล์ 'python_mappings.json' ในไดเรกทอรีปัจจุบัน
        - ไฟล์ถูกเขียนด้วยการเข้ารหัส UTF-8 เพื่อรองรับตัวอักษรภาษาไทย
    """
    mappings = {"PI_TO_PY": PI_TO_PY, "PY_TO_PI": PY_TO_PI}

    with open("python_mappings.json", "w", encoding="utf-8") as f:
        json.dump(mappings, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    export_mappings()
