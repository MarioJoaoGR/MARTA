
import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney

# Test cases for NoneMoney class
def test_none_money_with_qty():
    nm = NoneMoney()
    result = nm.with_qty(Decimal('100.00'))
    assert isinstance(result, NoneMoney), "Expected the method to return an instance of NoneMoney"