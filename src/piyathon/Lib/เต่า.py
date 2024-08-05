# เต่า/__init__.py

import turtle


# Classes
class ผืนผ้าใบ(turtle.Canvas):
    pass


class ปากกา(turtle.Pen):
    pass


class ปากกาดิบ(turtle.RawPen):
    pass


class เต่าดิบ(turtle.RawTurtle):
    pass


class ผืนผ้าใบเลื่อน(turtle.ScrolledCanvas):
    pass


class รูปร่าง(turtle.Shape):
    pass


class ตัวนำทาง(turtle.TNavigator):
    pass


class ปากกาที(turtle.TPen):
    pass


class บัฟเฟอร์ที(turtle.Tbuffer):
    pass


class ตัวยุติ(turtle.Terminator):
    pass


class เต่า(turtle.Turtle):
    pass


class ข้อผิดพลาดกราฟิกเต่า(turtle.TurtleGraphicsError):
    pass


class จอเต่า(turtle.TurtleScreen):
    pass


class ฐานจอเต่า(turtle.TurtleScreenBase):
    pass


class เวกเตอร์2มิติ(turtle.Vec2D):
    pass


# class รูท(turtle._Root):
#     pass


# class จอ(turtle._Screen):
#     pass


# class รูปภาพเต่า(turtle._TurtleImage):
#     pass


# Functions
จอ = turtle.Screen
# __ส่งต่อวิธีการ = turtle.__forwardmethods
# __พจนานุกรมวิธีการ = turtle.__methodDict
# __วิธีการ = turtle.__methods
# _สร้าง_ฟังก์ชันส่วนกลาง = turtle._make_global_funcs
# _จอ_แก้ไขเอกสาร = turtle._screen_docrevise
# _เต่า_แก้ไขเอกสาร = turtle._turtle_docrevise
เพิ่มรูปร่าง = turtle.addshape
ถอยหลัง = turtle.back
ถอยหลัง = turtle.backward
เริ่มระบายสี = turtle.begin_fill
เริ่มพหุเหลี่ยม = turtle.begin_poly
สีพื้นหลัง = turtle.bgcolor
รูปพื้นหลัง = turtle.bgpic
ถอย = turtle.bk
ลาก่อน = turtle.bye
วงกลม = turtle.circle
ล้าง = turtle.clear
ล้างจอ = turtle.clearscreen
ลบประทับ = turtle.clearstamp
ลบประทับทั้งหมด = turtle.clearstamps
โคลน = turtle.clone
สี = turtle.color
โหมดสี = turtle.colormode
พจนานุกรมการกำหนดค่า = turtle.config_dict
คัดลอกลึก = turtle.deepcopy
องศา = turtle.degrees
หน่วงเวลา = turtle.delay
ระยะทาง = turtle.distance
เสร็จสิ้น = turtle.done
จุด = turtle.dot
ลง = turtle.down
จบระบายสี = turtle.end_fill
จบพหุเหลี่ยม = turtle.end_poly
ออกเมื่อคลิก = turtle.exitonclick
ไปข้างหน้า = turtle.fd
สีพื้น = turtle.fillcolor
กำลังระบายสี = turtle.filling
ไปข้างหน้า = turtle.forward
รับพหุเหลี่ยม = turtle.get_poly
รับรูปร่างพหุเหลี่ยม = turtle.get_shapepoly
รับผืนผ้าใบ = turtle.getcanvas
รับรายการพารามิเตอร์วิธีการ = turtle.getmethparlist
รับปากกา = turtle.getpen
รับจอ = turtle.getscreen
รับรูปร่าง = turtle.getshapes
รับเต่า = turtle.getturtle
ไปยัง = turtle.goto
ทิศทาง = turtle.heading
ซ่อนเต่า = turtle.hideturtle
กลับบ้าน = turtle.home
ซ่อน = turtle.ht
ปากกาลง = turtle.isdown
เป็นไฟล์ = turtle.isfile
มองเห็น = turtle.isvisible
รวม = turtle.join
ซ้าย = turtle.left
ฟัง = turtle.listen
เลี้ยวซ้าย = turtle.lt
เมนหลัก = turtle.mainloop
โหมด = turtle.mode
ป้อนตัวเลข = turtle.numinput
เมื่อคลิก = turtle.onclick
เมื่อลาก = turtle.ondrag
เมื่อกดปุ่ม = turtle.onkey
เมื่อกดปุ่มค้าง = turtle.onkeypress
เมื่อปล่อยปุ่ม = turtle.onkeyrelease
เมื่อปล่อย = turtle.onrelease
เมื่อคลิกจอ = turtle.onscreenclick
เมื่อหมดเวลา = turtle.ontimer
วางปากกา = turtle.pd
ปากกา = turtle.pen
สีปากกา = turtle.pencolor
ปากกาลง = turtle.pendown
ขนาดปากกา = turtle.pensize
ยกปากกา = turtle.penup
ตำแหน่ง = turtle.pos
ตำแหน่ง = turtle.position
ยกปากกา = turtle.pu
เรเดียน = turtle.radians
อ่านเอกสาร = turtle.read_docstrings
อ่านการกำหนดค่า = turtle.readconfig
ลงทะเบียนรูปร่าง = turtle.register_shape
รีเซ็ต = turtle.reset
รีเซ็ตจอ = turtle.resetscreen
โหมดปรับขนาด = turtle.resizemode
ขวา = turtle.right
เลี้ยวขวา = turtle.rt
ขนาดจอ = turtle.screensize
กำหนดทิศทาง = turtle.seth
กำหนดทิศทาง = turtle.setheading
กำหนดตำแหน่ง = turtle.setpos
กำหนดตำแหน่ง = turtle.setposition
กำหนดมุมเอียง = turtle.settiltangle
กำหนดบัฟเฟอร์ย้อนกลับ = turtle.setundobuffer
ตั้งค่า = turtle.setup
ตั้งค่าพิกัดโลก = turtle.setworldcoordinates
กำหนดx = turtle.setx
กำหนดy = turtle.sety
รูปร่าง = turtle.shape
ขนาดรูปร่าง = turtle.shapesize
แปลงรูปร่าง = turtle.shapetransform
ปัจจัยเฉือน = turtle.shearfactor
แสดงเต่า = turtle.showturtle
ความเร็ว = turtle.speed
แยก = turtle.split
แสดง = turtle.st
ประทับ = turtle.stamp
เคลื่อนย้าย = turtle.teleport
ป้อนข้อความ = turtle.textinput
เอียง = turtle.tilt
มุมเอียง = turtle.tiltangle
ชื่อเรื่อง = turtle.title
ไปทาง = turtle.towards
ติดตาม = turtle.tracer
เต่าทั้งหมด = turtle.turtles
ขนาดเต่า = turtle.turtlesize
ย้อนกลับ = turtle.undo
รายการบัฟเฟอร์ย้อนกลับ = turtle.undobufferentries
ขึ้น = turtle.up
อัพเดท = turtle.update
ความกว้าง = turtle.width
ความสูงหน้าต่าง = turtle.window_height
ความกว้างหน้าต่าง = turtle.window_width
เขียน = turtle.write
เขียนพจนานุกรมเอกสาร = turtle.write_docstringdict
พิกัดx = turtle.xcor
พิกัดy = turtle.ycor

# Constants
TK = turtle.TK

# Get all public names from the turtle module
turtle_names = [name for name in dir(turtle) if not name.startswith("_")]

# Get all names defined in this file (our Thai translations)
thai_names = [name for name in locals() if not name.startswith("_")]

# Combine both sets of names, removing duplicates
__all__ = list(set(turtle_names + thai_names))
