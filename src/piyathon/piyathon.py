import sys
import ast
from keywords import THAI_TO_PYTHON


class ThaiKeywordTransformer(ast.NodeTransformer):
    def visit_Name(self, node):
        if node.id in THAI_TO_PYTHON:
            return ast.Name(id=THAI_TO_PYTHON[node.id], ctx=node.ctx)
        return node


def execute_piyathon(code):
    tree = ast.parse(code)
    transformed_tree = ThaiKeywordTransformer().visit(tree)
    # pylint: disable=exec-used
    exec(compile(transformed_tree, filename="<ast>", mode="exec"), globals())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python piyathon.py <piyathon_file>")
        sys.exit(1)

    piyathon_file = sys.argv[1]

    try:
        with open(piyathon_file, "r", encoding="utf-8") as file:
            piyathon_code = file.read()
    except FileNotFoundError:
        print(f"Error: File '{piyathon_file}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Unable to read file '{piyathon_file}'.")
        sys.exit(1)

    execute_piyathon(piyathon_code)
