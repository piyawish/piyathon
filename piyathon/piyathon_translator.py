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

    def translate(self, code, translation_dict):
        try:
            tokens = list(tokenize.generate_tokens(StringIO(code).readline))
        except (tokenize.TokenError, IndentationError) as e:
            print(f"Error tokenizing code: {e}")
            return None

        result = [
            (
                tok._replace(string=translation_dict.get(tok.string, tok.string))
                if tok.type == tokenize.NAME
                else tok
            )
            for tok in tokens
        ]
        return tokenize.untokenize(result)

    def python_to_piyathon(self, code):
        if not self.check_syntax(code):
            return None
        return self.translate(code, self.py_to_thai)

    def piyathon_to_python(self, code):
        return self.translate(code, self.thai_to_py)
