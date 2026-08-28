
import pytest
from pypara.monetary import NoneMoney, Numeric

# Test case for scalar_add method with integer addition
def test_scalar_add_integer():
    money = NoneMoney()
    result = money.scalar_add(50)
    assert isinstance(result, NoneMoney), "Expected the same type after adding an integer"

# Test case for scalar_add method with float addition
def test_scalar_add_float():
    money = NoneMoney()
    result = money.scalar_add(50.25)
    assert isinstance(result, NoneMoney), "Expected the same type after adding a float"

# Test case for scalar_add method with another instance of Numeric
def test_scalar_add_numeric():
    money = NoneMoney()
    other_money = NoneMoney()
    result = money.scalar_add(other_money)
    assert isinstance(result, NoneMoney), "Expected the same type after adding another instance of NoneMoney"
