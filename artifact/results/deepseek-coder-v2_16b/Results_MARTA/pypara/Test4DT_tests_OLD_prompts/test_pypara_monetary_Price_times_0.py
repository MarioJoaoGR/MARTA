
import pytest
from decimal import Decimal
from pypara.monetary import Price, Currency, Money

# Test for times method with defined price

# Test for times method with undefined price

# Test for times method with not implemented error
def test_times_with_not_implemented_error():
    price = Price()
    with pytest.raises(NotImplementedError):
        price.times(2)