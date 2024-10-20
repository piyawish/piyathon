# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import tokenize
from io import StringIO
from .keywords import PY_TO_THAI, THAI_TO_PY


class PiyathonTranslator:
    def __init__(self):
        self.py_to_thai = PY_TO_THAI
        self.thai_to_py = THAI_TO_PY

    def translate(self, code, translation_dict):
        tokens = list(tokenize.generate_tokens(StringIO(code).readline))
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
        return self.translate(code, self.py_to_thai)

    def piyathon_to_python(self, code):
        return self.translate(code, self.thai_to_py)
