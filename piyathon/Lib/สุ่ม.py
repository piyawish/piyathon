# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

# Generated module file. Do not edit directly.

"""
Piyathon Random Number Generation Module (สุ่ม)

This module provides Thai language bindings for Python's random module,
offering a complete suite of random number generation tools and utilities.

Core Components:
    - สุ่ม: Main random number generator class (maps to random.Random)
    - สุ่มระบบ: System random number generator (maps to random.SystemRandom)
    - Various distribution functions (normal, beta, gamma, etc.)
    - Utility functions for sampling and shuffling
    - Mathematical constants used in distributions

Key Features:
    - Full support for all random module functionality
    - Thai language function and class names
    - Maintains all original Python random module behaviors
    - Thread-safe random number generation options

Integration Points:
    - Compatible with all standard Python random module use cases
    - Can be used interchangeably with the original random module
    - Supports both pure Python and system random number generation

Usage Examples:
    >>> from piyathon.Lib.สุ่ม import สุ่มจำนวนเต็ม
    >>> สุ่มจำนวนเต็ม(1, 10)  # Random integer between 1 and 10
    >>> from piyathon.Lib.สุ่ม import สุ่ม
    >>> gen = สุ่ม()  # Create a random number generator instance
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
