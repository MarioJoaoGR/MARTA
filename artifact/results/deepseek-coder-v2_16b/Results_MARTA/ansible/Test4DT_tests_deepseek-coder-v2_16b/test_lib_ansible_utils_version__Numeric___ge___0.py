
import pytest
from ansible.utils.version import _Numeric

def test_valid_inputs():
    num1 = _Numeric(5)
    num2 = _Numeric('10')
    num3 = _Numeric(7)
    
    assert num1 < num2, "5 is not less than 10"
    assert num1 <= num2, "5 is not less than or equal to 10"
    assert num2 >= num1, "10 is greater than or equal to 5"
    assert num3 <= num2, "7 is less than or equal to 10"

def test_edge_cases():
    with pytest.raises(TypeError):
        num_none = _Numeric(None)

def test_invalid_inputs():
    with pytest.raises(ValueError):
        invalid_input1 = _Numeric('abc')
