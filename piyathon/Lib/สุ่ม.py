# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

# Generated module file. Do not edit directly.

"""
โมดูลสร้างตัวเลขสุ่มของ Piyathon (สุ่ม)

โมดูลนี้ให้การเชื่อมต่อภาษาไทยสำหรับโมดูลสุ่มของ Python
โดยมีเครื่องมือและยูทิลิตี้สำหรับการสร้างตัวเลขสุ่มครบถ้วน

ส่วนประกอบหลัก:
    - สุ่ม: คลาสตัวสร้างตัวเลขสุ่มหลัก (แมปไปยัง random.Random)
    - สุ่มระบบ: ตัวสร้างตัวเลขสุ่มของระบบ (แมปไปยัง random.SystemRandom)
    - ฟังก์ชันการแจกแจงต่างๆ (ปกติ, เบต้า, แกมมา, ฯลฯ)
    - ฟังก์ชันยูทิลิตี้สำหรับการสุ่มตัวอย่างและการสับเปลี่ยน
    - ค่าคงที่ทางคณิตศาสตร์ที่ใช้ในการแจกแจง

คุณสมบัติหลัก:
    - รองรับฟังก์ชันการทำงานของโมดูลสุ่มทั้งหมด
    - ชื่อฟังก์ชันและคลาสเป็นภาษาไทย
    - คงพฤติกรรมเดิมของโมดูลสุ่มของ Python ทั้งหมด
    - ตัวเลือกการสร้างตัวเลขสุ่มที่ปลอดภัยต่อการทำงานพร้อมกัน

จุดเชื่อมต่อ:
    - ใช้งานได้กับทุกกรณีการใช้งานของโมดูลสุ่มมาตรฐาน
    - สามารถใช้สลับกับโมดูลสุ่มต้นฉบับได้
    - รองรับการสร้างตัวเลขสุ่มทั้งแบบ Python ล้วนและแบบระบบ

ตัวอย่างการใช้งาน:
    >>> from piyathon.Lib.สุ่ม import สุ่มจำนวนเต็ม
    >>> สุ่มจำนวนเต็ม(1, 10)  # สุ่มจำนวนเต็มระหว่าง 1 ถึง 10
    >>> from piyathon.Lib.สุ่ม import สุ่ม
    >>> gen = สุ่ม()  # สร้างอินสแตนซ์ตัวสร้างตัวเลขสุ่ม
"""

import random
from abc import ABC


# Classes
class สุ่ม(random.Random):
    pass


class สุ่มระบบ(random.SystemRandom, ABC):
    pass


# Methods
เบต้าผันแปร = random.betavariate
ทวินามผันแปร = random.binomialvariate
เลือก = random.choice
ตัวเลือก = random.choices
เอ็กซ์โปเนนเชียลผันแปร = random.expovariate
แกมมาผันแปร = random.gammavariate
เกาส์ = random.gauss
รับสถานะ = random.getstate
ลอการิทึมปกติผันแปร = random.lognormvariate
ปกติผันแปร = random.normalvariate
พาเรโตผันแปร = random.paretovariate
สุ่มไบต์ = random.randbytes
สุ่มจำนวนเต็ม = random.randint
สุ่มช่วง = random.randrange
ตัวอย่าง = random.sample
เมล็ดพันธุ์ = random.seed
ตั้งสถานะ = random.setstate
สับเปลี่ยน = random.shuffle
สามเหลี่ยม = random.triangular
สม่ำเสมอ = random.uniform
ฟอนมีเซสผันแปร = random.vonmisesvariate
ไวบูลล์ผันแปร = random.weibullvariate

# Functions


# Constants
บีพีเอฟ = random.BPF
ลอจ4 = random.LOG4
เอ็นวีเมจิกคอนสท์ = random.NV_MAGICCONST
รีซิปบีพีเอฟ = random.RECIP_BPF
เอสจีเมจิกคอนสท์ = random.SG_MAGICCONST
สองพาย = random.TWOPI


# Get all public names from the module
eng_names = [name for name in dir(random) if not name.startswith("_")]

# Get all names defined in this file (our Thai translations)
thai_names = [name for name in locals() if not name.startswith("_")]

# Combine both sets of names, removing duplicates
__all__ = list(set(eng_names + thai_names))
