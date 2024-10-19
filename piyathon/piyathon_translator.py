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
                if tok.string == "for":
                    i = self.handle_for_in(tokens, i, result)
                else:
                    result.append(tok._replace(string=self.py_to_thai[tok.string]))
            else:
                result.append(tok)
            i += 1
        return tokenize.untokenize(result)

    def handle_for_in(self, tokens, i, result):
        result.append(tokens[i]._replace(string=self.py_to_thai["for"]))
        i += 1
        while i < len(tokens) and tokens[i].string != "in":
            result.append(tokens[i])
            i += 1
        if i < len(tokens) and tokens[i].string == "in":
            result.append(tokens[i]._replace(string=self.py_to_thai["in"]))
        return i

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
                if tok.string == self.py_to_thai["for"]:
                    i = self.handle_thai_for_in(tokens, i, result)
                else:
                    result.append(tok._replace(string=self.thai_to_py[tok.string]))
            else:
                result.append(tok)
            i += 1
        return tokenize.untokenize(result)

    def handle_thai_for_in(self, tokens, i, result):
        result.append(tokens[i]._replace(string="for"))
        i += 1
        while i < len(tokens) and tokens[i].string != self.py_to_thai["in"]:
            result.append(tokens[i])
            i += 1
        if i < len(tokens) and tokens[i].string == self.py_to_thai["in"]:
            result.append(tokens[i]._replace(string="in"))
        return i
