# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
Piyathon Code Translation Module

This module provides the core translation functionality between Piyathon and Python code.
It handles the bidirectional translation of keywords and maintains proper code structure
while dealing with special cases like string literals and whitespace.

Core Functionality:
    - Bidirectional translation between Piyathon and Python code
    - Token-based code processing and generation
    - Special handling for adjacent string literals
    - Whitespace preservation and cleanup

Dependencies:
    - tokenize: For Python code tokenization and untokenization
    - io.StringIO: For string-based token generation
    - keywords: For Piyathon-Python keyword mappings

Data Structures:
    - Token objects from the tokenize module representing code elements
    - Translation dictionaries (PY_TO_PI, PI_TO_PY) for keyword mapping

Known Limitations:
    - Handles only direct keyword translations
    - May require special handling for complex string patterns
    - Limited to Python's tokenization capabilities
"""

import tokenize
from io import StringIO
from .keywords import PY_TO_PI, PI_TO_PY


class PiyathonTranslator:
    """
    A translator class that converts between Piyathon and Python code.

    This class provides methods for bidirectional translation between Piyathon and Python
    code using Python's tokenize module. It handles special cases like adjacent string
    literals and maintains proper code formatting.

    Methods:
        is_string_like(token): Check if a token is a string-like token
        custom_untokenize(tokens): Untokenize with special handling for adjacent strings
        clean_whitespaces(code): Clean and normalize code whitespace
        translate(code, translation_dict): Perform the actual translation
        python_to_piyathon(code): Convert Python code to Piyathon
        piyathon_to_python(code): Convert Piyathon code to Python
    """

    @staticmethod
    def is_string_like(token):
        """
        Determine if a token represents a string-like element.

        Args:
            token (TokenInfo): A token from the tokenize module

        Returns:
            bool: True if the token is a string, f-string start, or f-string end

        Example:
            >>> token = get_token()  # Some token
            >>> PiyathonTranslator.is_string_like(token)
            True
        """
        return token.type in (
            tokenize.STRING,
            tokenize.FSTRING_START,
            tokenize.FSTRING_END,
        )

    @classmethod
    def custom_untokenize(cls, tokens):
        """
        Untokenize a sequence of tokens with special handling for adjacent string-like tokens.

        This method fixes issues with adjacent string token positioning that can occur
        during the translation process, ensuring proper spacing and formatting.

        It might be a bug in the tokenize module introduced in
        https://github.com/python/cpython/commit/ecf16ee50e42f979624e55fa343a8522942db2e7#diff-35c916ae2b7e488053d1c28da2a853790f2c0474e909c03950e49aa4203ea976R306

        Args:
            tokens (list): List of TokenInfo objects to be untokenized

        Returns:
            str: The untokenized code as a string

        Side Effects:
            None, but modifies token positions in the process

        Example:
            >>> tokens = tokenize.generate_tokens(StringIO('code').readline)
            >>> PiyathonTranslator.custom_untokenize(list(tokens))
            'code'
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
        """
        Clean and normalize whitespace in the given code.

        Args:
            code (str): The source code to clean

        Returns:
            str: The code with normalized whitespace

        Example:
            >>> code = "def  func ():\\n   pass"
            >>> PiyathonTranslator.clean_whitespaces(code)
            'def func():\\n    pass'
        """
        tokens = list(tokenize.generate_tokens(StringIO(code).readline))
        return cls.custom_untokenize(tokens)

    def translate(self, code, translation_dict):
        """
        Translate code using the provided translation dictionary.

        Args:
            code (str): The source code to translate
            translation_dict (dict): Dictionary mapping source to target keywords

        Returns:
            str: The translated code

        Example:
            >>> translator = PiyathonTranslator()
            >>> translator.translate("def main():", PY_TO_PI)
            'คำสั่ง หลัก():'
        """
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
        """
        Convert Python code to Piyathon code.

        Args:
            code (str): Python source code

        Returns:
            str: Equivalent Piyathon code

        Example:
            >>> translator = PiyathonTranslator()
            >>> translator.python_to_piyathon("def main():\\n    print('Hello')")
            'คำสั่ง หลัก():\\n    พิมพ์("Hello")'
        """
        return self.translate(code, PY_TO_PI)

    def piyathon_to_python(self, code):
        """
        Convert Piyathon code to Python code.

        Args:
            code (str): Piyathon source code

        Returns:
            str: Equivalent Python code

        Example:
            >>> translator = PiyathonTranslator()
            >>> translator.piyathon_to_python('คำสั่ง หลัก():\\n    พิมพ์("Hello")')
            'def main():\\n    print("Hello")'
        """
        return self.translate(code, PI_TO_PY)
