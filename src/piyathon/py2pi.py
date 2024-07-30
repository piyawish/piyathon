import sys
import os
import tokenize
from io import StringIO
from keywords import PYTHON_TO_THAI


def handle_from_import(tokens, i, result):
    result.append(tokens[i]._replace(string=PYTHON_TO_THAI["from"]))
    i += 1
    while i < len(tokens) and tokens[i].string != "import":
        result.append(tokens[i])
        i += 1
    if i < len(tokens) and tokens[i].string == "import":
        result.append(tokens[i]._replace(string=PYTHON_TO_THAI["import"]))
    return i


def handle_else_elif(tokens, i, result):
    next_token = tokens[i + 1] if i + 1 < len(tokens) else None
    if next_token and next_token.type == tokenize.NAME and next_token.string == "if":
        result.append(tokens[i]._replace(string=PYTHON_TO_THAI["elif"]))
        i += 1  # Skip the 'if' in 'elif'
    else:
        result.append(tokens[i]._replace(string=PYTHON_TO_THAI["else"]))
    return i


def handle_for_in(tokens, i, result):
    result.append(tokens[i]._replace(string=PYTHON_TO_THAI["for"]))
    i += 1
    while i < len(tokens) and tokens[i].string != "in":
        result.append(tokens[i])
        i += 1
    if i < len(tokens) and tokens[i].string == "in":
        result.append(tokens[i]._replace(string=PYTHON_TO_THAI["in"]))
    return i


def transform_to_thai(code):
    tokens = list(tokenize.generate_tokens(StringIO(code).readline))
    result = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok.type == tokenize.NAME and tok.string in PYTHON_TO_THAI:
            if tok.string == "from":
                i = handle_from_import(tokens, i, result)
            elif tok.string == "else":
                i = handle_else_elif(tokens, i, result)
            elif tok.string == "for":
                i = handle_for_in(tokens, i, result)
            else:
                result.append(tok._replace(string=PYTHON_TO_THAI[tok.string]))
        else:
            result.append(tok)
        i += 1

    return tokenize.untokenize(result)


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

    piyathon_code = transform_to_thai(python_code)

    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(piyathon_code)
        print(f"Piyathon code has been written to '{output_file}'.")
    except IOError:
        print(f"Error: Unable to write to output file '{output_file}'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
