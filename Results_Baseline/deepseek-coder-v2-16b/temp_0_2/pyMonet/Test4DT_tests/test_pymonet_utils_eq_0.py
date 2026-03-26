
import pytest
from pymonet.utils import eq

# Test cases for the eq function
def test_eq_equal():
    assert eq(5, 5) is True
    assert eq("hello", "hello") is True
    assert eq(None, None) is True
    assert eq([1, 2], [1, 2]) is True

def test_eq_not_equal():
    assert eq(5, 6) is False
    assert eq("hello", "world") is False
    assert eq(None, 0) is False