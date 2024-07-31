import sys
import os
from piyathon_translator import PiyathonTranslator


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python py2pi.py <input_python_file> [output_piyathon_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = (
        sys.argv[2] if len(sys.argv) == 3 else os.path.splitext(input_file)[0] + ".pi"
    )

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            python_code = file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Unable to read input file '{input_file}'.")
        sys.exit(1)

    translator = PiyathonTranslator()
    piyathon_code = translator.transform_to_thai(python_code)

    if piyathon_code is None:
        print("Translation aborted due to syntax errors in the input file.")
        sys.exit(1)

    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(piyathon_code)
        print(f"Piyathon code has been written to '{output_file}'.")
    except IOError:
        print(f"Error: Unable to write to output file '{output_file}'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
