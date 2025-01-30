# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""ยูทิลิตี้สำหรับดึงและจัดรูปแบบแอตทริบิวต์ของแพ็คเกจ Python

สคริปต์นี้วิเคราะห์แพ็คเกจ Python เพื่อดึงแอตทริบิวต์สาธารณะ (คลาส,
เมธอด, ฟังก์ชัน, และค่าคงที่) และจัดรูปแบบให้เป็นโครงสร้างพจนานุกรม
ที่เหมาะสมสำหรับการแมปการแปลภาษา ผลลัพธ์จะถูกพิมพ์และคัดลอกไปยังคลิปบอร์ด

Dependencies:
    - sys: สำหรับอาร์กิวเมนต์คำสั่ง
    - inspect: สำหรับตรวจสอบออบเจกต์ Python
    - importlib: สำหรับการนำเข้าโมดูลแบบไดนามิก
    - pyperclip: สำหรับการทำงานกับคลิปบอร์ด

รูปแบบผลลัพธ์:
    สร้างพจนานุกรมที่มีโครงสร้างดังนี้:
    {
        "__name__": "",
        "classes": {class_name: "" สำหรับแต่ละคลาส},
        "methods": {method_name: "" สำหรับแต่ละเมธอด},
        "functions": {function_name: "" สำหรับแต่ละฟังก์ชัน},
        "constants": {constant_name: "" สำหรับแต่ละค่าคงที่}
    }

ประวัติเวอร์ชัน:
    - 1.0: การใช้งานเริ่มต้นพร้อมการดึงแอตทริบิวต์พื้นฐาน
"""

import sys
import inspect
import importlib
import pyperclip


def list_package_attributes(package_name):
    """ดึงและจัดรูปแบบแอตทริบิวต์จากแพ็คเกจ Python

    วิเคราะห์แพ็คเกจ Python เพื่อดึงแอตทริบิวต์สาธารณะและจัดรูปแบบ
    ให้เป็นโครงสร้างพจนานุกรมที่เหมาะสมสำหรับการแมปการแปลภาษา
    ผลลัพธ์จะถูกพิมพ์และคัดลอกไปยังคลิปบอร์ด

    Args:
        package_name (str): ชื่อของแพ็คเกจ Python ที่ต้องการวิเคราะห์

    ผลกระทบข้างเคียง:
        - พิมพ์พจนานุกรมที่จัดรูปแบบแล้วไปยัง stdout
        - คัดลอกพจนานุกรมที่จัดรูปแบบแล้วไปยังคลิปบอร์ดของระบบ
    """
    try:
        package = importlib.import_module(package_name)
    except ImportError:
        print(f"Error: Package '{package_name}' not found.")
        return

    attributes = dir(package)

    # Filter and sort classes
    classes = sorted(
        [attr for attr in attributes if inspect.isclass(getattr(package, attr))]
    )

    # Filter and sort methods
    methods = sorted(
        [attr for attr in attributes if inspect.ismethod(getattr(package, attr))]
    )

    # Filter and sort functions
    functions = sorted(
        [attr for attr in attributes if inspect.isfunction(getattr(package, attr))]
    )

    # Filter and sort constants (assuming constants are uppercase)
    constants = sorted([attr for attr in attributes if attr.isupper()])

    library_dict = {
        "__name__": "",
        "classes": {cls: "" for cls in classes},
        "methods": {mtd: "" for mtd in methods},
        "functions": {func: "" for func in functions},
        "constants": {const: "" for const in constants},
    }

    output = f"{package_name} = {library_dict}"
    print(output)
    pyperclip.copy(output)
    print("\nThe output has been copied to the clipboard.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python list_package_attributes.py <package_name>")
    else:
        package_name = sys.argv[1]
        list_package_attributes(package_name)
