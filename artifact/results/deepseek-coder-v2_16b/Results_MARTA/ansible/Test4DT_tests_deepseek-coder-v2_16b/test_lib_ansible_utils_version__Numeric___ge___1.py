
import pytest
from ansible.utils.version import _Numeric

def test_valid_inputs():
    num1 = _Numeric(5)
    num2 = _Numeric('10')
    num3 = _Numeric(7)
    
    assert num1.specifier == 5
    assert num2.specifier == 10
    assert num3.specifier == 7

def test_edge_cases():
    with pytest.raises(TypeError):
        _Numeric(None)

def test_comparison():
    num1 = _Numeric(5)
    num2 = _Numeric('10')
    num3 = _Numeric(10)
    
    assert num1 < num2
    assert num2 >= num3
