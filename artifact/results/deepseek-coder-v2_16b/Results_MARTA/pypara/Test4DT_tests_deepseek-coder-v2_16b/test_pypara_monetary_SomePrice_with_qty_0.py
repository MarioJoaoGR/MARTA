
import pytest
from decimal import Decimal
from pypara.monetary import SomePrice


def test_invalid_currency():
    with pytest.raises(TypeError):
        SomePrice(currency='XYZ', amount=Decimal('100'), exchange_rate=1.2)

def test_missing_arguments():
    with pytest.raises(TypeError):
        SomePrice()