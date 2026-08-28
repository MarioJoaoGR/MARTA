# Module: pymonet.utils
import pytest
from pymonet.utils import eq

# Test cases for eq function
def test_eq_equal():
    assert eq(5, 5) is True
    assert eq('hello', 'hello') is True
    assert eq(None, None) is True
    assert eq([1, 2], [1, 2]) is True

def test_eq_not_equal():
    assert eq(5, 6) is False
    assert eq('hello', 'world') is False
    assert eq(None, 0) is False
    assert eq([1, 2], [3, 4]) is False

def test_eq_different_types():
    assert eq(5, "5") is False
    assert eq('hello', b'hello') is False
    assert eq(None, []) is False

def test_eq_edge_cases():
    # Edge case with large numbers or strings to ensure performance and memory usage are handled correctly
    large_number = 10**100
    assert eq(large_number, large_number) is True
    very_long_string = 'a' * (2 ** 16)  # A string of length 32768 to test memory and performance
    assert eq(very_long_string, very_long_string) is True
