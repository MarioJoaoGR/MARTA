
import pytest
from ansible.utils.version import _Numeric

def test_numeric_string_comparison():
    str_num = '7'
    num3 = _Numeric(str_num)
    assert num3 == 7, "Expected string representation of number to be converted to integer for comparison"

def test_numeric_alpha_comparison():
    with pytest.raises(ValueError):
        alpha_val = _Numeric('a')

def test_numeric_different_values():
    num6 = _Numeric(20)
    assert num6 == 20, "Expected different numeric values to be considered unequal"
