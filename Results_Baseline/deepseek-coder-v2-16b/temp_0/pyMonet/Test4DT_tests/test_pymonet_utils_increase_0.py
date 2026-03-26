# Module: pymonet.utils
import pytest
from pymonet.utils import increase

# Test cases for the increase function
def test_increase_positive():
    assert increase(5) == 6

def test_increase_negative():
    assert increase(-2) == -1

def test_increase_zero():
    assert increase(0) == 1

# Test case for the maximum positive integer value
import sys
max_value = sys.maxsize
def test_increase_max_positive():
    assert increase(max_value) == (max_value + 1)
