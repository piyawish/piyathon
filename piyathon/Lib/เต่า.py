# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

# Generated module file. Do not edit directly.

"""
Piyathon Turtle Graphics Module (เต่า)

This module provides Thai language bindings for Python's turtle graphics module,
offering a complete set of turtle graphics functionality for educational and
creative programming.

Core Components:
    Classes:
        - เต่า: Main turtle graphics class (maps to turtle.Turtle)
        - หน้าจอเต่า: Turtle screen management (maps to turtle.TurtleScreen)
        - ผ้าใบ: Drawing canvas (maps to turtle.Canvas)
        - ปากกา: Drawing pen (maps to turtle.Pen)
        - Various supporting classes for shapes, navigation, and error handling

    Functions:
        - Movement: เดินหน้า, ถอยหลัง, ซ้าย, ขวา, etc.
        - Drawing: วงกลม, จุด, เขียน, etc.
        - Pen control: ลงปากกา, ยกปากกา, สีปากกา, etc.
        - Screen management: หน้าจอ, ล้างหน้าจอ, อัปเดต, etc.

Key Features:
    - Complete turtle graphics functionality in Thai
    - Support for both simple and complex drawing operations
    - Event handling and animation capabilities
    - Screen and window management utilities

Integration Points:
    - Compatible with all standard turtle module features
    - Can be used for educational programming
    - Supports interactive graphics applications

Usage Examples:
    >>> from piyathon.Lib.เต่า import เต่า
    >>> t = เต่า()
    >>> t.เดินหน้า(100)
    >>> t.ขวา(90)
    >>> t.วงกลม(50)

Known Limitations:
    - Performance depends on the underlying Tkinter implementation
    - Some complex animations may require manual screen updates
    - Limited to 2D graphics operations
"""

import turtle


# Classes
class ผ้าใบ(turtle.Canvas):
    pass


class ปากกา(turtle.Pen):
    pass


class ปากกาดิบ(turtle.RawPen):
    pass


class เต่าดิบ(turtle.RawTurtle):
    pass


class ผ้าใบเลื่อนได้(turtle.ScrolledCanvas):
    pass


class รูปร่าง(turtle.Shape):
    pass


class ที_นำทาง(turtle.TNavigator):
    pass


class ที_ปากกา(turtle.TPen):
    pass


class ที_บัฟเฟอร์(turtle.Tbuffer):
    pass


class ตัวยุติ(turtle.Terminator):
    pass


class เต่า(turtle.Turtle):
    pass


class ข้อผิดพลาดกราฟิกเต่า(turtle.TurtleGraphicsError):
    pass


class หน้าจอเต่า(turtle.TurtleScreen):
    pass


class ฐานหน้าจอเต่า(turtle.TurtleScreenBase):
    pass


class เวคเตอร์สองมิติ(turtle.Vec2D):
    pass


# Methods


