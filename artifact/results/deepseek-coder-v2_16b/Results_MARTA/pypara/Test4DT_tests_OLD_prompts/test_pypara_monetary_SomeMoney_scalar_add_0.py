
import pytest
from pypara.monetary import SomeMoney, Numeric
from decimal import Decimal


def test_invalid_inputs():
    with pytest.raises(TypeError):
        money = SomeMoney(currency_unit=Decimal('1'), quantity=Decimal('10.50'))
        money.scalar_add("not a number")