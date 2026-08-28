
import pytest
from ansible.utils.version import _Numeric

def test_numeric_comparison():
    num1 = _Numeric(5)
    num2 = _Numeric('5')
    assert num1 == num2, "Comparing an integer and a string should be equal"

def test_numeric_inequality():
    num3 = _Numeric(10)
    num4 = _Numeric(20)
    assert num3 != num4, "Comparing different integers should be unequal"

def test_string_to_integer_comparison():
    num5 = _Numeric('5')
    num6 = 5
    assert num5 == num6, "String '5' should be converted to integer and compared as such"
