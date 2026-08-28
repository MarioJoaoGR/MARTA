
import pytest

def format_natural(import_line: str) -> str:
    import_line = import_line.strip()
    if not import_line.startswith("from ") and not import_line.startswith("import "):
        if "." not in import_line:
            return f"import {import_line}"
        parts = import_line.split(".")
        end = parts.pop(-1)
        return f"from {'.'.join(parts)} import {end}"

    return import_line

def test_format_natural_basic():
    assert format_natural("os") == "import os"
    assert format_natural("numpy.random") == "from numpy import random"
    assert format_natural("sys.path") == "from sys import path"
    assert format_natural("from math import sqrt") == "from math import sqrt"
    assert format_natural("import json") == "import json"
    assert format_natural("   pandas ") == "import pandas"
