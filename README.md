# Piyathon

Piyathon is a Thai language-localized superset of Python that uses Thai keywords and function names. It employs a sophisticated translation approach combining tokenization and Abstract Syntax Tree (AST) manipulation to convert between standard Python and Piyathon code. This process involves tokenizing the source code, generating an AST, transforming the AST by translating Thai keywords and function names to their English equivalents (or vice versa), and finally generating code in the target language. This method ensures full compatibility with Python's syntax and features while providing a Thai language interface.

The project includes tools for bidirectional translation between Python and Piyathon, as well as a custom interpreter for directly executing Piyathon code. This interpreter leverages the existing Python ecosystem, translating Piyathon to Python on-the-fly before execution. Piyathon also provides Thai translations for built-in functions, constants, and error messages, and supports Thai characters in variable names, function names, and comments.

By reducing language barriers, Piyathon makes programming more accessible to Thai speakers, particularly beginners, while still allowing seamless transition to standard Python. It also enables experienced programmers to write Python code using Thai, potentially increasing productivity and code readability for Thai-speaking development teams.

## Installation

Piyathon requires Python 3.12. It can be installed using the following command:

```bash
pip install piyathon
```

# ปิยะทอน

ปิยะทอนเป็นภาษาโปรแกรมที่พัฒนาต่อยอดจากไพธอน โดยใช้คำสำคัญและชื่อฟังก์ชันเป็นภาษาไทย ปิยะทอนใช้วิธีการแปลภาษาที่ซับซ้อน โดยผสมผสานการแยกโทเคน (tokenization) และการจัดการต้นไม้ไวยากรณ์เชิงนามธรรม (Abstract Syntax Tree หรือ AST) เพื่อแปลงระหว่างโค้ดไพธอนมาตรฐานและโค้ดปิยะทอน กระบวนการนี้ประกอบด้วยการแยกโค้ดต้นฉบับเป็นโทเคน การสร้าง AST การแปลง AST โดยแปลคำสำคัญและชื่อฟังก์ชันภาษาไทยเป็นภาษาอังกฤษ (หรือในทางกลับกัน) และสุดท้ายคือการสร้างโค้ดในภาษาเป้าหมาย วิธีการนี้ช่วยให้ปิยะทอนสามารถทำงานร่วมกับไวยากรณ์และคุณสมบัติของไพธอนได้อย่างสมบูรณ์ ในขณะที่ให้อินเทอร์เฟซเป็นภาษาไทย

โครงการนี้มีเครื่องมือสำหรับการแปลสองทิศทางระหว่างไพธอนและปิยะทอน รวมถึงตัวแปลภาษาที่สามารถรันโค้ดปิยะทอนได้โดยตรง ตัวแปลภาษานี้ใช้ประโยชน์จากระบบนิเวศของไพธอนที่มีอยู่แล้ว โดยแปลงปิยะทอนเป็นไพธอนแบบทันทีก่อนการประมวลผล นอกจากนี้ ปิยะทอนยังมีการแปลฟังก์ชันในตัว ค่าคงที่ และข้อความแสดงข้อผิดพลาดเป็นภาษาไทย และรองรับการใช้ตัวอักษรภาษาไทยในชื่อตัวแปร ชื่อฟังก์ชัน และคำอธิบายในโค้ด

ด้วยการลดอุปสรรคทางภาษา ปิยะทอนช่วยให้การเขียนโปรแกรมเข้าถึงได้ง่ายขึ้นสำหรับผู้ใช้ภาษาไทย โดยเฉพาะผู้เริ่มต้น ในขณะเดียวกันก็ยังเอื้อให้สามารถเปลี่ยนไปใช้ไพธอนมาตรฐานได้อย่างราบรื่น นอกจากนี้ ยังช่วยให้โปรแกรมเมอร์ที่มีประสบการณ์สามารถเขียนโค้ดไพธอนโดยใช้ภาษาไทยได้ ซึ่งอาจช่วยเพิ่มประสิทธิภาพและความสามารถในการอ่านโค้ดสำหรับทีมพัฒนาที่ใช้ภาษาไทย

## การติดตั้ง

ปิยะทอนต้องการ Python 3.12 สามารถติดตั้งได้โดยใช้คำสั่งต่อไปนี้:

```bash
pip install piyathon
```
