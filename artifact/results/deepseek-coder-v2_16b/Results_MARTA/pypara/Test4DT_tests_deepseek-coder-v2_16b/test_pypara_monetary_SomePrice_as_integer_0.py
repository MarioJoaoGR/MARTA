
import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomePrice


def test_as_integer_method():
    price = SomePrice(ccy='USD', qty=Decimal('100.25'), dov=date.today())
    assert price.as_integer() == 100, "Expected the integer representation of quantity to be 100"