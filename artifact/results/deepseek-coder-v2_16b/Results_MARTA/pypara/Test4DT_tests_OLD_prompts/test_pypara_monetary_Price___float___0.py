
import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import Currency, Price

# Test for initializing a Price object with valid parameters

# Test for initializing a Price object with invalid currency type
def test_price_invalid_currency():
    with pytest.raises(TypeError):
        price = Price(ccy='USD', qty=Decimal('100.50'), dov=date.today())

# Test for initializing a Price object without required parameters