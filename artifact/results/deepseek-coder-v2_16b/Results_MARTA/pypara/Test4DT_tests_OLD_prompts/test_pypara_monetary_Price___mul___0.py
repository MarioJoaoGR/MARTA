
import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import Price, Currency

def test_price_creation():
    with pytest.raises(TypeError):
        price = Price(ccy=Currency('USD'), qty=Decimal('100.25'), dov=date(2023, 4, 1))
