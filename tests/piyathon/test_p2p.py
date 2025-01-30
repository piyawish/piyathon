# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
ชุดทดสอบสำหรับเครื่องมือแปลภาษาระหว่าง Piyathon และ Python

โมดูลนี้ประกอบด้วยชุดทดสอบสำหรับเครื่องมือคำสั่งที่ใช้แปลระหว่าง
ไฟล์ต้นฉบับ Piyathon (.pi) และ Python (.py) โดยตรวจสอบการจัดการไฟล์
เงื่อนไขข้อผิดพลาด และฟังก์ชันการแปลทั้งสองทิศทาง

ขอบเขตการทดสอบ:
    - การตรวจสอบอาร์กิวเมนต์ของคำสั่ง
    - การตรวจสอบนามสกุลไฟล์
    - การตรวจสอบการมีอยู่และความสามารถในการอ่านไฟล์
    - การจัดรูปแบบข้อความแสดงข้อผิดพลาด
    - ความสมบูรณ์ของการแปลทั้งสองทิศทาง
    - การดำเนินการกับไฟล์ I/O

การพึ่งพา:
    - pytest: สำหรับเฟรมเวิร์คและ fixtures การทดสอบ
    - unittest.mock: สำหรับการจำลองการเรียกระบบและการดำเนินการกับไฟล์
    - sys: สำหรับการจัดการอาร์กิวเมนต์ของคำสั่ง
    - tmp_path: สำหรับการสร้างและล้างไฟล์ชั่วคราว
"""

import sys
from unittest.mock import patch, mock_open
import pytest
from piyathon.p2p import main


def test_wrong_number_of_arguments(capsys):
    """
    ทดสอบพฤติกรรมเมื่อมีการระบุจำนวนอาร์กิวเมนต์ของคำสั่งไม่ถูกต้อง

    การทดสอบนี้ตรวจสอบว่าเครื่องมือจัดการกรณีที่ขาดอาร์กิวเมนต์อย่างถูกต้อง
    โดยตรวจสอบว่ามีการออกจากโปรแกรมด้วยรหัสข้อผิดพลาดและข้อความที่ถูกต้อง

    อาร์กิวเมนต์:
        capsys: pytest fixture สำหรับการจับ stdout/stderr

    การตรวจสอบ:
        - ออกจากโปรแกรมด้วย SystemExit รหัส 2
        - ข้อความแสดงข้อผิดพลาดระบุว่าขาดอาร์กิวเมนต์ที่จำเป็น
    """
    test_args = ["p2p.py"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 2
        captured = capsys.readouterr()
        assert "required" in captured.err


def test_same_extension(capsys):
    """
    ทดสอบพฤติกรรมเมื่อไฟล์ต้นฉบับและปลายทางมีนามสกุลเดียวกัน

    การทดสอบนี้ตรวจสอบว่าเครื่องมือตรวจสอบนามสกุลไฟล์อย่างถูกต้อง
    โดยต้องการให้ไฟล์ต้นฉบับและปลายทางมีนามสกุลที่แตกต่างกัน

    อาร์กิวเมนต์:
        capsys: pytest fixture สำหรับการจับ stdout/stderr

    การตรวจสอบ:
        - ออกจากโปรแกรมด้วย SystemExit รหัส 1
        - ข้อความแสดงข้อผิดพลาดระบุว่านามสกุลไฟล์ไม่ถูกต้อง
    """
    test_args = ["p2p.py", "source.py", "destination.py"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 1
        captured = capsys.readouterr()
        assert (
            "Error: Source and destination files must have different extensions (.py or .pi)"
            in captured.out
        )


def test_invalid_extension(capsys):
    """
    ทดสอบพฤติกรรมเมื่อไฟล์มีนามสกุลไม่ถูกต้อง

    การทดสอบนี้ตรวจสอบว่าเครื่องมือตรวจสอบนามสกุลไฟล์อย่างถูกต้อง
    โดยต้องการให้ทั้งสองไฟล์มีนามสกุล .py หรือ .pi เท่านั้น

    อาร์กิวเมนต์:
        capsys: pytest fixture สำหรับการจับ stdout/stderr

    การตรวจสอบ:
        - ออกจากโปรแกรมด้วย SystemExit รหัส 1
        - ข้อความแสดงข้อผิดพลาดระบุว่านามสกุลไฟล์ไม่ถูกต้อง
    """
    test_args = ["p2p.py", "source.txt", "destination.pi"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 1
        captured = capsys.readouterr()
        assert (
            "Error: Both files must have either .py or .pi extensions" in captured.out
        )


def test_file_not_found(capsys):
    """
    ทดสอบพฤติกรรมเมื่อไม่พบไฟล์ต้นฉบับ

    การทดสอบนี้ตรวจสอบว่าเครื่องมือจัดการกรณีที่ไม่พบไฟล์อินพุตอย่างถูกต้อง
    โดยแสดงข้อความแสดงข้อผิดพลาดและรหัสออกจากโปรแกรมที่เหมาะสม

    อาร์กิวเมนต์:
        capsys: pytest fixture สำหรับการจับ stdout/stderr

    การตรวจสอบ:
        - ออกจากโปรแกรมด้วย SystemExit รหัส 1
        - ข้อความแสดงข้อผิดพลาดระบุว่าไม่พบไฟล์
    """
    test_args = ["p2p.py", "nonexistent.pi", "destination.py"]
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

    การทดสอบนี้ตรวจสอบว่าเครื่องมือจัดการข้อผิดพลาด I/O เมื่ออ่านไฟล์ต้นฉบับอย่างถูกต้อง
    โดยแสดงข้อความแสดงข้อผิดพลาดและรหัสออกจากโปรแกรมที่เหมาะสม

    อาร์กิวเมนต์:
        capsys: pytest fixture สำหรับการจับ stdout/stderr

    การตรวจสอบ:
        - ออกจากโปรแกรมด้วย SystemExit รหัส 1
        - ข้อความแสดงข้อผิดพลาดระบุว่าไม่สามารถอ่านไฟล์ได้
    """
    test_args = ["p2p.py", "source.pi", "destination.py"]
    with patch.object(sys, "argv", test_args):
        with patch("builtins.open", mock_open()) as mocked_open:
            mocked_open.side_effect = IOError
            with pytest.raises(SystemExit) as e:
                main()
            assert e.type == SystemExit
            assert e.value.code == 1
            captured = capsys.readouterr()
            assert "Error: Unable to read input file 'source.pi'." in captured.out


