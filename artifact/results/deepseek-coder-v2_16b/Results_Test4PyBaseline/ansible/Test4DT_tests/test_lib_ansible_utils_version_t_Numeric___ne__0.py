# Module: ansible.utils.version
import pytest
from ansible.utils.version import _Numeric

# Test case for initializing an instance with an integer
def test_numeric_init_with_integer():
    num = _Numeric(5)
    assert num.specifier == 5

# Test case for initializing an instance with a string representation of a number
def test_numeric_init_with_string():
    num = _Numeric("6")
    assert num.specifier == 6

# Test case for comparing two instances of _Numeric using the less than operator
def test_numeric_less_than():
    num1 = _Numeric(5)
    num3 = _Numeric(7)
    assert num1 < num3

# Test case for comparing an instance of _Numeric with an integer using the less than operator
def test_numeric_less_than_with_integer():
    num1 = _Numeric(5)
    assert num1 < 8

# Test case for comparing two instances of _Numeric for equality
def test_numeric_equal():
    num1 = _Numeric(5)
    num4 = _Numeric("5")
    assert num1 == num4

# Test case for checking inequality using the not equal operator
def test_numeric_not_equal():
    num1 = _Numeric(5)
    num3 = _Numeric(7)
    assert num1 != num3
