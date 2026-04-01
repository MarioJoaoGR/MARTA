
import pytest
from isort.parse import Config

# Mocking DEFAULT_CONFIG as per the requirement
class ConfigMock:
    def __init__(self):
        self.honor_noqa = True

DEFAULT_CONFIG = ConfigMock()

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
    ("cimport some_module", "straight"),
    ("import something", "straight"),  # Adding a test for another valid straight import
    ("from math import cos", "from")   # Adding a test for another valid from import
])
def test_valid_case_straight_import(line, expected):
    assert import_type(line) == expected
