
# Module: ansible.utils.version
import pytest
from ansible.utils.version import _Numeric

# Test case for defining the behavior of the less than or equal to (`<=`) operator using __le__ method
def test_numeric_less_than_or_equal():
    num1 = _Numeric(5)
    num2 = _Numeric("6")
    assert num1 <= num2  # True, because 5 is less than 6

# Test case for defining the behavior of the less than or equal to (`<=`) operator when objects are equal
def test_numeric_equal():
    num1 = _Numeric(5)
    num3 = _Numeric("5")
    assert num1 <= num3  # True, because both are equal to 5

# Test case for defining the behavior of the less than or equal to (`<=`) operator when self is strictly less than other
def test_numeric_less_than():
    num1 = _Numeric(5)
    num4 = _Numeric("4")
    assert not (num1 <= num4)  # False, because 5 is not less than or equal to 4

# Test case for defining the behavior of the less than or equal to (`<=`) operator with non-numeric types
def test_numeric_comparison_with_non_numeric():
    num1 = _Numeric(5)
    alpha_instance = "alpha"  # Assuming this is not a number and should raise a ValueError
    with pytest.raises(ValueError):
        assert num1 <= alpha_instance
