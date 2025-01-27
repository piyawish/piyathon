# ตัวอย่างพื้นฐาน

```{eval-rst}
.. meta::
   :title: ตัวอย่างพื้นฐานการเขียนโค้ดกับภาษาปิยะธอน - ภาษา Python คำสั่งภาษาไทย
   :description: ตัวอย่างพื้นฐานภาษาปิยะธอนสำหรับผู้เริ่มต้นเรียนเขียนโปรแกรม Python เบื้องต้นในรูปแบบภาษาไทย เรียนง่าย เป็นเร็ว เหมาะสำหรับเด็ก ผู้ใหญ่ และผู้เริ่มต้นเขียนโค้ด Python
```

## การคำนวณพื้นฐาน

```piyathon
# คำนวณแฟกทอเรียล
นิยาม แฟกทอเรียล(n):
    ถ้า n <= 1:
        คืนค่า 1
    คืนค่า n * แฟกทอเรียล(n - 1)

# หาตัวหารร่วมมาก
นิยาม หา_หรม(a, b):
    ขณะ b:
        a, b = b, a % b
    คืนค่า a

# ทดสอบจำนวนเฉพาะ
นิยาม เป็นจำนวนเฉพาะ(n):
    ถ้า n < 2:
        คืนค่า เท็จ
    สำหรับ i ใน ช่วง(2, จำนวนเต็ม(n ** 0.5) + 1):
        ถ้า n % i == 0:
            คืนค่า เท็จ
    คืนค่า จริง
```

## การจัดการข้อความ

```piyathon
# นับคำในประโยค
นิยาม นับคำ(ข้อความ):
    คำ = ข้อความ.split()
    คืนค่า ความยาว(คำ)

# เช็คว่าเป็น palindrome
# (คำที่อ่านกลับหน้าหลังก็มีความหมายเหมือนกัน เช่น madam หรือ racecar)
นิยาม เป็นพาลินโดรม(ข้อความ):
    ข้อความ = ''.join(c สำหรับ c ใน ข้อความ.lower() ถ้า c.isalnum())
    คืนค่า ข้อความ == ข้อความ[::-1]

# แปลงเลขโรมัน
นิยาม แปลงเลขโรมัน(เลข):
    ค่า = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ผลลัพธ์ = 0
    สำหรับ i ใน ช่วง(ความยาว(เลข)):
        ถ้า i + 1 < ความยาว(เลข) และ ค่า[เลข[i]] < ค่า[เลข[i + 1]]:
            ผลลัพธ์ -= ค่า[เลข[i]]
        อื่น:
            ผลลัพธ์ += ค่า[เลข[i]]
    คืนค่า ผลลัพธ์
```

## การจัดการรายการ

```piyathon
# หาค่าที่ซ้ำกัน
นิยาม หาค่าซ้ำ(รายการ):
    พบแล้ว = เซ็ต()
    ซ้ำ = เซ็ต()
    สำหรับ x ใน รายการ:
        ถ้า x ใน พบแล้ว:
            ซ้ำ.add(x)
        อื่น:
            พบแล้ว.add(x)
    คืนค่า รายการ(ซ้ำ)

# จัดกลุ่มตามเงื่อนไข
นิยาม จัดกลุ่มคู่คี่(รายการ):
    คู่ = []
    คี่ = []
    สำหรับ เลข ใน รายการ:
        ถ้า เลข % 2 == 0:
            คู่.append(เลข)
        อื่น:
            คี่.append(เลข)
    คืนค่า (คู่, คี่)

# หาผลรวมย่อยที่มากที่สุด
นิยาม ผลรวมย่อยสูงสุด(รายการ):
    ผลรวมปัจจุบัน = ผลรวมสูงสุด = รายการ[0]
    สำหรับ x ใน รายการ[1:]:
        ผลรวมปัจจุบัน = ค่าสูงสุด(x, ผลรวมปัจจุบัน + x)
        ผลรวมสูงสุด = ค่าสูงสุด(ผลรวมสูงสุด, ผลรวมปัจจุบัน)
    คืนค่า ผลรวมสูงสุด
```

## การจัดการไฟล์

```piyathon
# อ่านและนับคำในไฟล์
นิยาม นับคำในไฟล์(ชื่อไฟล์):
    ลอง:
        ด้วย เปิด(ชื่อไฟล์, 'r', encoding='utf-8') เป็น ไฟล์:
            เนื้อหา = ไฟล์.read()
            คำ = เนื้อหา.split()
            คืนค่า ความยาว(คำ)
    ยกเว้น FileNotFoundError:
        พิมพ์(f"ไม่พบไฟล์: {ชื่อไฟล์}")
        คืนค่า 0

# เขียนรายการลงไฟล์ CSV
นิยาม เขียนไฟล์ CSV(ชื่อไฟล์, ข้อมูล):
    จาก csv นำเข้า writer
    ด้วย เปิด(ชื่อไฟล์, 'w', newline='', encoding='utf-8') เป็น ไฟล์:
        เขียน = writer(ไฟล์)
        สำหรับ แถว ใน ข้อมูล:
            เขียน.writerow(แถว)
```

## โครงสร้างข้อมูลพื้นฐาน

```piyathon
# สร้าง Stack อย่างง่าย
ชั้น Stack:
    นิยาม __เริ่มต้น__(ตัว):
        ตัว.ข้อมูล = []

    นิยาม ใส่(ตัว, ค่า):
        ตัว.ข้อมูล.append(ค่า)

    นิยาม นำออก(ตัว):
        ถ้า ไม่ ตัว.ว่าง():
            คืนค่า ตัว.ข้อมูล.pop()
        ยก ValueError("Stack ว่าง")

    นิยาม ว่าง(ตัว):
        คืนค่า ความยาว(ตัว.ข้อมูล) == 0

# สร้าง Queue อย่างง่าย
ชั้น Queue:
    นิยาม __เริ่มต้น__(ตัว):
        ตัว.ข้อมูล = []

    นิยาม ใส่(ตัว, ค่า):
        ตัว.ข้อมูล.append(ค่า)

    นิยาม นำออก(ตัว):
        ถ้า ไม่ ตัว.ว่าง():
            คืนค่า ตัว.ข้อมูล.pop(0)
        ยก ValueError("Queue ว่าง")

    นิยาม ว่าง(ตัว):
        คืนค่า ความยาว(ตัว.ข้อมูล) == 0
```

## การใช้งาน

```piyathon
# ทดสอบฟังก์ชันคำนวณ
พิมพ์(แฟกทอเรียล(5))            # 120
พิมพ์(หา_หรม(48, 18))           # 6
พิมพ์(เป็นจำนวนเฉพาะ(17))       # จริง

# ทดสอบฟังก์ชันข้อความ
พิมพ์(นับคำ("สวัสดี ชาวโลก"))    # 2
พิมพ์(เป็นพาลินโดรม("racecar"))   # จริง
พิมพ์(แปลงเลขโรมัน("IV"))       # 4

# ทดสอบฟังก์ชันรายการ
พิมพ์(หาค่าซ้ำ([1, 2, 2, 3, 3, 4]))      # [2, 3]
พิมพ์(จัดกลุ่มคู่คี่([1, 2, 3, 4, 5]))     # ([2, 4], [1, 3, 5])
พิมพ์(ผลรวมย่อยสูงสุด([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6

# ทดสอบโครงสร้างข้อมูล
stack = Stack()
stack.ใส่(1)
stack.ใส่(2)
พิมพ์(stack.นำออก())  # 2

queue = Queue()
queue.ใส่("ก")
queue.ใส่("ข")
พิมพ์(queue.นำออก())  # "ก"
```
