# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""สคริปต์สำหรับสร้างโมดูล Python ที่แปลภาษาแล้ว

ยูทิลิตี้นี้สร้างโมดูลห่อหุ้ม Python ที่ให้การเชื่อมต่อภาษาไทย
สำหรับโมดูลมาตรฐานของ Python โดยใช้การแมปการแปลภาษาเพื่อสร้างโมดูล
ที่เปิดเผยทั้งชื่อภาษาไทยและภาษาอังกฤษสำหรับคลาส เมธอด ฟังก์ชัน และค่าคงที่

Dependencies:
    - os: สำหรับการทำงานกับไดเรกทอรี
    - translated_list: มีการแมปการแปลภาษาไทย-อังกฤษ

โครงสร้างผลลัพธ์:
    สร้างโมดูล Python ในไดเรกทอรี piyathon/Lib ที่มี:
    - การแปลภาษาไทยของแอตทริบิวต์สาธารณะทั้งหมดของโมดูล
    - รักษาชื่อภาษาอังกฤษเดิมไว้
    - สร้างรายการ __all__ ที่รวมทั้งชื่อภาษาไทยและภาษาอังกฤษ
    - ข้อมูลลิขสิทธิ์และใบอนุญาต
"""

import os

# Import the translated_list module
import translated_list

# Path to the output directory
output_dir = "../src/piyathon/Lib"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Template for the generated module files
module_template = """# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

# Generated module file. Do not edit directly.

import {original_module}


# Classes
{classes}
# Methods
{methods}

# Functions
{functions}

# Constants
{constants}


# Get all public names from the module
eng_names = [name for name in dir({original_module}) if not name.startswith("_")]

# Get all names defined in this file (our Thai translations)
thai_names = [name for name in locals() if not name.startswith("_")]

# Combine both sets of names, removing duplicates
__all__ = list(set(eng_names + thai_names))
"""


def generate_classes(classes, original_module):
    """Generate class translation assignments.

    Args:
        classes (dict): Dictionary mapping Thai class names to English class names
        original_module (str): Name of the original Python module

    Returns:
        str: Python code defining class translations

    Example:
        >>> generate_classes({"สุ่ม": "Random"}, "random")
        'สุ่ม = random.Random'
    """
    return "\n".join(
        [
            f"{thai_name} = {original_module}.{eng_name}"
            for thai_name, eng_name in classes.items()
        ]
    )


def generate_methods(methods, original_module):
    """Generate method translation assignments.

    Args:
        methods (dict): Dictionary mapping Thai method names to English method names
        original_module (str): Name of the original Python module

    Returns:
        str: Python code defining method translations

    Example:
        >>> generate_methods({"เลือก": "choice"}, "random")
        'เลือก = random.choice'
    """
    return "\n".join(
        [
            f"{thai_name} = {original_module}.{eng_name}"
            for eng_name, thai_name in methods.items()
            if not eng_name.startswith("_")
        ]
    )


generate_functions = generate_methods


def generate_constants(constants, original_module):
    """Generate constant translation assignments.

    Args:
        constants (dict): Dictionary mapping Thai constant names to English constant names
        original_module (str): Name of the original Python module

    Returns:
        str: Python code defining constant translations

    Example:
        >>> generate_constants({"พาย": "PI"}, "math")
        'พาย = math.PI'
    """
    return "\n".join(
        [
            f"{thai_name} = {original_module}.{eng_name}"
            for eng_name, thai_name in constants.items()
            if not eng_name.startswith("_")
        ]
    )


# Get the list of module names from translated_list
module_names = [name for name in dir(translated_list) if not name.startswith("__")]

# Generate module files
for original_module in module_names:
    module_info = getattr(translated_list, original_module)
    module_name = module_info["__name__"]
    classes = generate_classes(module_info.get("classes", {}), original_module)
    methods = generate_methods(module_info.get("methods", {}), original_module)
    functions = generate_functions(module_info.get("functions", {}), original_module)
    constants = generate_constants(module_info.get("constants", {}), original_module)

    # Create the module content
    module_content = module_template.format(
        original_module=original_module,
        classes=classes,
        methods=methods,
        functions=functions,
        constants=constants,
    )

    # Write the module file
    module_file_path = os.path.join(output_dir, f"{module_name}.py")
    with open(module_file_path, "w", encoding="utf-8") as module_file:
        module_file.write(module_content)

print("Module files generated successfully.")
