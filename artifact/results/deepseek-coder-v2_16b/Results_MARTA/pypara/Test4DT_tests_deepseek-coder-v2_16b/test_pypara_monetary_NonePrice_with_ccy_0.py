
import pytest
from pypara.monetary import NonePrice, Currency, Price



def test_invalid_currency():
    undefined_price = NonePrice()
    with pytest.raises(TypeError):
        converted_price = undefined_price.with_ccy(Currency('XXX'))