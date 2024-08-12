# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

# Generated module file. Do not edit directly.

import random


# Classes
class สุ่ม(random.Random):
    pass


class สุ่มระบบ(random.SystemRandom):
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
