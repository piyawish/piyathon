# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""Utility script for exporting Piyathon-Python keyword mappings.

This script exports the bidirectional mappings between Piyathon and Python keywords
to a JSON file for use in documentation, tooling, and other integrations.

Dependencies:
    - json: For JSON file operations
    - sys: For path manipulation
    - pathlib: For cross-platform path handling
    - piyathon.keywords: Source of keyword mapping dictionaries

Output:
    Creates 'python_mappings.json' containing two mapping dictionaries:
    - PI_TO_PY: Maps Piyathon keywords to Python keywords
    - PY_TO_PI: Maps Python keywords to Piyathon keywords
"""

import json
import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from piyathon.keywords import PI_TO_PY, PY_TO_PI


def export_mappings():
    """Export keyword mappings to a JSON file.

    Exports both Piyathon-to-Python and Python-to-Piyathon keyword mappings
    to a JSON file named 'python_mappings.json' in the current directory.

    Side Effects:
        - Creates or overwrites 'python_mappings.json' in the current directory
        - File is written with UTF-8 encoding to support Thai characters

    Example:
        >>> export_mappings()
        # Creates python_mappings.json with mapping dictionaries
    """
    mappings = {"PI_TO_PY": PI_TO_PY, "PY_TO_PI": PY_TO_PI}

    with open("python_mappings.json", "w", encoding="utf-8") as f:
        json.dump(mappings, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    export_mappings()
