# การติดตั้งภาษาปิยะธอน

```{eval-rst}
.. meta::
  :title: การติดตั้งภาษาปิยะธอน pip install piyathon
  :description: เรียนการติดตั้งภาษาปิยะธอน pip install piyathon สำหรับการเขียนโปรแกรม Python เบื้องต้นในรูปแบบภาษาไทย เรียนง่าย เป็นเร็ว ครอบคลุมทั้ง Windows, macOS และ Linux
```

คู่มือนี้จะแนะนำวิธีการติดตั้งภาษาปิยะธอนบนระบบปฏิบัติการต่างๆ

## ความต้องการของระบบ

เนื่องจากภาษาปิยะธอนเป็นไลบรารีที่พัฒนาขึ้นบนภาษาไพทอน จึงสามารถติดตั้งได้บนระบบปฏิบัติการใดก็ตามที่สามารถรันภาษาไพทอนได้ โดยมีความต้องการพื้นฐานดังนี้:

- ระบบปฏิบัติการที่รองรับภาษาไพทอน (Windows, macOS, Linux หรือระบบปฏิบัติการอื่นๆ ที่รันภาษาไพทอนได้)
- ภาษาไพทอน: เวอร์ชัน 3.12 ขึ้นไป
- พื้นที่ดิสก์ว่าง: อย่างน้อย 100 MB
- หน่วยความจำ (RAM): อย่างน้อย 512 MB

## การติดตั้งตัวแปลภาษาปิยะธอน

ภาษาปิยะธอนเป็นไลบรารี่ของภาษาไพทอนที่ทำงานบนตัวแปลภาษาไพทอนอีกชั้นหนึ่ง ดังนั้นคุณต้องติดตั้งภาษาไพทอนให้เรียบร้อยก่อนแล้วจึงจะติดตั้งภาษาปิยะธอนต่อได้

ภาษาปิยะธอนไลบรารี่อยู่ที่ [piyathon](https://pypi.org/project/piyathon/) ใน ​PyPI และสามารถติดตั้งผ่านคำสั่ง pip ได้เช่นเดียวกับไลบรารี่ของภาษาไพทอนทั่วไป

### วิธีที่ 1: ติดตั้งผ่านคำสั่ง pip

```bash
pip install piyathon
```

### วิธีที่ 2: ติดตั้งจากซอร์สโค้ด

```bash
git clone https://github.com/piyawish/piyathon
cd piyathon
pip install -e .
```

## การติดตั้งบนระบบปฏิบัติการต่างๆ

### Windows

1. ดาวน์โหลดและติดตั้งภาษาไพทอนจาก [python.org](https://python.org)
2. เปิด Command Prompt หรือ PowerShell
3. รันคำสั่ง:

```bash
pip install piyathon
```

### macOS

1. ติดตั้ง Homebrew (ถ้ายังไม่มี):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

1. ติดตั้งภาษาไพทอน:

```bash
brew install python
```

1. ติดตั้งภาษาปิยะธอน:

```bash
pip install piyathon
```

### Linux (Ubuntu/Debian)

```bash
# ติดตั้งภาษาไพทอนและเครื่องมือที่จำเป็น
sudo apt update
sudo apt install python3 python3-pip

# ติดตั้งภาษาปิยะธอน
pip install piyathon
```

## การทดสอบการติดตั้ง

1. เปิดเทอร์มินัลหรือ Command Prompt
1. รันคำสั่ง:

```bash
piyathon --version
```

1. ทดสอบการทำงาน:

```piyathon
# สร้างไฟล์ test.pi
พิมพ์("สวัสดีชาวโลก")
```

1. รันโปรแกรม:

```bash
piyathon test.pi
```

## ข้อควรระวัง

```{warning}
ตรวจสอบให้แน่ใจว่าคุณติดตั้งภาษาไพทอนเวอร์ชันที่ถูกต้อง (3.12+) ก่อนติดตั้งภาษาปิยะธอน
```

## การแก้ปัญหาที่พบบ่อย

### ปัญหา: คำสั่ง pip ไม่ทำงาน

- Windows: ตรวจสอบว่าได้เพิ่ม Python Scripts path ใน PATH หรือยัง
- Linux/macOS: ลองใช้ `pip3` แทน `pip`

### ปัญหา: ModuleNotFoundError

ลองรันคำสั่งต่อไปนี้:

```bash
pip install --upgrade pip
pip install piyathon --force-reinstall
```

## การถอนการติดตั้ง

หากต้องการถอนการติดตั้งภาษาปิยะธอน:

```bash
pip uninstall piyathon
```

## ขั้นตอนถัดไป

- [ก้าวแรก](first_steps.md) - เริ่มเขียนโปรแกรมภาษาปิยะธอนแรกของคุณ
- [การตั้งค่า](configuration.md) - ตั้งค่าสภาพแวดล้อมการพัฒนา
- [บทเรียน](../tutorial/basics.md) - เรียนรู้การใช้งานภาษาปิยะธอนเพิ่มเติม