def test_bidirectional_translation(tmp_path, capsys):
    """
    ทดสอบขั้นตอนการแปลทั้งสองทิศทางอย่างสมบูรณ์

    การทดสอบนี้ตรวจสอบวงจรการแปลทั้งหมด:
    1. การแปลจาก Python เป็น Piyathon
    2. การแปลจาก Piyathon เป็น Python
    3. การเปรียบเทียบโค้ด Python ต้นฉบับและสุดท้าย

    การทดสอบใช้ไฟล์ชั่วคราวเพื่อหลีกเลี่ยงผลกระทบต่อระบบไฟล์จริง
    และรับประกันการล้างที่เหมาะสม

    อาร์กิวเมนต์:
        tmp_path: pytest fixture สำหรับไดเรกทอรีชั่วคราว
        capsys: pytest fixture สำหรับการจับ stdout/stderr

    การตรวจสอบ:
        - การแปลสำเร็จในทั้งสองทิศทาง
        - การรักษาเนื้อหาผ่านวงจรการแปล
        - การสร้างและล้างไฟล์อย่างเหมาะสม
        - ข้อความแสดงความสำเร็จที่ถูกต้อง
    """
    # Create temporary files
    source_py = tmp_path / "p2p.py"
    intermediate_pi = tmp_path / "p2p.pi"
    final_py = tmp_path / "p2p_final.py"

    # Copy original p2p.py content to temp file
    with open("piyathon/p2p.py", "r", encoding="utf-8") as f:
        original_content = f.read()
    source_py.write_text(original_content, encoding="utf-8")

    # Python -> Piyathon
    test_args = ["p2p.py", str(source_py), str(intermediate_pi)]
    with patch.object(sys, "argv", test_args):
        main()
    captured = capsys.readouterr()
    assert "Python to Piyathon translation completed." in captured.out
    assert intermediate_pi.exists()

    # Piyathon -> Python
    test_args = ["p2p.py", str(intermediate_pi), str(final_py)]
    with patch.object(sys, "argv", test_args):
        main()
    captured = capsys.readouterr()
    assert "Piyathon to Python translation completed." in captured.out
    assert final_py.exists()

    # Compare original and final Python code
    final_content = final_py.read_text(encoding="utf-8")
    assert original_content == final_content

    # Verify files exist before cleanup
    assert source_py.exists()
    assert intermediate_pi.exists()
    assert final_py.exists()
