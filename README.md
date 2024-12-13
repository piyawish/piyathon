# Piyathon

Piyathon is a Thai language-localized superset of Python that uses Thai keywords and function names. It employs a sophisticated translation approach combining tokenization and Abstract Syntax Tree (AST) manipulation to convert between standard Python and Piyathon code. This process involves tokenizing the source code, generating an AST, transforming the AST by translating Thai keywords and function names to their English equivalents (or vice versa), and finally generating code in the target language. This method ensures full compatibility with Python's syntax and features while providing a Thai language interface.

The project includes tools for bidirectional translation between Python and Piyathon, as well as a custom interpreter for directly executing Piyathon code. This interpreter leverages the existing Python ecosystem, translating Piyathon to Python on-the-fly before execution. Piyathon also provides Thai translations for built-in functions, constants, and error messages, and supports Thai characters in variable names, function names, and comments.

By reducing language barriers, Piyathon makes programming more accessible to Thai speakers, particularly beginners, while still allowing seamless transition to standard Python. It also enables experienced programmers to write Python code using Thai, potentially increasing productivity and code readability for Thai-speaking development teams.

## Installation

Piyathon requires Python 3.12. It can be installed using the following command:

```bash
pip install piyathon
```

### VS Code Extension

To get syntax highlighting and language support in Visual Studio Code:

1. Open VS Code
2. Go to the Extensions view (Ctrl+Shift+X or Cmd+Shift+X on macOS)
3. Search for "Piyathon"
4. Click Install on the "Piyathon" extension

Alternatively, you can install it by running this command in VS Code's Quick Open (Ctrl+P or Cmd+P on macOS):

```bash
ext install piyawish.piyathon-vscode
```

The extension provides:

- Syntax highlighting for .pi files
- Thai keyword support
- Code formatting
- Smart indentation

# ปิยะธอน

ปิยะธอนเป็นภาษาโปรแกรมที่พัฒนาต่อยอดจากไพธอน โดยใช้คำสำคัญและชื่อฟังก์ชันเป็นภาษาไทย ปิยะธอนใช้วิธีการแปลภาษาที่ซับซ้อน โดยผสมผสานการแยกโทเคน (tokenization) และการจัดการต้นไม้ไวยากรณ์เชิงนามธรรม (Abstract Syntax Tree หรือ AST) เพื่อแปลงระหว่างโค้ดไพธอนมาตรฐานและโค้ดปิยะธอน กระบวนการนี้ประกอบด้วยการแยกโค้ดต้นฉบับเป็นโทเคน การสร้าง AST การแปลง AST โดยแปลคำสำคัญและชื่อฟังก์ชันภาษาไทยเป็นภาษาอังกฤษ (หรือในทางกลับกัน) และสุดท้ายคือการสร้างโค้ดในภาษาเป้าหมาย วิธีการนี้ช่วยให้ปิยะธอนสามารถทำงานร่วมกับไวยากรณ์และคุณสมบัติของไพธอนได้อย่างสมบูรณ์ ในขณะที่ให้อินเทอร์เฟซเป็นภาษาไทย

โครงการนี้มีเครื่องมือสำหรับการแปลสองทิศทางระหว่างไพธอนและปิยะธอน รวมถึงตัวแปลภาษาที่สามารถรันโค้ดปิยะธอนได้โดยตรง ตัวแปลภาษานี้ใช้ประโยชน์จากระบบนิเวศของไพธอนที่มีอยู่แล้ว โดยแปลงปิยะธอนเป็นไพธอนแบบทันทีก่อนการประมวลผล นอกจากนี้ ปิยะธอนยังมีการแปลฟังก์ชันในตัว ค่าคงที่ และข้อความแสดงข้อผิดพลาดเป็นภาษาไทย และรองรับการใช้ตัวอักษรภาษาไทยในชื่อตัวแปร ชื่อฟังก์ชัน และคำอธิบายในโค้ด

ด้วยการลดอุปสรรคทางภาษา ปิยะธอนช่วยให้การเขียนโปรแกรมเข้าถึงได้ง่ายขึ้นสำหรับผู้ใช้ภาษาไทย โดยเฉพาะผู้เริ่มต้น ในขณะเดียวกันก็ยังเอื้อให้สามารถเปลี่ยนไปใช้ไพธอนมาตรฐานได้อย่างราบรื่น นอกจากนี้ ยังช่วยให้โปรแกรมเมอร์ที่มีประสบการณ์สามารถเขียนโค้ดไพธอนโดยใช้ภาษาไทยได้ ซึ่งอาจช่วยเพิ่มประสิทธิภาพและความสามารถในการอ่านโค้ดสำหรับทีมพัฒนาที่ใช้ภาษาไทย

## การติดตั้ง

ปิยะธอนต้องการ Python 3.12 สามารถติดตั้งได้โดยใช้คำสั่งต่อไปนี้:

```bash
pip install piyathon
```

### ส่วนขยาย VS Code

วิธีติดตั้งส่วนขยายสำหรับ Visual Studio Code เพื่อรองรับการเขียนโค้ดปิยะธอน:

1. เปิด VS Code
2. ไปที่มุมมองส่วนขยาย (กด Ctrl+Shift+X หรือ Cmd+Shift+X บน macOS)
3. ค้นหา "Piyathon"
4. คลิกติดตั้งที่ส่วนขยาย "Piyathon"

หรือติดตั้งโดยรันคำสั่งนี้ใน Quick Open ของ VS Code (กด Ctrl+P หรือ Cmd+P บน macOS):

```bash
ext install piyawish.piyathon-vscode
```

ส่วนขยายนี้มีคุณสมบัติดังนี้:

- ไฮไลท์ไวยากรณ์สำหรับไฟล์ .pi
- รองรับคำสำคัญภาษาไทย
- การจัดรูปแบบโค้ด
- การเยื้องอัตโนมัติ
