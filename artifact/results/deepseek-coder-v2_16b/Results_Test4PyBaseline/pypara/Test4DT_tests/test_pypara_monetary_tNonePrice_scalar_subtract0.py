
import pytest
from pypara.monetary import NonePrice

# Test initialization of NonePrice instance
def test_noneprice_initialization():
    undefined_price = NonePrice()
    assert bool(undefined_price) is False, "Expected bool(undefined_price) to be False"

# Test scalar subtraction with numeric types (should return self)
@pytest.mark.parametrize("other", [10, 5.2, -3, 0])
def test_scalar_subtract(other):
    undefined_price = NonePrice()
    result = undefined_price.scalar_subtract(other)
    assert result is undefined_price, "Expected scalar_subtract to return self"

# Test addition with numeric types (should not change the instance)
@pytest.mark.parametrize("other", [10, 5.2, -3, 0])
def test_addition(other):
    undefined_price = NonePrice()
    result = undefined_price + other