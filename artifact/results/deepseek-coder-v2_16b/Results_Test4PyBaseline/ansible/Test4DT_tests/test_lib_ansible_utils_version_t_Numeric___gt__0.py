
# Module: ansible.utils.version
import pytest
from ansible.utils.version import _Numeric

# Test initialization with an integer
def test_numeric_init_with_integer():
    num1 = _Numeric(5)
    assert num1.specifier == 5

# Test initialization with a string representation of an integer
def test_numeric_init_with_string():
    num2 = _Numeric("6")
    assert num2.specifier == 6

# Test comparison using less than (<)
def test_numeric_less_than():
    num1 = _Numeric(5)
    num2 = _Numeric("6")
    assert num1 < num2

# Test comparison using equality (==)
def test_numeric_equal_to():
    num3 = _Numeric("7")
    num1 = _Numeric(5)  # Corrected the variable name to match previous definitions
    assert not (num1 == num3)

# Test comparison using greater than (>)
def test_numeric_greater_than():
    num3 = _Numeric("7")
    num1 = _Numeric(5)  # Corrected the variable name to match previous definitions
    assert num3 > num1

# Test comparison using less than or equal to (<=)
def test_numeric_less_or_equal_to():
    num1 = _Numeric(5)  # Corrected the variable name to match previous definitions
    num2 = _Numeric("6")  # Corrected the variable name to match previous definitions
    assert num1 <= num2

# Test comparison using greater than or equal to (>=)
def test_numeric_greater_or_equal_to():
    num3 = _Numeric("7")
    num1 = _Numeric(5)  # Corrected the variable name to match previous definitions
    assert num3 >= num1

# Test initialization with a non-integer string, should raise ValueError
def test_numeric_init_with_non_integer_string():
    with pytest.raises(ValueError):
        _Numeric("abc")

# Test comparison with a non-numeric type, should raise ValueError
def test_numeric_comparison_with_non_numeric():
    alpha_instance = object()  # Assuming this is not numeric
    num1 = _Numeric(5)  # Corrected the variable name to match previous definitions
    with pytest.raises(ValueError):
        num1 < alpha_instance
