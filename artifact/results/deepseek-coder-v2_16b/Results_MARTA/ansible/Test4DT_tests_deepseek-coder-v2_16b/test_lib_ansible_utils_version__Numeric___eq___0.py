
import pytest
from ansible.utils.version import _Numeric

def test_numeric_comparison():
    num1 = _Numeric(5)
    num2 = _Numeric('5')
    assert num1 == num2, "Comparing an instance of _Numeric with another instance should return True if their specifiers are equal"



def test_numeric_integer_equality():
    num5 = _Numeric(10)
    num6 = _Numeric(20)
    assert not (num5 == num6), "Comparing two instances of _Numeric with different integers should return False"
