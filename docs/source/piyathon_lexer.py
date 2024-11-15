# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import sys
from pathlib import Path

from pygments.lexer import inherit
from pygments.lexers.python import PythonLexer
from pygments.token import Keyword
from pygments.lexers import _mapping

sys.path.append(str(Path(__file__).parent.parent.parent))
from piyathon.keywords import PYTHON_KEYWORDS

__all__ = ["PiyathonLexer"]


class PiyathonLexer(PythonLexer):
    name = "Piyathon"
    aliases = ["piyathon"]
    filenames = ["*.pi"]

    PIYATHON_KEYWORDS = set(PYTHON_KEYWORDS.values())

    tokens = {
        "root": [
            (r"\b(" + "|".join(PIYATHON_KEYWORDS) + r")\b", Keyword),
            inherit,
        ],
    }


# Register the lexer
_mapping.LEXERS[PiyathonLexer.name] = (
    __name__,
    PiyathonLexer.name,
    PiyathonLexer.aliases,
    PiyathonLexer.filenames,
    ("text/x-piyathon",),
)
