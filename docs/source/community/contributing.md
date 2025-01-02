# การมีส่วนร่วม

```{note}
หน้านี้อยู่ระหว่างการจัดทำ
```

คู่มือนี้จะแนะนำวิธีการมีส่วนร่วมในการพัฒนาภาษาปิยะธอน

## การเริ่มต้น

1. **Fork Repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/piyathon.git
   cd piyathon
   git remote add upstream https://github.com/piyawish/piyathon.git
   ```

2. **ติดตั้ง**

   ```bash
   python -m venv venv
   source venv/bin/activate  # หรือ venv\Scripts\activate บน Windows
   pip install -e ".[dev]"
   ```

## การส่ง Pull Request

1. **สร้าง Branch**

   ```bash
   git checkout -b feature/your-feature
   ```

2. **พัฒนาและทดสอบ**

   ```bash
   pytest
   black .
   flake8
   ```

3. **Commit และ Push**

   ```bash
   git add .
   git commit -m "เพิ่ม: อธิบายการเปลี่ยนแปลง"
   git push origin feature/your-feature
   ```

4. สร้าง Pull Request ที่ GitHub repository

## แนวทางการเขียนโค้ด

1. **รูปแบบโค้ด**
   - ใช้ black จัดรูปแบบ
   - ทำตาม PEP8
   - เขียน docstring

2. **การเขียนเทสต์**
   - เขียน unit tests
   - ทดสอบให้ครอบคลุม
   - รันเทสต์ก่อน commit

## การรายงานปัญหา

เมื่อพบปัญหา ให้รายงานที่ [GitHub Issues](https://github.com/piyawish/piyathon/issues) พร้อมระบุ

- รายละเอียดปัญหา
- ขั้นตอนการทำซ้ำ
- เวอร์ชันที่ใช้
- โค้ดตัวอย่าง (ถ้ามี)
