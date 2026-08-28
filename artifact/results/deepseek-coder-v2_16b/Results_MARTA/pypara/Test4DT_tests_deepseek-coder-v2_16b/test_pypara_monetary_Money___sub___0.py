
import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import Currency, Money


def test_error_handling():
    with pytest.raises(TypeError):
        money1 = Money(ccy=Currency('USD'), qty=Decimal('100.0'), dov=date.today())
        money2 = None  # Assuming None is used to represent an undefined Money object
        result_money = money1 - money2

def test_error_handling_reverse():
    with pytest.raises(TypeError):
        money1 = None  # Assuming None is used to represent an undefined Money object
        money2 = Money(ccy=Currency('USD'), qty=Decimal('50.0'), dov=date.today())
        result_money = money1 - money2