# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import ast
import tokenize
from io import StringIO
from .keywords import PY_TO_THAI, THAI_TO_PY


class PiyathonTranslator:
    def __init__(self):
        self.py_to_thai = PY_TO_THAI
        self.thai_to_py = THAI_TO_PY

    def check_syntax(self, code):
        try:
            ast.parse(code)
            return True
        except SyntaxError as e:
            print(f"Syntax error in the input code: {e}")
            return False

    def python_to_piyathon(self, code):
        if not self.check_syntax(code):
            return None

        tokens = list(tokenize.generate_tokens(StringIO(code).readline))
        result = []
        i = 0
        while i < len(tokens):
            tok = tokens[i]
            if tok.type == tokenize.NAME and tok.string in self.py_to_thai:
                result.append(tok._replace(string=self.py_to_thai[tok.string]))
            else:
                result.append(tok)
            i += 1
        return tokenize.untokenize(result)

    def piyathon_to_python(self, code):
        try:
            tokens = list(tokenize.generate_tokens(StringIO(code).readline))
        except (tokenize.TokenError, IndentationError) as e:
            print(f"Error tokenizing Piyathon code: {e}")
            return None

        result = []
        i = 0
        while i < len(tokens):
            tok = tokens[i]
            if tok.type == tokenize.NAME and tok.string in self.thai_to_py:
                result.append(tok._replace(string=self.thai_to_py[tok.string]))
            else:
                result.append(tok)
            i += 1
        return tokenize.untokenize(result)
