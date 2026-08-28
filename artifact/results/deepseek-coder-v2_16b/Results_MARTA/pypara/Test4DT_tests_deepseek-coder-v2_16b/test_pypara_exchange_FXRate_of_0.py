
import pytest
from datetime import date
from pypara.currencies import Currencies  # Assuming this module contains the Currency classes
from pypara.exchange import FXRateService, FXRate

# Test valid input scenario
def test_valid_input():
    ccy1 = Currencies["EUR"]
    ccy2 = Currencies["USD"]
    rate = FXRate(ccy1, ccy2, date.today(), 2)
    
    assert isinstance(rate, FXRate)
    assert rate.ccy1 == ccy1
    assert rate.ccy2 == ccy2
    assert rate.date == date.today()
    assert rate.value == 2

# Test edge case scenario where no error should be raised
def test_edge_case():
    with pytest.raises(ValueError):
        FXRate.of(None, None, date.today(), 0)

# Test invalid input scenario
def test_invalid_input():
    ccy1 = 'InvalidCurrency'
    ccy2 = 'InvalidCurrency'
    date = 'invalid_date'
    value = 'invalid_value'
    
    with pytest.raises(ValueError):
        FXRate.of(ccy1, ccy2, date, value)
