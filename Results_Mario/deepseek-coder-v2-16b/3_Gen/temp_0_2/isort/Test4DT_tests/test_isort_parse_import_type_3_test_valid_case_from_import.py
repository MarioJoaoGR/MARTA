
import pytest
from unittest.mock import MagicMock
from isort.parse import Config

# Assuming DEFAULT_CONFIG is defined somewhere in your code or module
DEFAULT_CONFIG = Config()

def import_type(line: str, config: Config = DEFAULT_CONFIG) -> str | None:
    """If the current line is an import line it will return its type (from or straight)"""
    if config.honor_noqa and line.lower().rstrip().endswith("noqa"):
        return None
    if "isort:skip" in line or "isort: skip" in line or "isort: split" in line:
        return None
    if line.startswith(("import ", "cimport ")):
        return "straight"
    if line.startswith("from "):
        return "from"
    return None

@pytest.mark.parametrize("line, expected", [
    ("from math import sin", "from"),
    ("import os", "straight"),
    ("import sys # isort:skip", None),
    ("cimport some_module", "straight"),
    ("from collections import defaultdict", "from"),
    ("from itertools import chain", "from"),
    ("import math", "straight"),
    ("# This should be skipped", None),
    ("from math import sin # isort:skip", None),
])
def test_valid_case_from_import(line, expected):
    config = MagicMock()
    assert import_type(line, config) == expected
