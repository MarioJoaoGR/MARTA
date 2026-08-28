
import pytest
from ansible.utils.version import _Numeric

def test_numeric_init():
    num1 = _Numeric(5)
    assert num1.specifier == 5
    
    num2 = _Numeric('10')
    assert num2.specifier == 10

def test_numeric_comparison():
    num3 = _Numeric(5)
    num4 = _Numeric('10')
    assert num3 < num4
    
    str_num = '7'
    num5 = _Numeric(str_num)
    assert num3 < num5

def test_numeric_greater_than():
    num6 = _Numeric(20)
    num7 = _Numeric(10)
    assert num6 > num7
    
    str_num = '3'
    num8 = _Numeric(str_num)
    assert num7 > num8
