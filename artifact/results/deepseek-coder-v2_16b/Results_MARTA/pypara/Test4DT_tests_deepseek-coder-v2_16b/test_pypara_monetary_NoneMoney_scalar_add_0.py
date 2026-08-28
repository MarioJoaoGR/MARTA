
import pytest
from pypara.monetary import NoneMoney

# Test for scalar_add method of NoneMoney class
def test_scalar_add():
    money = NoneMoney()
    result = money.scalar_add(50)
    assert isinstance(result, NoneMoney), "Expected the same type after adding a scalar value"
    assert result == money, "Expected no change when adding a scalar value to NoneMoney"

# Test for scalar_add method with float
def test_scalar_add_float():
    money = NoneMoney()
    result = money.scalar_add(50.25)
    assert isinstance(result, NoneMoney), "Expected the same type after adding a scalar value"
    assert result == money, "Expected no change when adding a float to NoneMoney"
