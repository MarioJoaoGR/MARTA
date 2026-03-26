# Module: isort.wrap_modes
import pytest

from isort.wrap_modes import vertical_grid_grouped


# Test Case 1: Basic Usage
def test_vertical_grid_grouped_basic():
    imports = ["import os", "import sys"]
    interface = {
        "imports": imports,
        "comments": "",
        "remove_comments": False,
        "comment_prefix": "#",
        "line_separator": "\n",
        "indent": "    ",
        "include_trailing_comma": True,
        "line_length": 80,
        "statement": ""
    }
    result = vertical_grid_grouped(**interface)
    assert isinstance(result, str), "Expected a string output"
    assert len(result.split("\n")) == 3, "Expected multiple lines with proper formatting"

# Test Case 2: With Comments and No Trailing Comma
def test_vertical_grid_grouped_with_comments():
    imports = ["import os", "import sys"]
    interface = {
        "imports": imports,
        "comments": "Initial comments before import statements",
        "remove_comments": False,
        "comment_prefix": "#",
        "line_separator": "\n",
        "indent": "    ",
        "include_trailing_comma": False,
        "line_length": 80,
        "statement": ""
    }
    result = vertical_grid_grouped(**interface)
    assert isinstance(result, str), "Expected a string output"
    assert len(result.split("\n")) == 3, "Expected multiple lines with proper formatting including comments"

# Test Case 3: With Trailing Comma and Custom Indentation
def test_vertical_grid_grouped_custom_indent():
    imports = ["import os", "import sys"]
    interface = {
        "imports": imports,
        "comments": "",
        "remove_comments": False,
        "comment_prefix": "#",
        "line_separator": "\n",
        "indent": "  ",
        "include_trailing_comma": True,
        "line_length": 80,
        "statement": ""
    }
    result = vertical_grid_grouped(**interface)
    assert isinstance(result, str), "Expected a string output"
    assert len(result.split("\n")) == 3, "Expected multiple lines with custom indentation"

# Test Case 4: With Comments and Trailing Comma
def test_vertical_grid_grouped_with_comments_and_trailing_comma():
    imports = ["import os", "import sys"]
    interface = {
        "imports": imports,
        "comments": "Comments before import statements",
        "remove_comments": False,
        "comment_prefix": "#",
        "line_separator": "\n",
        "indent": "    ",
        "include_trailing_comma": True,
        "line_length": 80,
        "statement": ""
    }
    result = vertical_grid_grouped(**interface)
    assert isinstance(result, str), "Expected a string output"
    assert len(result.split("\n")) == 3, "Expected multiple lines with proper formatting including comments and trailing comma"

# Test Case 5: With Trailing Comma and Custom Line Length
def test_vertical_grid_grouped_custom_line_length():
    imports = ["import os", "import sys"]
    interface = {
        "imports": imports,
        "comments": "",
        "remove_comments": False,
        "comment_prefix": "#",
        "line_separator": "\n",
        "indent": "    ",
        "include_trailing_comma": True,
        "line_length": 120,
        "statement": ""
    }
    result = vertical_grid_grouped(**interface)
    assert isinstance(result, str), "Expected a string output"
    assert len(result.split("\n")) == 3, "Expected multiple lines with proper formatting and custom line length"
