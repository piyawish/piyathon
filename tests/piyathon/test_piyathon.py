# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
ชุดทดสอบสำหรับโมดูล CLI ของ Piyathon

โมดูลนี้ประกอบด้วยชุดทดสอบสำหรับฟังก์ชันการทำงานของ Command-line interface ของ Piyathon
ทดสอบเงื่อนไขข้อผิดพลาดต่างๆ และกรณีพิเศษสำหรับการจัดการไฟล์และการแยกวิเคราะห์อาร์กิวเมนต์

ขอบเขตการทดสอบ:
    - การตรวจสอบอาร์กิวเมนต์ของคำสั่ง
    - การตรวจสอบนามสกุลไฟล์
    - การตรวจสอบการมีอยู่และความสามารถในการอ่านไฟล์
    - การจัดรูปแบบและเนื้อหาของข้อความแสดงข้อผิดพลาด

การพึ่งพา:
    - pytest: สำหรับเฟรมเวิร์คและ fixtures การทดสอบ
    - unittest.mock: สำหรับการจำลองการเรียกระบบและการดำเนินการกับไฟล์
    - sys: สำหรับการจัดการอาร์กิวเมนต์ของคำสั่ง
"""

import sys
from unittest.mock import patch, mock_open
import pytest
from piyathon.piyathon import main


def test_no_arguments(capsys):
    """
    ทดสอบพฤติกรรมเมื่อไม่มีการระบุอาร์กิวเมนต์ในคำสั่ง

    การทดสอบนี้ตรวจสอบว่า CLI จัดการกรณีที่ไม่มีการระบุไฟล์ต้นฉบับอย่างถูกต้อง
    โดยตรวจสอบว่ามีการออกจากโปรแกรมด้วยรหัสข้อผิดพลาดและข้อความที่ถูกต้อง

    อาร์กิวเมนต์:
        capsys: pytest fixture สำหรับการจับ stdout/stderr

    การตรวจสอบ:
        - ออกจากโปรแกรมด้วย SystemExit รหัส 2
        - ข้อความแสดงข้อผิดพลาดระบุว่าขาดอาร์กิวเมนต์ที่จำเป็น
    """
    test_args = ["piyathon.py"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 2
        captured = capsys.readouterr()
        assert "required" in captured.err


def test_invalid_extension(capsys):
    """
    ทดสอบพฤติกรรมเมื่อมีการระบุไฟล์ที่มีนามสกุลไม่ถูกต้อง

    การทดสอบนี้ตรวจสอบว่า CLI ตรวจสอบนามสกุลไฟล์อย่างถูกต้อง
    โดยต้องการไฟล์นามสกุล .pi และปฏิเสธนามสกุลอื่น

    อาร์กิวเมนต์:
        capsys: pytest fixture สำหรับการจับ stdout/stderr

    การตรวจสอบ:
        - ออกจากโปรแกรมด้วย SystemExit รหัส 1
        - ข้อความแสดงข้อผิดพลาดระบุว่านามสกุลไฟล์ไม่ถูกต้อง
    """
    test_args = ["piyathon.py", "source.txt"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 1
        captured = capsys.readouterr()
        assert "Error: The source file must have a .pi extension" in captured.out


def test_file_not_found(capsys):
    """
    ทดสอบพฤติกรรมเมื่อไม่พบไฟล์ที่ระบุ

    การทดสอบนี้ตรวจสอบว่า CLI จัดการกรณีที่ไม่พบไฟล์อินพุตอย่างถูกต้อง
    โดยแสดงข้อความแสดงข้อผิดพลาดและรหัสออกจากโปรแกรมที่เหมาะสม

    อาร์กิวเมนต์:
        capsys: pytest fixture สำหรับการจับ stdout/stderr

    การตรวจสอบ:
        - ออกจากโปรแกรมด้วย SystemExit รหัส 1
        - ข้อความแสดงข้อผิดพลาดระบุว่าไม่พบไฟล์
    """
    test_args = ["piyathon.py", "nonexistent.pi"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 1
        captured = capsys.readouterr()
        assert "Error: Input file 'nonexistent.pi' not found." in captured.out


def test_file_read_error(capsys):
    """
    ทดสอบพฤติกรรมเมื่อไม่สามารถอ่านไฟล์ต้นฉบับได้

    การทดสอบนี้ตรวจสอบว่า CLI จัดการข้อผิดพลาด I/O เมื่ออ่านไฟล์ต้นฉบับอย่างถูกต้อง
    โดยแสดงข้อความแสดงข้อผิดพลาดและรหัสออกจากโปรแกรมที่เหมาะสม

    อาร์กิวเมนต์:
        capsys: pytest fixture สำหรับการจับ stdout/stderr

    การตรวจสอบ:
        - ออกจากโปรแกรมด้วย SystemExit รหัส 1
        - ข้อความแสดงข้อผิดพลาดระบุว่าไม่สามารถอ่านไฟล์ได้
    """
    test_args = ["piyathon.py", "source.pi"]
    with patch.object(sys, "argv", test_args):
        with patch("builtins.open", mock_open()) as mocked_open:
            mocked_open.side_effect = IOError
            with pytest.raises(SystemExit) as e:
                main()
            assert e.type == SystemExit
            assert e.value.code == 1
            captured = capsys.readouterr()
            assert "Error: Unable to read input file 'source.pi'." in captured.out
