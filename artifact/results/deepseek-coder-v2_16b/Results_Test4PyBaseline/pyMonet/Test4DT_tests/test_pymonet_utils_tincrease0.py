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

# Additional edge cases to consider
def test_increase_large_positive():
    assert increase(1000000) == 1000001

def test_increase_large_negative():
    assert increase(-1000000) == -999999

# Test case for non-integer input to ensure the function handles errors gracefully
def test_increase_non_integer():
    with pytest.raises(TypeError):
        increase("test")
