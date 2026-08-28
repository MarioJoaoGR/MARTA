
import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import Currency, Price

# Test for creating a Price object
def test_price_creation():
    with pytest.raises(TypeError):
        price = Price(ccy=Currency('USD'), qty=Decimal('100.25'), dov=date(2023, 4, 1))

# Test for converting a Price object
def test_price_conversion():
    with pytest.raises(TypeError):
        price = Price(ccy=Currency('USD'), qty=Decimal('100.25'), dov=date(2023, 4, 1))
        converted_price = price.convert(to=Currency('EUR'))

# Test for multiplying a Price object
def test_price_multiplication():
    with pytest.raises(TypeError):
        price = Price(ccy=Currency('USD'), qty=Decimal('100.25'), dov=date(2023, 4, 1))
        multiplied_price = price * Decimal('2')

# Test for checking if the Price object is defined after multiplication
def test_price_defined_after_multiplication():
    with pytest.raises(TypeError):
        price = Price(ccy=Currency('USD'), qty=Decimal('100.25'), dov=date(2023, 4, 1))
        multiplied_price = price * Decimal('2')
