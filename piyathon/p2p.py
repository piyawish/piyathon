# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import sys
import os
import argparse
from .piyathon_translator import PiyathonTranslator


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Translate between Python and Piyathon files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("source_file", help="Source file (.py or .pi)")
    parser.add_argument("destination_file", help="Destination file (.py or .pi)")
    return parser.parse_args()


def validate_extensions(source_file, destination_file):
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
    try:
        with open(destination_file, "w", encoding="utf-8") as file:
            file.write(translated_code)
        print(f"{translation_type} translation completed.")
        print(f"Translated code has been written to '{destination_file}'.")
    except IOError:
        print(f"Error: Unable to write to output file '{destination_file}'.")
        sys.exit(1)


def main():
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
