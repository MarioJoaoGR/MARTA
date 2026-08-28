
import pytest
from unittest.mock import patch, MagicMock
from pypara.exchange import FXRate
from pypara.currencies import Currencies
import datetime
from decimal import Decimal

# Test for the __invert__ method of FXRate class
def test_fxrate_invert():
    with patch('pypara.currencies.Currencies', return_value=MagicMock()):
        rate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
        inverted_rate = ~rate
        assert isinstance(inverted_rate, FXRate)
        assert inverted_rate.ccy1 == Currencies["USD"]
        assert inverted_rate.ccy2 == Currencies["EUR"]
        assert inverted_rate.date == rate.date
        assert inverted_rate.value == Decimal("0.5")

# Test for the __invert__ method with a specific date
def test_fxrate_invert_specific_date():
    with patch('pypara.currencies.Currencies', return_value=MagicMock()):
        specific_date = datetime.date(2023, 10, 1)
        rate = FXRate(Currencies["EUR"], Currencies["USD"], specific_date, Decimal("2"))
        inverted_rate = ~rate
        assert isinstance(inverted_rate, FXRate)
        assert inverted_rate.ccy1 == Currencies["USD"]
        assert inverted_rate.ccy2 == Currencies["EUR"]
        assert inverted_rate.date == rate.date
        assert inverted_rate.value == Decimal("0.5")

# Test for the __invert__ method with a negative value
def test_fxrate_invert_negative_value():
    with patch('pypara.currencies.Currencies', return_value=MagicMock()):
        rate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("-2"))
        inverted_rate = ~rate
        assert isinstance(inverted_rate, FXRate)
        assert inverted_rate.ccy1 == Currencies["USD"]
        assert inverted_rate.ccy2 == Currencies["EUR"]
        assert inverted_rate.date == rate.date
        assert inverted_rate.value == Decimal("-0.5")
