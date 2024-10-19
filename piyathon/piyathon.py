# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import sys
import os
import argparse
from .piyathon_translator import PiyathonTranslator
from . import __version__


def parse_arguments():
    parser = argparse.ArgumentParser(
        description=f"Piyathon {__version__}\n"
        "Copyright (c) 2024, Piyawish Piyawat\n"
        "Licensed under the MIT License",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("source_file", help="Piyathon source file (.pi)")
    parser.add_argument(
        "-v", "--version", action="version", version=f"Piyathon {__version__}"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    source_file = args.source_file

    if not source_file.endswith(".pi"):
        print("Error: The source file must have a .pi extension")
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
    python_code = translator.piyathon_to_python(piyathon_code)

    if python_code is None:
        print("Execution aborted due to errors in the Piyathon input file.")
        sys.exit(1)

    # Get the absolute path to the current file's directory and append 'Lib'
    lib_path = os.path.join(os.path.dirname(__file__), "Lib")

    # Inject the absolute path into sys.path
    sys.path.insert(0, lib_path)

    # Create a new namespace for execution
    namespace = {"__name__": "__main__"}

    try:
        exec(python_code, namespace)  # pylint: disable=exec-used
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error during execution: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
