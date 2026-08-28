
import pytest
from pypara.monetary import NonePrice, Price, NoMoney


def test_noneprice_gt():
    price1 = NonePrice()
    with pytest.raises(TypeError):
        result = price1 > Price(value=5)