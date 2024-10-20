# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import tokenize
from io import StringIO
from .keywords import PY_TO_PI, PI_TO_PY


class PiyathonTranslator:

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
        return self.translate(code, PY_TO_PI)

    def piyathon_to_python(self, code):
        return self.translate(code, PI_TO_PY)
