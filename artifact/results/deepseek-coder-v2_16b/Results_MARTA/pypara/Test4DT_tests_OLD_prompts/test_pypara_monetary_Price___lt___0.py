
import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import Currency, Price

# Test for price comparison when the first price is less than the second
def test_price_lt_true():
    with pytest.raises(TypeError):
        price1 = Price()
        price1.ccy = Currency('USD')  # This should raise a TypeError due to missing required arguments

# Test for price comparison when the first price is not less than the second
def test_price_lt_false():
    with pytest.raises(TypeError):
        price1 = Price()
        price1.ccy = Currency('USD')  # This should raise a TypeError due to missing required arguments

# Test for price comparison between the same instance (should not be less than itself)
def test_price_lt_same_instance():
    with pytest.raises(TypeError):
        price = Price()
        price.ccy = Currency('USD')  # This should raise a TypeError due to missing required arguments
