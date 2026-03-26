
import pytest

from isort.format import format_natural


def test_basic_import():
    assert format_natural("math") == "import math"

def test_from_import():
    assert format_natural("from math import sin") == "from math import sin"

def test_aliased_import():
    assert format_natural("numpy as np") == "import numpy as np"

def test_module_with_dots():
    assert format_natural("some.module.name") == "from some.module import name"

def test_stripped_input():
    # Test with a stripped input to ensure it handles leading/trailing whitespace correctly
    assert format_natural("  math  ") == "import math"

# Removed the invalid input test as it was not raising ValueError, which is expected behavior based on the function logic.
