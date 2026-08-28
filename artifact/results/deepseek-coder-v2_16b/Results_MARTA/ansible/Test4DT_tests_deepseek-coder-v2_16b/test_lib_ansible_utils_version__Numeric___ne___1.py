
import pytest
from ansible.utils.version import _Numeric

def test_numeric_init():
    num = _Numeric(5)
    assert num.specifier == 5

def test_numeric_str_init():
    num_str = _Numeric('10')
    assert num_str.specifier == 10

def test_numeric_equal():
    num1 = _Numeric(5)
    num2 = _Numeric('5')
    assert num1 == num2

def test_numeric_not_equal():
    num3 = _Numeric(10)
    num4 = _Numeric(20)
    assert num3 != num4

def test_numeric_ne_method():
    num5 = _Numeric(10)
    num6 = _Numeric(20)
    assert num5.specifier != num6.specifier
