
import pytest
import datetime
from decimal import Decimal
from pypara.currencies import Currencies
from pypara.exchange import FXRate

def test_fxrate_creation():
    # Example call 1: Creating an FXRate instance with valid parameters
    rate_eur_to_usd = FXRate.of(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("1.2"))
    assert isinstance(rate_eur_to_usd, FXRate)
    assert rate_eur_to_usd.ccy1 == Currencies["EUR"]
    assert rate_eur_to_usd.ccy2 == Currencies["USD"]
    assert rate_eur_to_usd.date == datetime.date.today()
    assert rate_eur_to_usd.value == Decimal("1.2")

def test_fxrate_creation_with_different_date_and_value():
    # Example call 2: Creating an FXRate instance with a different date and value
    previous_date = datetime.date.today() - datetime.timedelta(days=5)
    rate_gbp_to_usd = FXRate.of(Currencies["GBP"], Currencies["USD"], previous_date, Decimal("1.3"))
    assert isinstance(rate_gbp_to_usd, FXRate)
    assert rate_gbp_to_usd.ccy1 == Currencies["GBP"]
    assert rate_gbp_to_usd.ccy2 == Currencies["USD"]
    assert rate_gbp_to_usd.date == previous_date