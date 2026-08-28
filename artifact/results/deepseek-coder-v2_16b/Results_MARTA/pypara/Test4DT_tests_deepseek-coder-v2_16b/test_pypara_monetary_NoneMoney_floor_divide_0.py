
import pytest
from pypara.monetary import Money, NoneMoney


def test_undefined_floor_divide():
    undefined_money = NoneMoney()
    with pytest.raises(TypeError):
        undefined_money.floor_divide(Money(ccy='USD', qty=10))