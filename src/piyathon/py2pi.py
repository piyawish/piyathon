import sys
import os
import ast
import tokenize
from io import StringIO
from keywords import PYTHON_TO_THAI

KEYWORD_NODE_TYPES = (
    ast.FunctionDef,
    ast.AsyncFunctionDef,
    ast.ClassDef,
    ast.For,
    ast.AsyncFor,
    ast.While,
    ast.If,
    ast.With,
    ast.AsyncWith,
    ast.Try,
    ast.ExceptHandler,
    ast.Return,
    ast.Yield,
    ast.YieldFrom,
    ast.Delete,
    ast.Assign,
    ast.AugAssign,
    ast.Import,
    ast.ImportFrom,
    ast.Global,
    ast.Nonlocal,
    ast.Assert,
    ast.Break,
    ast.Continue,
    ast.Pass,
    ast.Raise,
    ast.Lambda,
    ast.Await,
    ast.ListComp,
    ast.SetComp,
    ast.DictComp,
    ast.GeneratorExp,
)


def transform_to_thai(code):
    tokens = list(tokenize.generate_tokens(StringIO(code).readline))
    result = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok.type == tokenize.NAME and tok.string in PYTHON_TO_THAI:
            if tok.string == "from":
                # Handle 'from ... import ...'
                result.append(tok._replace(string=PYTHON_TO_THAI["from"]))
                i += 1
                while i < len(tokens) and tokens[i].string != "import":
                    result.append(tokens[i])
                    i += 1
                if i < len(tokens) and tokens[i].string == "import":
                    result.append(tokens[i]._replace(string=PYTHON_TO_THAI["import"]))
            elif tok.string == "else":
                # Check if it's 'else' or 'elif'
                next_token = tokens[i + 1] if i + 1 < len(tokens) else None
                if (
                    next_token
                    and next_token.type == tokenize.NAME
                    and next_token.string == "if"
                ):
                    result.append(tok._replace(string=PYTHON_TO_THAI["elif"]))
                    i += 1  # Skip the 'if' in 'elif'
                else:
                    result.append(tok._replace(string=PYTHON_TO_THAI["else"]))
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

    if len(sys.argv) == 3:
        output_file = sys.argv[2]
    else:
        output_file = os.path.splitext(input_file)[0] + ".pi"

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
