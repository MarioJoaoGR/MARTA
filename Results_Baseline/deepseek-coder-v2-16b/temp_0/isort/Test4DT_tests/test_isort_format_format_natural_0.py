# Module: isort.format
# test_isort_format.py
import pytest

from isort.format import format_natural


def test_simple_import():
    assert format_natural("math") == 'import math'

def test_alias_import():
    assert format_natural("numpy as np") == 'import numpy as np'

def test_from_import():
    assert format_natural("from math import sin") == 'from math import sin'

def test_complex_from_import():
    assert format_natural("sys.path") == 'from sys import path'

def test_unformatted_input():
    assert format_natural("import os") == 'import os'
