
import pytest
from ansible.utils.version import _Numeric

def test_numeric_comparison():
    num1 = _Numeric(5)
    num2 = _Numeric('10')
    assert num1 < num2, "Expected 5 to be less than 10"

def test_numeric_equal_comparison():
    num3 = _Numeric(10)
    num4 = _Numeric('10')
    assert num3 == num4, "Expected 10 to be equal to 10"

def test_numeric_greater_than_or_equal_comparison():
    num5 = _Numeric(10)
    num6 = _Numeric(20)
    assert not (num5 >= num6), "Expected 10 not to be greater than or equal to 20"
