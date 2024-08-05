import random


# Classes
class สุ่มตัวเลข(random.Random):
    pass


# Functions
def ค่าเมล็ดพันธุ์(a=None, version=2):
    return random.seed(a, version)


def รับค่าเมล็ดพันธุ์():
    return random.getstate()


def ตั้งค่าเมล็ดพันธุ์(state):
    return random.setstate(state)


def สุ่ม():
    return random.random()


def สุ่มช่วง(a, b):
    return random.randrange(a, b)


def สุ่มจำนวนเต็ม(a, b):
    return random.randint(a, b)


def เลือกสุ่ม(seq):
    return random.choice(seq)


def เลือกสุ่มหลายครั้ง(population, weights=None, *, cum_weights=None, k=1):
    return random.choices(population, weights, cum_weights=cum_weights, k=k)


def สับ(x, random=None):
    return random.shuffle(x, random)


def ตัวอย่างสุ่ม(population, k):
    return random.sample(population, k)


def สุ่มแบบสม่ำเสมอ(a, b):
    return random.uniform(a, b)


def สุ่มสามเหลี่ยม(low, high, mode):
    return random.triangular(low, high, mode)


def สุ่มเบต้า(alpha, beta):
    return random.betavariate(alpha, beta)


def สุ่มเอกซ์โพเนนเชียล(lambd):
    return random.expovariate(lambd)


def สุ่มแกมมา(alpha, beta):
    return random.gammavariate(alpha, beta)


def สุ่มเกาส์เซียน(mu, sigma):
    return random.gauss(mu, sigma)


def สุ่มลอกนอร์มอล(mu, sigma):
    return random.lognormvariate(mu, sigma)


def สุ่มนอร์มอล(mu, sigma):
    return random.normalvariate(mu, sigma)


def สุ่มวอน์มิสเซส(mu, kappa):
    return random.vonmisesvariate(mu, kappa)


def สุ่มพาเรโต(alpha):
    return random.paretovariate(alpha)


def สุ่มไวบูลล์(alpha, beta):
    return random.weibullvariate(alpha, beta)


# Constants
ข้อมูลการเวอร์ชัน = random.__all__

# Create an instance of Random class
ตัวสุ่มตัวเลข = สุ่มตัวเลข()

# System random
ระบบสุ่ม = random.SystemRandom()
