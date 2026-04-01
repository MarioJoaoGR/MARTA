
import pytest

from isort.parse import (  # Importing Config and DEFAULT_CONFIG from isort.parse
    DEFAULT_CONFIG, Config)


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

# Test case for edge case with an empty string
def test_edge_case_empty_string():
    assert import_type("") is None
