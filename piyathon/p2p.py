# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
Piyathon Code Translation Command Line Tool

This module provides a command-line interface for bidirectional translation
between Python (.py) and Piyathon (.pi) source files. It serves as a standalone
tool for code conversion without execution.

Core Functionality:
    - Converts Python source files to Piyathon format
    - Converts Piyathon source files to Python format
    - Validates file extensions and handles errors
    - Preserves code structure and formatting during translation

Dependencies:
    - sys: For system-level operations and exit handling
    - os: For path manipulation and file operations
    - argparse: For command-line argument parsing
    - piyathon_translator: For bidirectional code translation

Integration Points:
    - Works with PiyathonTranslator for code conversion
    - Interfaces with the file system for reading/writing code
    - Can be used as part of a build/translation pipeline

Usage Examples:
    # Convert Python to Piyathon
    $ python -m piyathon.p2p input.py output.pi

    # Convert Piyathon to Python
    $ python -m piyathon.p2p input.pi output.py

Known Limitations:
    - Processes one file at a time
    - No support for directory-wide translation
    - Basic error handling for file operations
"""

import sys
import os
import argparse
from .piyathon_translator import PiyathonTranslator


def parse_arguments():
    """
    Parse and validate command-line arguments for file translation.

    Returns:
        argparse.Namespace: Parsed command-line arguments containing:
            - source_file (str): Path to the source file (.py or .pi)
            - destination_file (str): Path to the output file (.pi or .py)

    Example:
        >>> args = parse_arguments()
        >>> print(args.source_file, args.destination_file)
        'input.py' 'output.pi'
    """
    parser = argparse.ArgumentParser(
        description="Translate between Python and Piyathon files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("source_file", help="Source file (.py or .pi)")
    parser.add_argument("destination_file", help="Destination file (.py or .pi)")
    return parser.parse_args()


def validate_extensions(source_file, destination_file):
    """
    Validate file extensions for source and destination files.

    Ensures that:
    1. Source and destination have different extensions
    2. Both files use either .py or .pi extensions
    3. The extension combination is valid for translation

    Args:
        source_file (str): Path to the source file
        destination_file (str): Path to the destination file

    Side Effects:
        - Exits with status code 1 if validation fails
        - Prints error message to stderr

    Example:
        >>> validate_extensions("test.py", "test.pi")  # Valid
        >>> validate_extensions("test.py", "test.py")  # Invalid, exits
    """
    source_ext = os.path.splitext(source_file)[1]
    dest_ext = os.path.splitext(destination_file)[1]

    if source_ext == dest_ext:
        print(
            "Error: Source and destination files must have different extensions (.py or .pi)"
        )
        sys.exit(1)

    if source_ext not in [".py", ".pi"] or dest_ext not in [".py", ".pi"]:
        print("Error: Both files must have either .py or .pi extensions")
        sys.exit(1)


def read_source_file(source_file):
    """
    Read and return the contents of the source file.

    Args:
        source_file (str): Path to the source file

    Returns:
        str: Contents of the source file

    Raises:
        SystemExit: If file cannot be read or doesn't exist

    Example:
        >>> code = read_source_file("example.py")
        >>> print(len(code))  # Number of characters read
    """
    try:
        with open(source_file, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{source_file}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Unable to read input file '{source_file}'.")
        sys.exit(1)


def translate_code(source_code, source_ext, dest_ext):
    """
    Translate code between Python and Piyathon formats.

    Args:
        source_code (str): The source code to translate
        source_ext (str): Source file extension (".py" or ".pi")
        dest_ext (str): Destination file extension (".pi" or ".py")

    Returns:
        tuple: (translated_code: str, translation_type: str)
            - translated_code: The translated source code
            - translation_type: Description of the translation direction

    Side Effects:
        - Exits with status code 1 if translation fails
        - Prints error message to stderr

    Example:
        >>> code, type = translate_code("def main():", ".py", ".pi")
        >>> print(type)
        'Python to Piyathon'
    """
    translator = PiyathonTranslator()

    if source_ext == ".py" and dest_ext == ".pi":
        translated_code = translator.python_to_piyathon(source_code)
        translation_type = "Python to Piyathon"
    elif source_ext == ".pi" and dest_ext == ".py":
        translated_code = translator.piyathon_to_python(source_code)
        translation_type = "Piyathon to Python"
    else:
        print("Error: Invalid file extension combination")
        sys.exit(1)

    if translated_code is None:
        if source_ext == ".py":
            print("Translation aborted due to syntax errors in the Python input file.")
        else:
            print("Translation aborted due to errors in the Piyathon input file.")
        sys.exit(1)

    return translated_code, translation_type


def write_translated_code(destination_file, translated_code, translation_type):
    """
    Write translated code to the destination file.

    Args:
        destination_file (str): Path to the output file
        translated_code (str): The translated source code
        translation_type (str): Description of the translation performed

    Side Effects:
        - Creates or overwrites the destination file
        - Prints success message to stdout
        - Exits with status code 1 if write fails

    Example:
        >>> write_translated_code("output.pi", "คำสั่ง หลัก():", "Python to Piyathon")
        Piyathon to Python translation completed.
        Translated code has been written to 'output.pi'.
    """
    try:
        with open(destination_file, "w", encoding="utf-8") as file:
            file.write(translated_code)
        print(f"{translation_type} translation completed.")
        print(f"Translated code has been written to '{destination_file}'.")
    except IOError:
        print(f"Error: Unable to write to output file '{destination_file}'.")
        sys.exit(1)


def main():
    """
    Main entry point for the translation tool.

    This function orchestrates the entire translation process:
    1. Parses command-line arguments
    2. Validates file extensions
    3. Reads the source file
    4. Performs the translation
    5. Writes the result to the destination file

    Side Effects:
        - File system operations (read/write)
        - Stdout/stderr output for status and errors
        - Process exit codes for success/failure

    Example:
        $ python -m piyathon.p2p input.py output.pi
    """
    args = parse_arguments()
    validate_extensions(args.source_file, args.destination_file)
    source_code = read_source_file(args.source_file)
    source_ext = os.path.splitext(args.source_file)[1]
    dest_ext = os.path.splitext(args.destination_file)[1]
    translated_code, translation_type = translate_code(
        source_code, source_ext, dest_ext
    )
    write_translated_code(args.destination_file, translated_code, translation_type)


if __name__ == "__main__":
    main()
