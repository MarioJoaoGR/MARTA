
import pytest
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
    ("import sys; print(sys.path) # isort: split", None),
    ("from math import sqrt # isort: split", None),
    ("# This is a comment, no import here", None),
    ("import os # isort: skip", None),
    ("from math import sqrt # isort: skip", None),
    ("import sys; print(sys.path)", "straight"),
    ("from math import sqrt", "from"),
])
def test_error_case_isort_split(line, expected):
    config = Config()
    assert import_type(line, config) == expected
