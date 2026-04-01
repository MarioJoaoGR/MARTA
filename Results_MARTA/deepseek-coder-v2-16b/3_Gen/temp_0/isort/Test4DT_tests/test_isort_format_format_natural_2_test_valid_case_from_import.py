
# Importing format_natural from the correct module path
from isort.format import format_natural


def test_valid_case_from_import():
    # Test cases for valid import lines
    assert format_natural("math") == "import math"
    assert format_natural("numpy as np") == "import numpy as np"
    assert format_natural("from math import sin") == "from math import sin"
    assert format_natural("sys.path") == "from sys import path"
