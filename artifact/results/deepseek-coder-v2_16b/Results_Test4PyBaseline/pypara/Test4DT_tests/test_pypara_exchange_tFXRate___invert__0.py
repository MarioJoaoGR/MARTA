# Module: pypara.exchange
# test_fxrate.py
import datetime
from decimal import Decimal
from pypara.currencies import Currencies
import pytest
from pypara.exchange import FXRate

@pytest.fixture(scope="module")
def fx_rate():
    return FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))

def test_fx_rate_creation(fx_rate):
    assert isinstance(fx_rate, FXRate)
    assert fx_rate.ccy1 == Currencies["EUR"]
    assert fx_rate.ccy2 == Currencies["USD"]
    assert fx_rate.date == datetime.date.today()
    assert fx_rate.value == Decimal("2")

def test_fx_rate_inversion(fx_rate):
    inverted_rate = ~fx_rate
    expected_rate = FXRate(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("0.5"))
    assert inverted_rate == expected_rate
