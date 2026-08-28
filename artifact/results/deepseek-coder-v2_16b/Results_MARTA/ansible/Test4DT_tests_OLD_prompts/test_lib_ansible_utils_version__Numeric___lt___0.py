
import pytest
from ansible.utils.version import _Numeric, _Alpha

def test_numeric_comparison_with_valid_integers():
    num1 = _Numeric(5)
    num2 = _Numeric(5)
    assert num1 == num2

def test_numeric_comparison_with_integer_and_string():
    num3 = _Numeric('5')
    num4 = _Numeric(5)
    assert num3 == num4

def test_numeric_comparison_with_different_integers():
    num5 = _Numeric(10)
    num6 = _Numeric(20)
    assert num5 != num6

def test_numeric_less_than_comparison():
    num7 = _Numeric(3)
    num8 = _Numeric('10')
    assert num7 < num8

def test_numeric_less_than_or_equal_comparison():
    num9 = _Numeric(7)
    num10 = _Numeric('10')
    assert num9 <= num10

def test_numeric_greater_than_comparison():
    num11 = _Numeric('20')
    num12 = _Numeric(15)
    assert num11 > num12

def test_numeric_greater_than_or_equal_comparison():
    num13 = _Numeric('30')
    num14 = _Numeric(30)
    assert num13 >= num14
