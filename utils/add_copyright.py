# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""สคริปต์สำหรับเพิ่มประกาศลิขสิทธิ์ในไฟล์ Python

สคริปต์ยูทิลิตี้นี้เพิ่มข้อมูลลิขสิทธิ์และใบอนุญาตในไฟล์ Python
ในไดเรกทอรีที่ระบุและไดเรกทอรีย่อยโดยอัตโนมัติ เพื่อให้มั่นใจว่าแต่ละไฟล์ Python
มีประกาศลิขสิทธิ์มาตรฐานถ้ายังไม่มี

Dependencies:
    - os: สำหรับการทำงานกับระบบไฟล์
    - sys: สำหรับอาร์กิวเมนต์คำสั่ง
"""

import os
import sys

COPYRIGHT_NOTE = """# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License
"""


def add_copyright_note_to_file(file_path):
    """เพิ่มประกาศลิขสิทธิ์ในไฟล์ Python ถ้ายังไม่มี

    Args:
        file_path (str): พาธของไฟล์ Python ที่ต้องการประมวลผล

    ผลกระทบข้างเคียง:
        - แก้ไขไฟล์เป้าหมายโดยเพิ่มประกาศลิขสิทธิ์ที่จุดเริ่มต้น
        - รักษาเนื้อหาไฟล์เดิมหลังประกาศลิขสิทธิ์

    Example:
        >>> add_copyright_note_to_file("example.py")
    """
    with open(file_path, "r+", encoding="utf-8") as file:
        content = file.read()
        if COPYRIGHT_NOTE not in content:
            file.seek(0, 0)
            file.write(COPYRIGHT_NOTE + "\n" + content)


def process_directory(directory):
    """ประมวลผลไฟล์ Python ทั้งหมดในไดเรกทอรีแบบเรียกซ้ำ

    เดินผ่านโครงสร้างไดเรกทอรีและเพิ่มประกาศลิขสิทธิ์ในไฟล์ Python ทั้งหมด
    ที่ยังไม่มีประกาศลิขสิทธิ์

    Args:
        directory (str): พาธของไดเรกทอรีรากที่จะเริ่มประมวลผล

    Side Effects:
        - Modifies Python files in the directory tree by adding copyright notices

    Example:
        >>> process_directory("./src")
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                add_copyright_note_to_file(file_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_copyright.py <directory>")
    else:
        directory = sys.argv[1]
        if os.path.isdir(directory):
            process_directory(directory)
        else:
            print(f"Error: {directory} is not a valid directory")
