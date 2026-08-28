# Module: ansible.utils.version
import pytest
from ansible.utils.version import _Numeric

# Test case for creating an instance with an integer
def test_numeric_creation_with_integer():
    num1 = _Numeric(5)
    assert num1.specifier == 5

# Test case for creating an instance with a string representation of a number
def test_numeric_creation_with_string():
    num2 = _Numeric("6")
    assert num2.specifier == 6

# Test case for comparing two _Numeric objects using the `<` operator
def test_numeric_comparison_less_than():
    num1 = _Numeric(5)
    num2 = _Numeric("6")
    assert num1 < num2

# Test case for comparing two _Numeric objects using the `==` operator
def test_numeric_comparison_equal():
    num1 = _Numeric(5)
    num2 = _Numeric("6")
    assert not (num1 == num2)

# Test case for creating another instance with a string representation of a number and comparing it to the first instance
def test_numeric_comparison_with_string():
    num1 = _Numeric(5)
    num3 = _Numeric("7")
    assert num1 < num3

# Test case for comparing a numeric object with an instance of another class (e.g., str)
def test_numeric_comparison_with_non_numeric():
    num1 = _Numeric(5)
    alpha_instance = "alpha"  # Assuming this is not a number and should raise a ValueError
    with pytest.raises(ValueError):
        assert num1 < alpha_instance
