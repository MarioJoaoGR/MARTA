
import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import Currency, Price, MonetaryOperationException, NonePrice





def test_noneprice_operations():
    from pypara.monetary import NonePrice
    
    price = NonePrice()
    assert bool(price) is False
    assert price == NonePrice()