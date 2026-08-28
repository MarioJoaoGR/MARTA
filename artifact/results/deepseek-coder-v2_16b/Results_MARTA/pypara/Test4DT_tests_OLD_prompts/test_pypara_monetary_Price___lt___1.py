
import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import Currency, Price

# Test for price comparison when currencies are different and quantities are involved
def test_price_lt_different_currency_and_quantity():
    with pytest.raises(TypeError):
        price1 = Price()
        price1.ccy = Currency('USD')
        price2 = Price()
        price2.ccy = Currency('EUR')
        assert price1 < price2

# Test for price comparison when currencies are the same but quantities are different
def test_price_lt_same_currency_different_quantity():
    with pytest.raises(TypeError):
        price1 = Price()
        price1.ccy = Currency('USD')
        price1.qty = Decimal('100.25')
        price2 = Price()
        price2.ccy = Currency('USD')
        price2.qty = Decimal('99.99')
        assert price1 < price2

# Test for price comparison when currencies are the same, quantities are the same but dates are different
def test_price_lt_same_currency_quantity_different_date():
    with pytest.raises(TypeError):
        price1 = Price()
        price1.ccy = Currency('USD')
        price1.qty = Decimal('100.25')
        price1.dov = date(2023, 4, 1)
        price2 = Price()
        price2.ccy = Currency('USD')
        price2.qty = Decimal('100.25')
        price2.dov = date(2023, 4, 2)
        assert price1 < price2

# Test for price comparison when currencies are the same, quantities are the same, and dates are the same but one is defined and the other is undefined
def test_price_lt_same_currency_quantity_date_different_defined():
    with pytest.raises(TypeError):
        price1 = Price()
        price1.ccy = Currency('USD')
        price1.qty = Decimal('100.25')
        price1.dov = date(2023, 4, 1)
        price1.defined = True
        price2 = Price()
        price2.ccy = Currency('USD')
        price2.qty = Decimal('100.25')
        price2.dov = date(2023, 4, 1)
        assert price1 < price2
