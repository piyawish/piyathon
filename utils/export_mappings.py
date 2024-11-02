# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import json
import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from piyathon.keywords import PI_TO_PY, PY_TO_PI


def export_mappings():
    mappings = {"PI_TO_PY": PI_TO_PY, "PY_TO_PI": PY_TO_PI}

    with open("python_mappings.json", "w", encoding="utf-8") as f:
        json.dump(mappings, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    export_mappings()