# Functions
หน้าจอ = turtle.Screen
เพิ่มรูปร่าง = turtle.addshape
กลับ = turtle.back
ถอยหลัง = turtle.backward
เริ่มเติม = turtle.begin_fill
เริ่มรูปหลายเหลี่ยม = turtle.begin_poly
สีพื้นหลัง = turtle.bgcolor
ภาพพื้นหลัง = turtle.bgpic
ถอยหลัง = turtle.bk
ลาก่อน = turtle.bye
วงกลม = turtle.circle
ล้าง = turtle.clear
ล้างหน้าจอ = turtle.clearscreen
ล้างตราประทับ = turtle.clearstamp
ล้างตราประทับทั้งหมด = turtle.clearstamps
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
สิ้นสุดการเติม = turtle.end_fill
สิ้นสุดรูปหลายเหลี่ยม = turtle.end_poly
ออกเมื่อคลิก = turtle.exitonclick
เดินหน้า = turtle.fd
สีเติม = turtle.fillcolor
กำลังเติม = turtle.filling
เดินหน้า = turtle.forward
รับรูปหลายเหลี่ยม = turtle.get_poly
รับรูปหลายเหลี่ยมของรูปร่าง = turtle.get_shapepoly
รับผ้าใบ = turtle.getcanvas
รับรายการพารามิเตอร์วิธีการ = turtle.getmethparlist
รับปากกา = turtle.getpen
รับหน้าจอ = turtle.getscreen
รับรูปร่าง = turtle.getshapes
รับเต่า = turtle.getturtle
ไปที่ = turtle.goto
ทิศทาง = turtle.heading
ซ่อนเต่า = turtle.hideturtle
บ้าน = turtle.home
ซ่อนเต่า = turtle.ht
ลงหรือไม่ = turtle.isdown
เป็นไฟล์หรือไม่ = turtle.isfile
มองเห็นหรือไม่ = turtle.isvisible
เข้าร่วม = turtle.join
ซ้าย = turtle.left
ฟัง = turtle.listen
ซ้าย = turtle.lt
ลูปหลัก = turtle.mainloop
โหมด = turtle.mode
ป้อนตัวเลข = turtle.numinput
เมื่อคลิก = turtle.onclick
เมื่อลาก = turtle.ondrag
เมื่อกดปุ่ม = turtle.onkey
เมื่อกดปุ่ม = turtle.onkeypress
เมื่อปล่อยปุ่ม = turtle.onkeyrelease
เมื่อปล่อย = turtle.onrelease
เมื่อคลิกหน้าจอ = turtle.onscreenclick
เมื่อถึงเวลา = turtle.ontimer
ลงปากกา = turtle.pd
ปากกา = turtle.pen
สีปากกา = turtle.pencolor
ลงปากกา = turtle.pendown
ขนาดปากกา = turtle.pensize
ยกปากกา = turtle.penup
ตำแหน่ง = turtle.pos
ตำแหน่ง = turtle.position
ยกปากกา = turtle.pu
เรเดียน = turtle.radians
อ่านสตริงเอกสาร = turtle.read_docstrings
อ่านการกำหนดค่า = turtle.readconfig
ลงทะเบียนรูปร่าง = turtle.register_shape
รีเซ็ต = turtle.reset
รีเซ็ตหน้าจอ = turtle.resetscreen
โหมดปรับขนาด = turtle.resizemode
ขวา = turtle.right
ขวา = turtle.rt
ขนาดหน้าจอ = turtle.screensize
ตั้งทิศทาง = turtle.seth
ตั้งทิศทาง = turtle.setheading
ตั้งตำแหน่ง = turtle.setpos
ตั้งตำแหน่ง = turtle.setposition
ตั้งมุมเอียง = turtle.settiltangle
ตั้งบัฟเฟอร์เลิกทำ = turtle.setundobuffer
ตั้งค่า = turtle.setup
ตั้งค่าพิกัดโลก = turtle.setworldcoordinates
ตั้งค่า_x = turtle.setx
ตั้งค่า_y = turtle.sety
รูปร่าง = turtle.shape
ขนาดรูปร่าง = turtle.shapesize
แปลงรูปร่าง = turtle.shapetransform
ปัจจัยเฉือน = turtle.shearfactor
แสดงเต่า = turtle.showturtle
ความเร็ว = turtle.speed
แยก = turtle.split
แสดงเต่า = turtle.st
ประทับตรา = turtle.stamp
เคลื่อนย้าย = turtle.teleport
ป้อนข้อความ = turtle.textinput
เอียง = turtle.tilt
มุมเอียง = turtle.tiltangle
ชื่อเรื่อง = turtle.title
ไปทาง = turtle.towards
ตัวติดตาม = turtle.tracer
เต่าทั้งหมด = turtle.turtles
ขนาดเต่า = turtle.turtlesize
เลิกทำ = turtle.undo
รายการบัฟเฟอร์เลิกทำ = turtle.undobufferentries
ขึ้น = turtle.up
อัปเดต = turtle.update
ความกว้าง = turtle.width
ความสูงหน้าต่าง = turtle.window_height
ความกว้างหน้าต่าง = turtle.window_width
เขียน = turtle.write
เขียนพจนานุกรมสตริงเอกสาร = turtle.write_docstringdict
พิกัด_x = turtle.xcor
พิกัด_y = turtle.ycor

# Constants
ทีเค = turtle.TK


# Get all public names from the module
eng_names = [name for name in dir(turtle) if not name.startswith("_")]

# Get all names defined in this file (our Thai translations)
thai_names = [name for name in locals() if not name.startswith("_")]

# Combine both sets of names, removing duplicates
__all__ = list(set(eng_names + thai_names))
