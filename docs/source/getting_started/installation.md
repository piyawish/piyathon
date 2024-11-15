# การติดตั้งปิยะทอน

คู่มือนี้จะแนะนำวิธีการติดตั้งปิยะทอนบนระบบปฏิบัติการต่างๆ

## ความต้องการของระบบ

เนื่องจากปิยะทอนเป็นไลบรารีที่พัฒนาขึ้นบนภาษาไพทอน จึงสามารถติดตั้งได้บนระบบปฏิบัติการใดก็ตามที่สามารถรันไพทอนได้ โดยมีความต้องการพื้นฐานดังนี้:

- ระบบปฏิบัติการที่รองรับไพทอน (Windows, macOS, Linux หรือระบบปฏิบัติการอื่นๆ ที่รันไพทอนได้)
- ไพทอน: เวอร์ชัน 3.12 ขึ้นไป
- พื้นที่ดิสก์ว่าง: อย่างน้อย 100 MB
- หน่วยความจำ (RAM): อย่างน้อย 512 MB

## การติดตั้งตัวแปลภาษาปิยะทอน

ปิยะทอนเป็นไลบรารี่ของภาษาไพทอนที่ทำงานบนตัวแปลภาษาไพทอนอีกชั้นหนึ่ง ดังนั้นคุณต้องติดตั้งไพทอนให้เรียบร้อยก่อนแล้วจึงจะติดตั้งปิยะทอนต่อได้

ปิยะทอนไลบรารี่อยู่ที่ [piyathon](https://pypi.org/project/piyathon/) ใน ​PyPI และสามารถติดตั้งผ่านคำสั่ง pip ได้เช่นเดียวกับไลบรารี่ของไพทอนทั่วไป

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

1. ดาวน์โหลดและติดตั้งไพทอนจาก [python.org](https://python.org)
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

1. ติดตั้งไพทอน:

```bash
brew install python
```

1. ติดตั้งปิยะทอน:

```bash
pip install piyathon
```

### Linux (Ubuntu/Debian)

```bash
# ติดตั้งไพทอนและเครื่องมือที่จำเป็น
sudo apt update
sudo apt install python3 python3-pip

# ติดตั้งปิยะทอน
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
ตรวจสอบให้แน่ใจว่าคุณติดตั้งไพทอนเวอร์ชันที่ถูกต้อง (3.12+) ก่อนติดตั้งปิยะทอน
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

หากต้องการถอนการติดตั้งปิยะทอน:

```bash
pip uninstall piyathon
```

## ขั้นตอนถัดไป

- [ก้าวแรก](first_steps.md) - เริ่มเขียนโปรแกรมปิยะทอนแรกของคุณ
- [การตั้งค่า](configuration.md) - ตั้งค่าสภาพแวดล้อมการพัฒนา
- [บทเรียน](../tutorial/basics.md) - เรียนรู้การใช้งานปิยะทอนเพิ่มเติม
