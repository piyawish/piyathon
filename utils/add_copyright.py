# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import os
import sys

COPYRIGHT_NOTE = """# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License
"""


def add_copyright_note_to_file(file_path):
    with open(file_path, "r+", encoding="utf-8") as file:
        content = file.read()
        if COPYRIGHT_NOTE not in content:
            file.seek(0, 0)
            file.write(COPYRIGHT_NOTE + "\n" + content)


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                add_copyright_note_to_file(file_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_copyright.py <directory>")
    else:
        directory = sys.argv[1]
        if os.path.isdir(directory):
            process_directory(directory)
        else:
            print(f"Error: {directory} is not a valid directory")
