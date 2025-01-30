# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
การกำหนดค่าการทดสอบและ fixtures ที่ใช้ร่วมกันสำหรับชุดทดสอบ Piyathon

โมดูลนี้จัดเตรียมฟังก์ชันการบันทึกข้อมูลและ fixtures ที่สามารถใช้ร่วมกัน
ในไฟล์ทดสอบทั้งหมดของโครงการ โดยตั้งค่าการกำหนดค่าการบันทึกข้อมูลมาตรฐาน
ที่สามารถนำกลับมาใช้ในโมดูลทดสอบต่างๆ

ส่วนประกอบหลัก:
    - การตั้งค่าการบันทึกข้อมูลที่สามารถปรับระดับได้
    - pytest fixture ที่มีขอบเขตระดับเซสชันสำหรับการเข้าถึงตัวบันทึกข้อมูล
"""

import logging
import pytest


def setup_logger(level=logging.INFO):
    """
    กำหนดค่าและคืนค่าตัวบันทึกข้อมูลด้วยระดับการบันทึกที่ระบุ

    อาร์กิวเมนต์:
        level (int): ระดับการบันทึกข้อมูลที่จะใช้ (ค่าเริ่มต้น: logging.INFO)
                    สามารถเป็น logging.DEBUG, logging.INFO, logging.WARNING, ฯลฯ

    คืนค่า:
        logging.Logger: อินสแตนซ์ของตัวบันทึกข้อมูลที่กำหนดค่าแล้ว พร้อมตัวจัดการ
                       การแสดงผลทางคอนโซลและการจัดรูปแบบเอาต์พุต

    ตัวอย่าง:
        >>> logger = setup_logger(logging.DEBUG)
        >>> logger.debug("Debug message")
        2024-01-26 12:34:56,789 - __main__ - DEBUG - Debug message
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    # Create console handler and set level to the specified level
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Add formatter to ch
    ch.setFormatter(formatter)

    # Add ch to logger
    logger.addHandler(ch)

    return logger


# Create a logger instance with INFO level by default
logger = setup_logger()


@pytest.fixture(scope="session")
def test_logger():
    """
    Pytest fixture ที่จัดเตรียมอินสแตนซ์ของตัวบันทึกข้อมูลที่กำหนดค่าแล้วสำหรับเซสชันการทดสอบทั้งหมด

    fixture นี้มีขอบเขตระดับเซสชัน หมายความว่าอินสแตนซ์ของตัวบันทึกข้อมูลเดียวกัน
    จะถูกใช้ร่วมกันในการทดสอบทั้งหมดในเซสชัน ซึ่งป้องกันการสร้างตัวจัดการบันทึกข้อมูลซ้ำ
    และรับประกันพฤติกรรมการบันทึกข้อมูลที่สอดคล้องกัน

    คืนค่า:
        logging.Logger: อินสแตนซ์ของตัวบันทึกข้อมูลที่กำหนดค่าโดย setup_logger()

    ตัวอย่าง:
        def test_something(test_logger):
            test_logger.info("เริ่มการทดสอบ...")
    """
    return logger
