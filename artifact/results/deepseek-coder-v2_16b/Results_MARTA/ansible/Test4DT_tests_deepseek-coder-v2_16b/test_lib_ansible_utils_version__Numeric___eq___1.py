
import pytest
from ansible.utils.version import _Numeric

def test__Numeric___eq___basic():
    num1 = _Numeric(5)
    num2 = _Numeric('5')
    
    assert num1 == num2, "Equality comparison between an integer and a string should return True"
    
    num3 = _Numeric(10)
    num4 = _Numeric('10')
    
    assert num3 == num4, "Equality comparison between two strings representing the same number should return True"
    
    num5 = _Numeric(10)
    num6 = _Numeric(20)
    
    assert not (num5 == num6), "Equality comparison between different integers should return False"
