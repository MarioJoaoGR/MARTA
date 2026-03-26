
# Module: isort.wrap_modes
# test_isort_wrap_modes.py
import pytest

from isort.wrap_modes import hanging_indent_with_parentheses


def test_hanging_indent_with_parentheses_empty_interface():
    interface = {}
    with pytest.raises(KeyError):
        result = hanging_indent_with_parentheses(**interface)

def test_hanging_indent_with_parentheses_no_imports():
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
    assert isinstance(result, str), "The function should return a string."

def test_hanging_indent_with_parentheses_single_import():
    interface = {
        "imports": ["from module1 import func1"],
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

def test_hanging_indent_with_parentheses_multiple_imports():
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

def test_hanging_indent_with_parentheses_long_import():
    interface = {
        "imports": ["from very_long_module_name import func1"],
        "line_length": 20,
        "comments": [],
        "remove_comments": False,
        "comment_prefix": "# ",
        "line_separator": "\n",
        "indent": "    ",
        "include_trailing_comma": True,
        "statement": "from very_long_module_name import func1 and"
    }
    result = hanging_indent_with_parentheses(**interface)
    assert isinstance(result, str), "The function should return a string."

def test_hanging_indent_with_parentheses_comments():
    interface = {
        "imports": ["from module1 import func1", "import os"],
        "line_length": 80,
        "comments": ["# This is a comment", "# Another comment"],
        "remove_comments": False,
        "comment_prefix": "# ",
        "line_separator": "\n",
        "indent": "    ",
        "include_trailing_comma": True,
        "statement": "from module1 import func1 and"
    }
    result = hanging_indent_with_parentheses(**interface)
    assert isinstance(result, str), "The function should return a string."

def test_hanging_indent_with_parentheses_exceeds_line_length():
    interface = {
        "imports": ["from module1 import func1", "import os"],
        "line_length": 20,
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
