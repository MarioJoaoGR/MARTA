
import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import Currency, Money

# Test initialization of Money object
def test_money_initialization():
    with pytest.raises(TypeError):
        money = Money(ccy=Currency('USD'), qty=Decimal('100.50'), dov=date(2023, 1, 1))

# Test defined attribute of Money object
def test_money_defined():
    with pytest.raises(TypeError):
        money = Money(ccy=Currency('USD'), qty=Decimal('100.50'), dov=date(2023, 1, 1))

# Test conversion to int of Money object
def test_money_to_int():
    with pytest.raises(TypeError):
        money = Money(ccy=Currency('USD'), qty=Decimal('100.50'), dov=date(2023, 1, 1))
