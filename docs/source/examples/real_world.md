# การใช้งานจริง

```{eval-rst}
.. meta::
  :title: ตัวอย่างการเขียนโค้ดกับภาษาปิยะธอน - ภาษา Python คำสั่งภาษาไทยจากตัวอย่างจริง
  :description: เรียนรู้การเขียนโค้ดภาษาปิยะธอนผ่านตัวอย่างการใช้งานในสถานการณ์จริง เหมาะสำหรับผู้เริ่มต้นเรียน Python ที่ต้องการฝึกทักษะการเขียนโปรแกรม Basic Python Coding
```

ตัวอย่างการใช้งานภาษาปิยะธอนในสถานการณ์จริง

## การวิเคราะห์ข้อมูล

### วิเคราะห์ข้อมูลจากไฟล์ CSV

```piyathon
นำเข้า pandas เป็น พด
นำเข้า matplotlib.pyplot เป็น พล

นิยาม วิเคราะห์ยอดขาย(ไฟล์):
    # อ่านข้อมูล
    ข้อมูล = พด.read_csv(ไฟล์)

    # คำนวณสถิติ
    ยอดรวม = ข้อมูล['ยอดขาย'].sum()
    ค่าเฉลี่ย = ข้อมูล['ยอดขาย'].mean()
    สูงสุด = ข้อมูล['ยอดขาย'].max()

    # สร้างกราฟ
    ข้อมูล.plot(x='วันที่', y='ยอดขาย')
    พล.title('ยอดขายรายวัน')
    พล.show()

    คืนค่า {
        'ยอดรวม': ยอดรวม,
        'ค่าเฉลี่ยต่อวัน': ค่าเฉลี่ย,
        'ยอดขายสูงสุด': สูงสุด
    }
```

### แปลงและทำความสะอาดข้อมูล

```piyathon
นิยาม ทำความสะอาดข้อมูล(ดีเอฟ):
    # แทนที่ค่าว่าง
    ดีเอฟ = ดีเอฟ.fillna({
        'ราคา': 0,
        'ชื่อ': 'ไม่ระบุ'
    })

    # ลบแถวซ้ำ
    ดีเอฟ = ดีเอฟ.drop_duplicates()

    # แปลงประเภทข้อมูล
    ดีเอฟ['วันที่'] = พด.to_datetime(ดีเอฟ['วันที่'])
    ดีเอฟ['ราคา'] = ดีเอฟ['ราคา'].astype(float)

    คืนค่า ดีเอฟ
```

## เว็บแอปพลิเคชัน

### เว็บเซิร์ฟเวอร์อย่างง่าย

```piyathon
จาก flask นำเข้า Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/คำนวณ', methods=['POST'])
นิยาม คำนวณ():
    ข้อมูล = request.get_json()

    ลอง:
        ผลลัพธ์ = ประมวลผล(ข้อมูล)
        คืนค่า jsonify({'ผลลัพธ์': ผลลัพธ์}), 200
    ยกเว้น Exception เป็น e:
        คืนค่า jsonify({'ข้อผิดพลาด': str(e)}), 400

นิยาม ประมวลผล(ข้อมูล):
    # โค้ดสำหรับประมวลผลข้อมูล
    ผ่าน

ถ้า __ชื่อ__ == '__main__':
    app.run(debug=จริง)
```

### บอทไลน์อย่างง่าย

```piyathon
จาก linebot นำเข้า LineBotApi, WebhookHandler
จาก linebot.models นำเข้า MessageEvent, TextMessage, TextSendMessage

bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

@handler.add(MessageEvent, message=TextMessage)
นิยาม จัดการข้อความ(event):
    ข้อความ = event.message.text
    คำตอบ = ประมวลผลข้อความ(ข้อความ)

    bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=คำตอบ)
    )

นิยาม ประมวลผลข้อความ(ข้อความ):
    # โค้ดสำหรับประมวลผลข้อความ
    ผ่าน
```

