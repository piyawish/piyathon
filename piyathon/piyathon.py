# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
Piyathon Command Line Interface and Runtime Environment

This module serves as the main entry point for the Piyathon programming language,
providing command-line interface functionality and runtime execution environment
for Piyathon (.pi) source files.

Core Functionality:
    - Parses command line arguments for Piyathon source files
    - Reads and validates Piyathon source code
    - Translates Piyathon code to Python using PiyathonTranslator
    - Sets up runtime environment with custom library path
    - Executes translated Python code in an isolated namespace

Dependencies:
    - sys: For system-level operations and exit handling
    - os: For path manipulation and file operations
    - argparse: For command-line argument parsing
    - piyathon_translator: For Piyathon to Python code translation

Integration Points:
    - Integrates with PiyathonTranslator for code translation
    - Interfaces with custom Piyathon standard library in the Lib directory
    - Works with the command line for file input and execution

Known Limitations:
    - Only processes single .pi files (no module imports yet)
    - Executes in an isolated namespace with limited global scope
    - Error handling is basic with general exception catching
"""

import sys
import os
import argparse
from .piyathon_translator import PiyathonTranslator
from . import __version__


def parse_arguments():
    """
    Parse and validate command-line arguments for Piyathon execution.

    Returns:
        argparse.Namespace: Parsed command-line arguments containing:
            - source_file (str): Path to the Piyathon source file (.pi)
            - version (bool): Flag for version information display

    Example:
        >>> args = parse_arguments()
        >>> print(args.source_file)
        'example.pi'
    """
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
    """
    Main entry point for the Piyathon interpreter.

    This function orchestrates the entire Piyathon execution process:
    1. Parses command-line arguments
    2. Validates the source file extension
    3. Reads and processes the source file
    4. Translates Piyathon code to Python
    5. Sets up the runtime environment
    6. Executes the translated code

    Side Effects:
        - Modifies sys.path to include Piyathon standard library
        - Creates and populates a new execution namespace
        - Writes to stdout/stderr for error reporting

    Exit Codes:
        - 0: Successful execution
        - 1: Various error conditions (file not found, invalid extension, etc.)

    Example:
        $ python -m piyathon example.pi
    """
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
