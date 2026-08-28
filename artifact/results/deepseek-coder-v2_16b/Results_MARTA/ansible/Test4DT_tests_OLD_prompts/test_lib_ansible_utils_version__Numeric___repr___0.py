
import pytest
from unittest.mock import patch
from ansible.utils.version import _Numeric

def test__Numeric___repr___basic():
    num1 = _Numeric(10)
    assert repr(num1) == '10'
    
    num2 = _Numeric('20')
    assert repr(num2) == '20'
    
    num3 = _Numeric(5)
    assert repr(num3) == '5'
    
    num4 = _Numeric('5')
    assert repr(num4) == '5'
    
    num5 = _Numeric(10)
    num6 = _Numeric(20)
    assert repr(num5) == '10'
    assert repr(num6) == '20'
    assert (num5 == num6) is False
