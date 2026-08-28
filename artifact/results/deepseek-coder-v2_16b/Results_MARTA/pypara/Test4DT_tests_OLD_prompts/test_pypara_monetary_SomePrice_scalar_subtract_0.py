
import pytest
from pypara.monetary import SomePrice, NonePrice
from decimal import Decimal

# Test for valid input

# Test for edge case with undefined price

# Test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        SomePrice(currency='USD', quantity=100, decimal_places=2).scalar_subtract('not a number')