
import pytest
from pymonet.utils import eq

# Test cases for eq function
def test_eq_equal():
    assert eq(5, 5) == True
    assert eq("hello", "hello") == True
    assert eq(None, None) == True
    assert eq([1, 2], [1, 2]) == True
    assert eq({"a": 1}, {"a": 1}) == True

def test_eq_not_equal():
    assert eq(5, 6) == False
    assert eq("hello", "world") == False
    assert eq(None, 0) == False
    assert eq([1, 2], [3, 4]) == False