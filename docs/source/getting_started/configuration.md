# การตั้งค่าสภาพแวดล้อมการพัฒนา

เอกสารนี้จะแนะนำการตั้งค่าสภาพแวดล้อมการพัฒนาสำหรับปิยะทอน ทั้งการตั้งค่า IDE และเครื่องมือต่างๆ

## การตั้งค่า IDE

Integrated Development Environment (IDE) ที่ใช้งานได้ดีกับการเขียนภาษาปิยะทอนคือ Visual Studio Code ส่วน IDE อื่นๆ ที่ใช้เขียนภาษาไพทอนได้ควรจะสามารถใช้งานได้เช่นเดียวกันเพราะปิยะทอนพัฒนาบนพื้นฐานของภาษาไพทอน และตัวปิยะทอนเองคือไลบรารีของภาษาไพทอน

### Visual Studio Code (แนะนำ)

1. ติดตั้ง Visual Studio Code จาก [code.visualstudio.com](https://code.visualstudio.com)

1. ติดตั้งส่วนขยาย (extensions) ที่จำเป็น:
   - "Piyathon" - ส่วนขยายหลักสำหรับปิยะทอน
   - "Python" - สำหรับการรันโค้ดไพทอนพื้นฐาน (จะติดตั้งอัตโนมัติเมื่อติดตั้งส่วนขยาย Piyathon)

<!--

1. ตั้งค่าในไฟล์ `settings.json`:

```json
{
    "files.associations": {
        "*.pi": "python"
    },
    "piyathon.interpreter.path": "/path/to/piyathon",
    "piyathon.linting.enabled": true
}
```

### PyCharm

1. ติดตั้งปลั๊กอิน Piyathon:
   - เปิด Settings/Preferences
   - ไปที่ Plugins
   - ค้นหาและติดตั้ง "Piyathon Support"

2. ตั้งค่า File Type:
   - ไปที่ Settings → Editor → File Types
   - เพิ่มนามสกุล `*.pi` ใน Python Files

## ตัวแปรสภาพแวดล้อม

### Windows

```batch
# ตั้งค่าใน Command Prompt
set PIYATHON_HOME=C:\Program Files\Piyathon
set PATH=%PATH%;%PIYATHON_HOME%\bin
```

### macOS/Linux

เพิ่มในไฟล์ `~/.bashrc` หรือ `~/.zshrc`:

```bash
export PIYATHON_HOME=/usr/local/piyathon
export PATH="$PATH:$PIYATHON_HOME/bin"
```

## ไฟล์การตั้งค่าปิยะทอน

ปิยะทอนใช้ไฟล์ `pyproject.toml` สำหรับการตั้งค่าโครงการ:

```toml
[tool.piyathon]
version = "0.1.0"
description = "โครงการปิยะทอน"

[tool.piyathon.scripts]
start = "piyathon main.pi"
test = "piyathon -m unittest"

[tool.piyathon.dependencies]
numpy = "^1.20.0"
pandas = "^1.3.0"
```

## การตั้งค่า Language Server

ปิยะทอนมาพร้อมกับ Language Server ที่ช่วยในการเขียนโค้ด:

1. ติดตั้ง Language Server:

```bash
pip install piyathon-language-server
```

2. ตั้งค่าใน VS Code:

```json
{
    "piyathon.languageServer.enabled": true,
    "piyathon.languageServer.path": "piyathon-language-server"
}
```

## การตั้งค่า Linter และ Formatter

### การใช้ pylint กับปิยะทอน

1. ติดตั้ง pylint-piyathon:

```bash
pip install pylint-piyathon
```

2. สร้างไฟล์ `.pylintrc`:

```ini
[MASTER]
load-plugins=pylint_piyathon

[MESSAGES CONTROL]
disable=C0111,C0103
```

### การใช้ black กับปิยะทอน

1. ติดตั้ง black-piyathon:

```bash
pip install black-piyathon
```

2. สร้างไฟล์ `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pi$'
```

## คีย์ลัดที่มีประโยชน์

### VS Code

- `F5` - รันโปรแกรม
- `Ctrl+Space` - เปิด code completion
- `F12` - ไปยังคำจำกัดความ
- `Shift+Alt+F` - จัดรูปแบบโค้ด

### PyCharm

- `Shift+F10` - รันโปรแกรม
- `Ctrl+B` - ไปยังคำจำกัดความ
- `Ctrl+Alt+L` - จัดรูปแบบโค้ด

## การแก้ไขปัญหาที่พบบ่อย

```{note}
### ปัญหา: Language Server ไม่ทำงาน
1. ตรวจสอบการติดตั้ง Language Server
2. รีสตาร์ท IDE
3. ตรวจสอบ log ใน Output panel
```

```{warning}
### ปัญหา: การ Import ไม่ทำงาน
ตรวจสอบให้แน่ใจว่าได้ตั้งค่า PYTHONPATH ถูกต้อง และไฟล์ `__init__.pi` อยู่ในตำแหน่งที่ถูกต้อง
```

-->