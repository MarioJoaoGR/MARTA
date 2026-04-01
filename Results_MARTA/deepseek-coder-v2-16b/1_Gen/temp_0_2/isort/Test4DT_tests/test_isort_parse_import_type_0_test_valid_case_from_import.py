
import pytest
from unittest.mock import MagicMock
from isort.parse import Config, DEFAULT_CONFIG

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
    ("import os", "straight"),
    ("from math import sin", "from"),
    ("import sys # isort:skip", None),
    ("cimport numpy as np", "straight"),
    ("from math import *", "from"),  # Test for wildcard in from import
    ("import os as alias", "straight"),  # Test with alias
    ("cimport os as alias", "straight"),  # Test cimport with alias
    ("from math import sin, cos", "from"),  # Test multiple imports in from statement
    ("# isort:skip", None),  # Test comment line that should be skipped
    ("import os\n# isort:skip", None),  # Test multiline with skip marker
])
def test_import_type(line, expected):
    config = MagicMock()
    assert import_type(line, config) == expected
