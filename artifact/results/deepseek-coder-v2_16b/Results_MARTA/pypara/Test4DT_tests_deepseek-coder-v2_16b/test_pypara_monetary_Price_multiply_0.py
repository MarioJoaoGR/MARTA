
import pytest
from pypara.monetary import Price, Currency, Date, Numeric

# Test for multiplying a defined price

# Test for multiplying an undefined price
def test_multiply_undefined_price():
    p = Price()
    with pytest.raises(NotImplementedError):
        p.multiply(3)

# Test for multiplying by zero