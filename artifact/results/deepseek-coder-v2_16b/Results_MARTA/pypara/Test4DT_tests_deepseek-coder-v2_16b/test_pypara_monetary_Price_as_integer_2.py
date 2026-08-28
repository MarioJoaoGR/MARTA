
import pytest
from decimal import Decimal
from pypara.monetary import Price, MonetaryOperationException



def test_invalid_input():
    price_instance = Price()
    with pytest.raises(AttributeError):
        assert price_instance.qty == Decimal('100.50')