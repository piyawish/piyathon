# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import tokenize
from io import StringIO
from .keywords import PY_TO_PI, PI_TO_PY


class PiyathonTranslator:

    @staticmethod
    def is_string_like(token):
        return token.type in (
            tokenize.STRING,
            tokenize.FSTRING_START,
            tokenize.FSTRING_END,
        )

    @classmethod
    def custom_untokenize(cls, tokens):
        """Adjust the start position of adjacent string-like tokens.
        This is to fix the issue where the start position of adjacent string-like tokens
        is not correctly adjusted during translation.

        It might be a bug in the tokenize module introduced in
        https://github.com/python/cpython/commit/ecf16ee50e42f979624e55fa343a8522942db2e7#diff-35c916ae2b7e488053d1c28da2a853790f2c0474e909c03950e49aa4203ea976R306
        """
        modified_tokens = []
        for i, token in enumerate(tokens):
            if (
                cls.is_string_like(token)
                and i > 0
                and cls.is_string_like(modified_tokens[-1])
            ):
                # Adjust the start position of adjacent string-like tokens
                prev_token = modified_tokens[-1]
                modified_tokens.append(
                    token._replace(start=(prev_token.end[0], prev_token.end[1] + 1))
                )
            else:
                modified_tokens.append(token)

        return tokenize.untokenize(modified_tokens)

    @classmethod
    def clean_whitespaces(cls, code):
        tokens = list(tokenize.generate_tokens(StringIO(code).readline))
        return cls.custom_untokenize(tokens)

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
        return self.custom_untokenize(result)

    def python_to_piyathon(self, code):
        return self.translate(code, PY_TO_PI)

    def piyathon_to_python(self, code):
        return self.translate(code, PI_TO_PY)
