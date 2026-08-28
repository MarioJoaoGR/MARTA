# Module: ansible.utils.version
import pytest
from ansible.utils.version import _Numeric

# Test initialization with an integer
def test_numeric_init_with_integer():
    num = _Numeric(5)
    assert num.specifier == 5

# Test initialization with a string that can be converted to an integer
def test_numeric_init_with_string():
    num = _Numeric("6")
    assert num.specifier == 6

# Test comparison between two _Numeric objects
def test_numeric_comparison():
    num1 = _Numeric(5)
    num2 = _Numeric(6)
    assert (num1 < num2) is True

# Test equality comparison with integers and strings
def test_numeric_equality_comparison():
    str_num = "7"
    num3 = _Numeric(str_num)
    num4 = _Numeric(5)
    assert (num4 == num3) is False

# Test greater than or equal to comparison
def test_numeric_ge_comparison():
    num1 = _Numeric(5)
    num2 = _Numeric(6)
    assert (num1 >= num2) is False

# Test less than or equal to comparison
def test_numeric_le_comparison():
    num1 = _Numeric(5)
    num2 = _Numeric(4)
    assert (num1 <= num2) is False

# Test comparison with a non-numeric type
def test_numeric_non_numeric_type():
    num = _Numeric(5)
    with pytest.raises(ValueError):
        num < "string"
