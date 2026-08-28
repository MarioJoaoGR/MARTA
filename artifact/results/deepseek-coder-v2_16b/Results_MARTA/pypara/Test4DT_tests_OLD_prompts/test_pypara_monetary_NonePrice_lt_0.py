
import pytest
from pypara.monetary import NonePrice, Price


def test_none_price_float():
    none_price = NonePrice()
    with pytest.raises(TypeError, match="Undefined monetary values do not have quantity information."):
        float(none_price)

def test_none_price_int():
    none_price = NonePrice()
    with pytest.raises(TypeError, match="Undefined monetary values do not have quantity information."):
        int(none_price)
