
from isort.parse import Config, DEFAULT_CONFIG
import pytest

# Assuming the function definition is correct as per the provided docstring
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

# Test cases for import_type function
@pytest.mark.parametrize("line, config, expected", [
    ("import os", DEFAULT_CONFIG, "straight"),  # Straight import
    ("from math import sqrt", DEFAULT_CONFIG, "from"),  # From import
    ("# noqa: F401", DEFAULT_CONFIG, None),  # Ignored due to noqa
    ("isort:skip this line", DEFAULT_CONFIG, None),  # Ignored due to isort:skip
    ("cimport some_module", DEFAULT_CONFIG, "straight"),  # Cimport statement
    ("from math import sin  # isort: skip", DEFAULT_CONFIG, None),  # Ignored with comment
    ("import os  # noqa: F401", Config(honor_noqa=False), "straight"),  # Not ignored due to honor_noqa=False
    ("from math import cos  # isort: split", DEFAULT_CONFIG, None),  # Ignored due to isort:split
])
def test_import_type(line, config, expected):
    assert import_type(line, config) == expected
