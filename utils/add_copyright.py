# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""Script for adding copyright notices to Python files.

This utility script automatically adds copyright and license information to Python files
in a specified directory and its subdirectories. It ensures that each Python file
contains the standard copyright notice if it's not already present.

Dependencies:
    - os: For file system operations
    - sys: For command line arguments
"""

import os
import sys

COPYRIGHT_NOTE = """# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License
"""


def add_copyright_note_to_file(file_path):
    """Add copyright notice to a Python file if it doesn't already exist.

    Args:
        file_path (str): Path to the Python file to process

    Side Effects:
        - Modifies the target file by adding copyright notice at the beginning
        - Preserves existing file content after the copyright notice

    Example:
        >>> add_copyright_note_to_file("example.py")
    """
    with open(file_path, "r+", encoding="utf-8") as file:
        content = file.read()
        if COPYRIGHT_NOTE not in content:
            file.seek(0, 0)
            file.write(COPYRIGHT_NOTE + "\n" + content)


def process_directory(directory):
    """Recursively process all Python files in a directory.

    Walks through the directory tree and adds copyright notices to all Python files
    that don't already have them.

    Args:
        directory (str): Root directory path to start processing from

    Side Effects:
        - Modifies Python files in the directory tree by adding copyright notices

    Example:
        >>> process_directory("./src")
    """
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
