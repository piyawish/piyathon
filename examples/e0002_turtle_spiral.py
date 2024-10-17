# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import turtle
import random

# ตั้งค่าหน้าต่างและเต่า
หน้าต่าง = turtle.Screen()
หน้าต่าง.title("ปิยะทอน: วาดเกลียวสี")
ปากกา = turtle.Turtle()
ปากกา.speed(0)  # ความเร็วสูงสุด


# ฟังก์ชันสำหรับสุ่มสี
def สุ่มสี():
    return (
        random.randint(0, 255) / 255,
        random.randint(0, 255) / 255,
        random.randint(0, 255) / 255,
    )


# วาดเกลียวสี
for ด in range(100):
    ปากกา.color(สุ่มสี())
    ปากกา.forward(ด * 2)
    ปากกา.right(60)
    ปากกา.pensize(ด / 20)

ปากกา.hideturtle()  # ซ่อนเต่าหลังจากวาดเสร็จ

# รอให้ผู้ใช้คลิกหน้าต่างเพื่อปิด
หน้าต่าง.exitonclick()
