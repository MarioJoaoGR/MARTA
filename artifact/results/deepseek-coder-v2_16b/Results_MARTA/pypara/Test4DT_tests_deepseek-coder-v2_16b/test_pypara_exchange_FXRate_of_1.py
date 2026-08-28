
import pytest
from pypara.exchange import FXRate
from pypara.currencies import Currency, Currencies
from decimal import Decimal
import datetime


def test_fxrate_of_method_invalid_value():
    with pytest.raises(ValueError):
        FXRate.of(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("0"))

def test_fxrate_of_method_correct_creation():
    rate = FXRate.of(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("1.2345"))
    assert isinstance(rate, FXRate)
    ccy1, ccy2, date, value = rate
    assert ccy1 == Currencies["USD"]
    assert ccy2 == Currencies["EUR"]
    assert date == datetime.date.today()
    assert value == Decimal("1.2345")