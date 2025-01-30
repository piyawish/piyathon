# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
โมดูลเริ่มต้นแพ็คเกจ Piyathon

โมดูลนี้เริ่มต้นแพ็คเกจ Piyathon และตั้งค่าสภาพแวดล้อมการรัน
จัดการการนำเข้าโมดูลแบบไดนามิกจากไดเรกทอรี Lib และส่งออกข้อมูลเมตาดาต้าของแพ็คเกจ

ฟังก์ชันหลัก:
    - นำเข้าโมดูลทั้งหมดจากแพ็คเกจ Lib แบบไดนามิก
    - ส่งออกข้อมูลเวอร์ชันของแพ็คเกจ
    - จัดการการส่งออกระดับแพ็คเกจผ่าน __all__

Dependencies:
    - importlib: สำหรับการนำเข้าโมดูลแบบไดนามิก
    - pkgutil: สำหรับการค้นหาและวนซ้ำโมดูล

จุดเชื่อมต่อ:
    - เชื่อมต่อกับไดเรกทอรี Lib สำหรับโมดูลไลบรารีมาตรฐาน
    - ให้ข้อมูลเวอร์ชันแก่ CLI และส่วนประกอบอื่นๆ
    - ควบคุมการมองเห็นสัญลักษณ์ระดับแพ็คเกจ

ผลกระทบข้างเคียง:
    - แก้ไขเนมสเปซของโมดูลด้วยสัญลักษณ์ที่นำเข้า
    - เติม __all__ ด้วยสัญลักษณ์ในพื้นที่ทั้งหมด
"""

import importlib
import pkgutil

# Import all modules in the .Lib package dynamically
package_name = "Lib"

for _, module_name, _ in pkgutil.iter_modules([package_name]):
    importlib.import_module(f".{module_name}", package=package_name)

__all__ = list(locals())

__version__ = "0.3.12.11"
