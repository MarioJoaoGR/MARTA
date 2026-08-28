
import pytest
from decimal import Decimal
from pypara.currencies import Currencies
from pypara.exchange import FXRate, Date

# Test creating an FX rate with valid parameters
def test_create_fxrate_with_valid_parameters():
    ccy1 = Currencies["USD"]
    ccy2 = Currencies["EUR"]
    date = Date(2023, 4, 1)
    value = Decimal("2")
    fxrate = FXRate.of(ccy1, ccy2, date, value)
    
    assert isinstance(fxrate, FXRate)
    assert fxrate.ccy1 == ccy1
    assert fxrate.ccy2 == ccy2
    assert fxrate.date == date
    assert fxrate.value == value

# Test creating an FX rate with invalid currency type for CCY1
def test_create_fxrate_with_invalid_currency_type():
    ccy1 = "USD"
    ccy2 = Currencies["EUR"]
    date = Date(2023, 4, 1)
    value = Decimal("2")
    
    with pytest.raises(ValueError):
        FXRate.of(ccy1, ccy2, date, value)

# Test creating an FX rate with invalid currency type for CCY2
def test_create_fxrate_with_invalid_currency_type():
    ccy1 = Currencies["USD"]
    ccy2 = "EUR"
    date = Date(2023, 4, 1)
    value = Decimal("2")
    
    with pytest.raises(ValueError):
        FXRate.of(ccy1, ccy2, date, value)

# Test creating an FX rate with invalid value type

# Test creating an FX rate with invalid date type

# Test creating an FX rate with invalid value (less than or equal to zero)
def test_create_fxrate_with_invalid_value():
    ccy1 = Currencies["USD"]
    ccy2 = Currencies["EUR"]
    date = Date(2023, 4, 1)
    value = Decimal("0")
    
    with pytest.raises(ValueError):
        FXRate.of(ccy1, ccy2, date, value)

# Test creating an FX rate with the same currency not equal to one
def test_create_fxrate_with_same_currency_not_equal_to_one():
    ccy1 = Currencies["USD"]
    ccy2 = Currencies["USD"]
    date = Date(2023, 4, 1)
    value = Decimal("1.5")
    
    with pytest.raises(ValueError):
        FXRate.of(ccy1, ccy2, date, value)

# Test querying an FX rate (mocking the FXRateService class)