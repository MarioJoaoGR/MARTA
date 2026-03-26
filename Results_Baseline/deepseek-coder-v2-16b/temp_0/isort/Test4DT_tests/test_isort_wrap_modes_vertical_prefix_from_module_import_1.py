
import pytest

from isort.wrap_modes import vertical_prefix_from_module_import


def test_vertical_prefix_from_module_import_empty_imports():
    interface = {
        "imports": [],
        "statement": "from prefix_module import",
        "comments": ["# Comment for the first import"],
        "remove_comments": False,
        "comment_prefix": "#",
        "line_length": 50,
        "line_separator": "\n"
    }
    result = vertical_prefix_from_module_import(**interface)
    assert isinstance(result, str), "The result should be a string."
    assert result == "", "Expected an empty string for no imports."

def test_vertical_prefix_from_module_import_single_import():
    interface = {
        "imports": ["import function1"],
        "statement": "from prefix_module import",
        "comments": [],
        "remove_comments": False,
        "comment_prefix": "#",
        "line_length": 50,
        "line_separator": "\n"
    }
    result = vertical_prefix_from_module_import(**interface)
    assert isinstance(result, str), "The result should be a string."