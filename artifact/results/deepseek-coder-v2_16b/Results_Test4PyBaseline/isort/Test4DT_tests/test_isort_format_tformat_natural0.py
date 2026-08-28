# Module: isort.format
# test_isort_format.py
import pytest
from isort.format import format_natural

def test_format_natural_standalone_module():
    assert format_natural("math") == "import math"

def test_format_natural_from_import():
    assert format_natural("from math import sin") == "from math import sin"

def test_format_natural_nested_modules():
    assert format_natural("math.sin") == "from math import sin"

def test_format_natural_with_alias():
    # Note: The function does not directly support this case, but it demonstrates how to handle different cases.
    assert format_natural("numpy as np") == "import numpy as np"
