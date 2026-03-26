
# Module: pymonet.utils
# test_increase.py
import pytest
from pymonet.utils import increase
import sys  # Importing sys module here since it is used in the test cases

def test_increase_positive():
    assert increase(5) == 6

def test_increase_negative():
    assert increase(-2) == -1

def test_increase_zero():
    assert increase(0) == 1

# Test with the maximum positive integer value
@pytest.mark.parametrize("value, expected", [(sys.maxsize, sys.maxsize + 1)])
def test_increase_max_int(value, expected):
    assert increase(value) == expected

# Test with the minimum negative integer value
@pytest.mark.parametrize("value, expected", [(-sys.maxsize - 1, -sys.maxsize)])
def test_increase_min_int(value, expected):
    assert increase(value) == expected
