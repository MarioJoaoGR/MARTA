
import pytest
from decimal import Decimal
from pypara.monetary import Price, Currency, Date

# Test cases for scalar_subtract method of Price class




def test_scalar_subtract_undefined_price_with_float():
    price = Price()
    with pytest.raises(NotImplementedError):
        result_price = price.scalar_subtract(2.5)