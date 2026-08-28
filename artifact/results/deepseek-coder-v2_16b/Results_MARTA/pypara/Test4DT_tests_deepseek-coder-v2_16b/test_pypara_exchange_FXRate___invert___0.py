
import pytest
from pypara.exchange import FXRate
from pypara.currencies import Currencies
import datetime
from decimal import Decimal

def test_valid_fxrate_creation():
    rate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    assert isinstance(rate, FXRate)
    assert rate.ccy1 == Currencies["EUR"]
    assert rate.ccy2 == Currencies["USD"]
    assert rate.date == datetime.date.today()
    assert rate.value == Decimal("2")

def test_invalid_fxrate_creation():
    with pytest.raises(TypeError):
        FXRate()  # Missing arguments should raise TypeError

def test_invert_fxrate():
    nrate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    inverted_rate = ~nrate
    assert isinstance(inverted_rate, FXRate)
    assert inverted_rate.ccy1 == Currencies["USD"]
    assert inverted_rate.ccy2 == Currencies["EUR"]
    assert inverted_rate.date == datetime.date.today()
    assert inverted_rate.value == Decimal("0.5")
