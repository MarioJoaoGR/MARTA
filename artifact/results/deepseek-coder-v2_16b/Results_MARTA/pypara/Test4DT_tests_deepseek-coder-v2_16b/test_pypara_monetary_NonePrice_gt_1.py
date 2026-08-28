
from pypara.monetary import NonePrice
import pytest

def test_noneprice_bool():
    none_price = NonePrice()
    assert bool(none_price) is False, "NonePrice should be falsy in boolean context"

def test_noneprice_float_conversion():
    none_price = NonePrice()
    with pytest.raises(TypeError):
        float(none_price), "Conversion of NonePrice to float should raise TypeError"

def test_noneprice_int_conversion():
    none_price = NonePrice()
    with pytest.raises(TypeError):
        int(none_price), "Conversion of NonePrice to int should raise TypeError"
