
import pytest
from your_module import _Numeric  # Replace 'your_module' with the actual module name where _Numeric is defined

# Test valid inputs
def test_valid_inputs():
    num1 = _Numeric(5)
    num2 = _Numeric('5')
    num3 = _Numeric(10)
    num4 = _Numeric('10')
    num5 = _Numeric(5)
    num6 = _Numeric('5')
    
    assert num1 == num2
    assert num3 != num4
    assert num1 == num5
    assert num2 == num6

# Test edge cases
def test_edge_cases():
    num_none = _Numeric(None)
    num_empty_str = _Numeric('')
    num_maxint = _Numeric(2**63 - 1)
    
    assert num_none == None
    with pytest.raises(ValueError):
        num_empty_str == None
    assert num_maxint != None

# Test invalid inputs
def test_invalid_inputs():
    with pytest.raises(ValueError):
        num_invalid_str = _Numeric('notanumber')
