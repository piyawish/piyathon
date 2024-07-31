import sys
import os
from piyathon_translator import PiyathonTranslator


def print_usage():
    print("Usage: python p2p.py <source_file> <destination_file>")
    print("Source and destination files must have different extensions (.py or .pi)")


def main():
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)

    source_file = sys.argv[1]
    destination_file = sys.argv[2]

    source_ext = os.path.splitext(source_file)[1]
    dest_ext = os.path.splitext(destination_file)[1]

    if source_ext == dest_ext:
        print(
            "Error: Source and destination files must have different extensions (.py or .pi)"
        )
        print_usage()
        sys.exit(1)

    if source_ext not in [".py", ".pi"] or dest_ext not in [".py", ".pi"]:
        print("Error: Both files must have either .py or .pi extensions")
        print_usage()
        sys.exit(1)

    try:
        with open(source_file, "r", encoding="utf-8") as file:
            source_code = file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{source_file}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Unable to read input file '{source_file}'.")
        sys.exit(1)

    translator = PiyathonTranslator()

    if source_ext == ".py" and dest_ext == ".pi":
        translated_code = translator.transform_to_thai(source_code)
        translation_type = "Python to Piyathon"
    elif source_ext == ".pi" and dest_ext == ".py":
        translated_code = translator.transform_to_python(source_code)
        translation_type = "Piyathon to Python"
    else:
        print("Error: Invalid file extension combination")
        print_usage()
        sys.exit(1)

    if translated_code is None:
        if source_ext == ".py":
            print("Translation aborted due to syntax errors in the Python input file.")
        else:
            print("Translation aborted due to errors in the Piyathon input file.")
        sys.exit(1)

    try:
        with open(destination_file, "w", encoding="utf-8") as file:
            file.write(translated_code)
        print(f"{translation_type} translation completed.")
        print(f"Translated code has been written to '{destination_file}'.")
    except IOError:
        print(f"Error: Unable to write to output file '{destination_file}'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
