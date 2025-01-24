# ชีทสรุปภาษาปิยะทอน

## คำสั่งควบคุม (Control Flow)

### เงื่อนไข (Conditionals)

```python
# Python
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```

```piyathon
# ปิยะทอน
ถ้า x > 0:
    พิมพ์("บวก")
อื่นถ้า x < 0:
    พิมพ์("ลบ")
อื่น:
    พิมพ์("ศูนย์")
```

### การวนซ้ำ (Loops)

```python
# Python
for i in range(3):
    if i == 1:
        continue
    print(i)
```

```piyathon
# ปิยะทอน
สำหรับ i ใน ช่วง(3):
    ถ้า i == 1:
        ทำต่อ
    พิมพ์(i)
```

```python
# Python
while count > 0:
    if done:
        break
    count -= 1
```

```piyathon
# ปิยะทอน
ขณะ จำนวน > 0:
    ถ้า เสร็จ:
        หยุด
    จำนวน -= 1
```

### ฟังก์ชันและการคืนค่า (Functions and Return)

```python
# Python
def greet(name):
    return f"Hello, {name}"
```

```piyathon
# ปิยะทอน
นิยาม ทักทาย(ชื่อ):
    คืนค่า f"สวัสดี, {ชื่อ}"
```

### การจัดการข้อผิดพลาด (Error Handling)

```{note}
Exceptions ยังไม่ได้แปลทั้งหมด
```

```python
# Python
try:
    result = 10 / x
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("Done")
```

```piyathon
# ปิยะทอน
ลอง:
    ผลลัพธ์ = 10 / x
ยกเว้น การหารด้วยศูนย์:
    พิมพ์("ผิดพลาด: หารด้วยศูนย์")
สุดท้าย:
    พิมพ์("เสร็จ")
```

### การยืนยัน (Assertions)

```python
# Python
def set_age(age):
    assert age >= 0, "Age must be positive"
```

```piyathon
# ปิยะทอน
นิยาม ตั้งค่าอายุ(อายุ):
    ยืนยัน อายุ >= 0, "อายุต้องเป็นบวก"
```

## คลาสและออบเจ็กต์ (Classes and Objects)

```python
# Python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"
```

```piyathon
# ปิยะทอน
ชั้น สุนัข:
    นิยาม __เริ่มต้น__(ตัว, ชื่อ):
        ตัว.ชื่อ = ชื่อ

    นิยาม เห่า(ตัว):
        คืนค่า "โฮ่ง!"
```

## ตัวดำเนินการตรรกะ (Logical Operators)

```python
# Python
age = 25
has_id = True
is_student = False

# AND operator
if age >= 18 and has_id:
    print("Can enter")

# OR operator
if is_student or age < 18:
    print("Gets discount")

# NOT operator
if not is_student:
    print("Regular price")
```

```piyathon
# ปิยะทอน
อายุ = 25
มีบัตร = จริง
เป็นนักเรียน = เท็จ

# ตัวดำเนินการ และ
ถ้า อายุ >= 18 และ มีบัตร:
    พิมพ์("เข้าได้")

# ตัวดำเนินการ หรือ
ถ้า เป็นนักเรียน หรือ อายุ < 18:
    พิมพ์("ได้ส่วนลด")

# ตัวดำเนินการ ไม่
ถ้า ไม่ เป็นนักเรียน:
    พิมพ์("ราคาปกติ")
```

## การนำเข้าโมดูล (Module Imports)

```{note}
Standard libraries ยังไม่ได้แปลทั้งหมด
```

```python
# Python
from math import pi as PI
import random
```

```piyathon
# ปิยะทอน
จาก คณิต นำเข้า พาย เป็น ค่าพาย
นำเข้า สุ่ม
```

## ฟังก์ชันพิเศษ (Special Functions)

### แลมบ์ดา (Lambda)

```python
# Python
square = lambda x: x * x
```

```piyathon
# ปิยะทอน
กำลังสอง = แลมบ์ดา x: x * x
```

### การจัดการบริบท (Context Management)

```python
# Python
with open('file.txt') as f:
    content = f.read()
```

```piyathon
# ปิยะทอน
ด้วย เปิด('ไฟล์.txt') เป็น ไฟล์:
    เนื้อหา = ไฟล์.อ่าน()
```

## ค่าคงที่และค่าพิเศษ (Constants and Special Values)

```python
# Python
success = True
empty = None
has_error = False
```

```piyathon
# ปิยะทอน
สำเร็จ = จริง
ว่าง = ไม่มีค่า
มีข้อผิดพลาด = เท็จ
```

## การประสานงาน (Asynchronous)

```python
# Python
async def fetch_data():
    await process()
```

```piyathon
# ปิยะทอน
ไม่ประสาน นิยาม ดึงข้อมูล():
    รอประสาน ประมวลผล()
```

## การจัดการขอบเขตตัวแปร (Variable Scope)

```python
# Python
global counter
nonlocal shared_var
```

```piyathon
# ปิยะทอน
ทั่วไป ตัวนับ
นอกเขต ตัวแปรร่วม
```

## การเทียบรูปแบบ (Pattern Matching)

```python
# Python
match status:
    case "ok":
        print("Success")
    case "error":
        print("Failed")
```

```piyathon
# ปิยะทอน
เทียบ สถานะ:
    เมื่อ "สำเร็จ":
        พิมพ์("ผ่าน")
    เมื่อ "ผิดพลาด":
        พิมพ์("ล้มเหลว")
```
