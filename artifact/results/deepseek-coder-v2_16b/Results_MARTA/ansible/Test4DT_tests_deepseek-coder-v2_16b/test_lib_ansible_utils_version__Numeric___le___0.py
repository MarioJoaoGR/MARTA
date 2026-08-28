
import pytest
from ansible.utils.version import _Numeric

def test_numeric_comparison():
    num1 = _Numeric(10)
    num2 = _Numeric('10')
    assert num1 == num2, "Comparing integer and string representation of the same number should be equal"


def test_numeric_greater_than():
    num5 = _Numeric(10)
    num6 = _Numeric(20)
    assert not (num5 > num6), "10 is not greater than 20"

def test_numeric_less_or_equal():
    num7 = _Numeric(5)
    num8 = _Numeric('5')
    assert num7 <= num8, "'5' should be less than or equal to '5'"
