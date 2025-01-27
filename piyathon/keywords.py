# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
Piyathon-Python Keyword Mapping Module

This module defines the bidirectional mapping between Python and Piyathon keywords,
built-in functions, and special variables. It serves as the foundation for the
translation system between the two languages.

Core Components:
    - PYTHON_KEYWORDS: Maps Python keywords to their Piyathon equivalents
    - PYTHON_BUILTIN_FUNCTIONS: Maps Python built-in functions to Piyathon names
    - PYTHON_SPECIAL_BUILTIN_VARIABLES: Maps Python special variables to Piyathon names
    - PY_TO_PI: Combined dictionary for Python to Piyathon translation
    - PI_TO_PY: Inverse mapping for Piyathon to Python translation

Data Structure Relationships:
    - All mappings are one-to-one between Python and Piyathon identifiers
    - PY_TO_PI combines all three mapping dictionaries
    - PI_TO_PY is the inverse of PY_TO_PI for reverse translation

Integration Points:
    - Used by PiyathonTranslator for code translation
    - Referenced during tokenization and untokenization processes
    - Supports both standard keywords and special method names

Known Limitations:
    - Only covers Python's built-in keywords and functions
    - Does not include standard library function mappings
    - Assumes one-to-one mapping between languages
"""

PYTHON_KEYWORDS = {
    "and": "และ",
    "as": "เป็น",
    "assert": "ยืนยัน",
    "async": "ไม่ประสาน",
    "await": "รอประสาน",
    "break": "หยุด",
    "case": "เมื่อ",
    "class": "ชั้น",
    "continue": "ทำต่อ",
    "def": "นิยาม",
    "del": "ลบ",
    "elif": "อื่นถ้า",
    "else": "อื่น",
    "except": "ยกเว้น",
    "False": "เท็จ",
    "finally": "สุดท้าย",
    "for": "สำหรับ",
    "from": "จาก",
    "global": "ทั่วไป",
    "if": "ถ้า",
    "import": "นำเข้า",
    "in": "ใน",
    "is": "คือ",
    "lambda": "แลมบ์ดา",
    "match": "เทียบ",
    "nonlocal": "นอกเขต",
    "None": "ไม่มีค่า",
    "not": "ไม่",
    "or": "หรือ",
    "pass": "ผ่าน",
    "raise": "ยก",
    "return": "คืนค่า",
    "True": "จริง",
    "try": "ลอง",
    "while": "ขณะ",
    "with": "ด้วย",
    "yield": "ให้",
}

PYTHON_BUILTIN_FUNCTIONS = {
    "abs": "ค่าสัมบูรณ์",
    "aiter": "อิเทอเรเตอร์อะซิงค์",
    "all": "ทั้งหมด",
    "anext": "ถัดไปอะซิงค์",
    "any": "ใดๆ",
    "ascii": "แอสกี",
    "bin": "ฐานสอง",
    "bool": "บูลีน",
    "breakpoint": "จุดพัก",
    "bytearray": "แถวไบต์",
    "bytes": "ไบต์",
    "callable": "เรียกได้",
    "chr": "อักขระ",
    "classmethod": "เมธอดคลาส",
    "compile": "คอมไพล์",
    "complex": "จำนวนเชิงซ้อน",
    "delattr": "ลบแอททริบิวต์",
    "dict": "พจนานุกรม",
    "dir": "ไดเรกทอรี",
    "divmod": "หารเอาเศษ",
    "enumerate": "ลำดับ",
    "eval": "ประเมิน",
    "exec": "ประมวลผล",
    "filter": "กรอง",
    "float": "ทศนิยม",
    "format": "จัดรูปแบบ",
    "frozenset": "เซ็ตแช่แข็ง",
    "getattr": "รับแอททริบิวต์",
    "globals": "ตัวแปรโกลบอล",
    "hasattr": "มีแอททริบิวต์",
    "hash": "แฮช",
    "help": "ช่วยเหลือ",
    "hex": "ฐานสิบหก",
    "id": "รหัส",
    "input": "รับค่า",
    "int": "จำนวนเต็ม",
    "isinstance": "เป็นชนิด",
    "issubclass": "เป็นคลาสลูก",
    "iter": "วนซ้ำ",
    "len": "ความยาว",
    "list": "รายการ",
    "locals": "ตัวแปรท้องถิ่น",
    "map": "แปลง",
    "max": "ค่าสูงสุด",
    "memoryview": "มุมมองหน่วยความจำ",
    "min": "ค่าต่ำสุด",
    "next": "ถัดไป",
    "object": "วัตถุ",
    "oct": "ฐานแปด",
    "open": "เปิด",
    "ord": "รหัสอักขระ",
    "pow": "ยกกำลัง",
    "print": "พิมพ์",
    "property": "คุณสมบัติ",
    "range": "ช่วง",
    "repr": "ตัวแทน",
    "reversed": "ย้อนกลับ",
    "round": "ปัดเศษ",
    "set": "เซ็ต",
    "setattr": "ตั้งแอททริบิวต์",
    "slice": "ตัดส่วน",
    "sorted": "เรียงลำดับ",
    "staticmethod": "เมธอดคงที่",
    "str": "สตริง",
    "sum": "ผลรวม",
    "super": "คลาสแม่",
    "tuple": "ทูเพิล",
    "type": "ชนิด",
    "vars": "ตัวแปร",
    "zip": "จับคู่",
    "__import__": "__นำเข้า__",
}

PYTHON_SPECIAL_BUILTIN_VARIABLES = {
    "__name__": "__ชื่อ__",
    "__doc__": "__เอกสาร__",
    "__file__": "__ไฟล์__",
    "__dict__": "__พจนานุกรม__",
    "__package__": "__แพ็กเกจ__",
    "__path__": "__เส้นทาง__",
    "__module__": "__โมดูล__",
    "__bases__": "__คลาสฐาน__",
    "__class__": "__คลาส__",
    "__init__": "__เริ่มต้น__",
    "__del__": "__ลบ__",
    "__repr__": "__ตัวแทนทางการ__",
    "__str__": "__ตัวแทน__",
    "__bytes__": "__ไบต์__",
    "__format__": "__จัดรูปแบบ__",
    "__lt__": "__น้อยกว่า__",
    "__le__": "__น้อยกว่าเท่ากับ__",
    "__eq__": "__เท่ากับ__",
    "__ne__": "__ไม่เท่ากับ__",
    "__gt__": "__มากกว่า__",
    "__ge__": "__มากกว่าเท่ากับ__",
    "__hash__": "__แฮช__",
    "__bool__": "__บูลีน__",
    "__call__": "__เรียกใช้__",
    "__len__": "__ความยาว__",
    "__getitem__": "__เข้าถึงสมาชิก__",
    "__setitem__": "__กำหนดสมาชิก__",
    "__delitem__": "__ลบสมาชิก__",
    "__iter__": "__วนซ้ำ__",
    "__next__": "__ถัดไป__",
    "__enter__": "__เข้า__",
    "__exit__": "__ออก__",
    "__slots__": "__ช่องเก็บ__",
    "__all__": "__ทั้งหมด__",
}

PY_TO_PI = {
    **PYTHON_KEYWORDS,
    **PYTHON_BUILTIN_FUNCTIONS,
    **PYTHON_SPECIAL_BUILTIN_VARIABLES,
}

PI_TO_PY = {v: k for k, v in PY_TO_PI.items()}
