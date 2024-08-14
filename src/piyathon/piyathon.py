# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import sys
from .piyathon_translator import PiyathonTranslator
from . import __version__


def print_usage():
    print(
        f"""
Piyathon {__version__}
Copyright (c) 2024, Piyawish Piyawat
Licensed under the MIT License

Usage: python piyathon.py <piyathon_source_file>
"""
    )


def main():
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    source_file = sys.argv[1]

    if not source_file.endswith(".pi"):
        print("Error: The source file must have a .pi extension")
        print_usage()
        sys.exit(1)

    try:
        with open(source_file, "r", encoding="utf-8") as file:
            piyathon_code = file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{source_file}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Unable to read input file '{source_file}'.")
        sys.exit(1)

    translator = PiyathonTranslator()
    python_code = translator.transform_to_python(piyathon_code)

    if python_code is None:
        print("Execution aborted due to errors in the Piyathon input file.")
        sys.exit(1)

    # Create a new namespace for execution
    namespace = {"__name__": "__main__"}

    try:
        exec(python_code, namespace)  # pylint: disable=exec-used
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error during execution: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