## เครื่องมือ CLI

### เครื่องมือจัดการไฟล์

```piyathon
จาก typer นำเข้า Typer
จาก pathlib นำเข้า Path

app = Typer()

@app.command()
นิยาม เรียงไฟล์(โฟลเดอร์: str = '.', นามสกุล: str = None):
    """เรียงไฟล์ในโฟลเดอร์ตามนามสกุล"""
    พาธ = Path(โฟลเดอร์)

    สำหรับ ไฟล์ ใน พาธ.iterdir():
        ถ้า ไฟล์.is_file():
            ถ้า นามสกุล คือ ไม่มีค่า หรือ ไฟล์.suffix == f'.{นามสกุล}':
                โฟลเดอร์_ใหม่ = พาธ / ไฟล์.suffix[1:]
                โฟลเดอร์_ใหม่.mkdir(exist_ok=จริง)
                ไฟล์.rename(โฟลเดอร์_ใหม่ / ไฟล์.name)

ถ้า __ชื่อ__ == '__main__':
    app()
```

### เครื่องมือสร้างรายงาน

```piyathon
จาก jinja2 นำเข้า Template
จาก datetime นำเข้า datetime

นิยาม สร้างรายงาน(ข้อมูล, เทมเพลต):
    """สร้างรายงาน HTML จากข้อมูลและเทมเพลต"""
    ด้วย เปิด(เทมเพลต, 'r', encoding='utf-8') เป็น ไฟล์:
        template = Template(ไฟล์.read())

    เนื้อหา = template.render(
        ข้อมูล=ข้อมูล,
        วันที่=datetime.now().strftime('%Y-%m-%d')
    )

    ด้วย เปิด('รายงาน.html', 'w', encoding='utf-8') เป็น ไฟล์:
        ไฟล์.write(เนื้อหา)

# ตัวอย่างการใช้งาน
ข้อมูล = {
    'หัวข้อ': 'รายงานประจำเดือน',
    'รายการ': [
        {'ชื่อ': 'สินค้า A', 'จำนวน': 100},
        {'ชื่อ': 'สินค้า B', 'จำนวน': 150}
    ]
}

สร้างรายงาน(ข้อมูล, 'เทมเพลต.html')
```

## การทดสอบและ CI/CD

### การทดสอบอัตโนมัติ

```piyathon
จาก unittest นำเข้า TestCase
จาก myapp นำเข้า คำนวณราคา

ชั้น ทดสอบการคำนวณ(TestCase):
    นิยาม test_คำนวณปกติ(ตัว):
        ผลลัพธ์ = คำนวณราคา(100, 7)
        ตัว.assertEqual(ผลลัพธ์, 107)

    นิยาม test_คำนวณลดราคา(ตัว):
        ผลลัพธ์ = คำนวณราคา(100, 7, ส่วนลด=10)
        ตัว.assertEqual(ผลลัพธ์, 96.3)

    นิยาม test_ข้อผิดพลาด(ตัว):
        ด้วย ตัว.assertRaises(ValueError):
            คำนวณราคา(-100, 7)
```

<!--
### การรัน GitHub Actions

```yaml
name: ทดสอบและ Deploy

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: ตั้งค่า Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: ติดตั้ง Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: รันเทสต์
      run: |
        python -m pytest tests/
```
-->

## การใช้งาน

1. **วิเคราะห์ข้อมูลขาย**

```piyathon
ข้อมูล = วิเคราะห์ยอดขาย('ยอดขาย.csv')
พิมพ์(f"ยอดขายรวม: {ข้อมูล['ยอดรวม']:,.2f} บาท")
```

1. **รันเว็บเซิร์ฟเวอร์**

```bash
piyathon app.pi
```

1. **ใช้เครื่องมือเรียงไฟล์**

```bash
piyathon sort_files.pi --โฟลเดอร์="เอกสาร" --นามสกุล="pdf"
```
