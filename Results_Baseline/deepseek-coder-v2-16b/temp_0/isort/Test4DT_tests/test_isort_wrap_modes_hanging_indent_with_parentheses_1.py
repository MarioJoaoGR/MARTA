
# Module: isort.wrap_modes
# test_isort_wrap_modes.py
import pytest

from isort.wrap_modes import hanging_indent_with_parentheses


def test_hanging_indent_with_parentheses_empty_imports():
    interface = {
        "imports": [],
        "line_length": 80,
        "comments": [],
        "remove_comments": False,
        "comment_prefix": "# ",
        "line_separator": "\n",
        "indent": "    ",
        "include_trailing_comma": True,
        "statement": ""
    }
    result = hanging_indent_with_parentheses(**interface)
    assert result == "", "The function should return an empty string for no imports."

def test_hanging_indent_with_parentheses_exact_line_length():
    interface = {
        "imports": ["from module1 import func1"],
        "line_length": 20,  # Adjusted line length to exactly match the first import statement
        "comments": [],
        "remove_comments": False,
        "comment_prefix": "# ",
        "line_separator": "\n",
        "indent": "    ",
        "include_trailing_comma": True,
        "statement": "from module1 import func1 and"
    }
    result = hanging_indent_with_parentheses(**interface)
    expected_result = (
        "from module1 import func1\n"  # Hanging indent applied here
        "and from module1 import func1)"  # Final statement with trailing comma
    )