
import pytest
from ansible.utils.version import _Numeric

def test_numeric_comparison():
    num1 = _Numeric(10)
    num2 = _Numeric('10')
    assert num1 == num2, "Comparing integer and string representation of the same number should be equal"

    num3 = _Numeric(5)
    num4 = _Numeric('5')
    assert num3 == num4, "Comparing different numeric strings with the same value should be equal"

    num5 = _Numeric(10)
    num6 = _Numeric(20)
    assert num5 != num6, "Comparing different integers should not be equal"

def test_numeric_less_than():
    num7 = _Numeric(5)
    num8 = _Numeric('10')
    assert num7 < num8, "5 is less than 10"

def test_numeric_greater_than():
    num9 = _Numeric(20)
    num10 = _Numeric('10')
    assert num9 > num10, "20 is greater than 10"

def test_numeric_less_or_equal():
    num11 = _Numeric(5)
    num12 = _Numeric('10')
    assert num11 <= num12, "5 is less than or equal to 10"

def test_numeric_greater_or_equal():
    num13 = _Numeric(20)
    num14 = _Numeric('10')
    assert num13 >= num14, "20 is greater than or equal to 10"
