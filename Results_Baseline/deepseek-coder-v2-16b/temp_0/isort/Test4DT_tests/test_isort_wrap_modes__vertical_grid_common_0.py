
from typing import Any

import pytest

from isort.wrap_modes import _vertical_grid_common


def test_basic_usage():
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
    result = _vertical_grid_common(need_trailing_char=True, **interface)
    assert isinstance(result, str), "The function should return a string"
    assert len(result.split("\n")) == 2, "Expected two lines of import statements"

def test_custom_comments_and_prefix():
    imports = ["from math import sqrt", "import numpy as np"]
    interface = {
        "imports": imports,
        "comments": "Code to perform mathematical operations.",
        "remove_comments": False,
        "comment_prefix": "##",
        "line_separator": "\n",
        "indent": "    ",
        "include_trailing_comma": True,
        "line_length": 80,
        "statement": ""
    }
    result = _vertical_grid_common(need_trailing_char=True, **interface)
    assert isinstance(result, str), "The function should return a string"
    assert len(result.split("\n")) == 2, "Expected two lines of import statements with comments"