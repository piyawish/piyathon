import random


# Classes
class สุ่ม(random.Random):
    pass


class สุ่มระบบ(random.SystemRandom):  # pylint: disable=abstract-method
    pass


# Methods
กระจายเบต้า = random.betavariate
กระจายทวินาม = random.binomialvariate
เลือก = random.choice
เลือกหลายอัน = random.choices
กระจายเอกซ์โพเนนเชียล = random.expovariate
กระจายแกมมา = random.gammavariate
เกาส์ = random.gauss
รับสถานะ = random.getstate
กระจายล็อกนอร์มอล = random.lognormvariate
กระจายปกติ = random.normalvariate
กระจายพาเรโต = random.paretovariate
ไบต์สุ่ม = random.randbytes
จำนวนเต็มสุ่ม = random.randint
ช่วงสุ่ม = random.randrange
ตัวอย่าง = random.sample
เมล็ดพันธุ์ = random.seed
ตั้งสถานะ = random.setstate
สับเปลี่ยน = random.shuffle
สามเหลี่ยม = random.triangular
สม่ำเสมอ = random.uniform
กระจายวอนมิเสส = random.vonmisesvariate
กระจายไวบูลล์ = random.weibullvariate

# Constants
BPF = random.BPF
LOG4 = random.LOG4
NV_MAGICCONST = random.NV_MAGICCONST
RECIP_BPF = random.RECIP_BPF
SG_MAGICCONST = random.SG_MAGICCONST
TWOPI = random.TWOPI

# Get all public names from the random module
random_names = [name for name in dir(random) if not name.startswith("_")]

# Get all names defined in this file (our Thai translations)
thai_names = [name for name in locals() if not name.startswith("_")]

# Combine both sets of names, removing duplicates
__all__ = list(set(random_names + thai_names))
