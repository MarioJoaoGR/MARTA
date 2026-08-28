
import pytest
from pypara.monetary import NonePrice, Currency, Price


def test_handling_undefined_price():
    undefined_price = NonePrice()
    with pytest.raises(TypeError):
        converted_price = undefined_price.with_ccy(Currency('JPY'))