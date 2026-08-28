
import pytest
from pypara.monetary import NonePrice, NoMoney


def test_noneprice_conversion():
    price = NonePrice()
    with pytest.raises(TypeError):
        float(price)
