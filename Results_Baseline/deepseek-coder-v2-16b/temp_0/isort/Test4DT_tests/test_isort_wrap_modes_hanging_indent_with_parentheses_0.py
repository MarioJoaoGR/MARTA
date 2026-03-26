
# Module: isort.wrap_modes
# test_isort_wrap_modes.py
import pytest

from isort.wrap_modes import hanging_indent_with_parentheses


def test_hanging_indent_with_parentheses_all_parameters():
    interface = {
        "imports": ["from module1 import func1", "import os"],
        "line_length": 80,
        "comments": [],
        "remove_comments": False,
        "comment_prefix": "# ",
        "line_separator": "\n",
        "indent": "    ",
        "include_trailing_comma": True,
        "statement": "from module1 import func1 and"
    }
    result = hanging_indent_with_parentheses(**interface)
    assert isinstance(result, str), "The function should return a string."