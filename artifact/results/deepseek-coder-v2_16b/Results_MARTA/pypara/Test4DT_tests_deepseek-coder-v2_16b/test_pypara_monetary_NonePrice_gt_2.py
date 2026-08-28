
import pytest
from pypara.monetary import NonePrice

def test_noneprice_creation():
    none_price = NonePrice()
    assert isinstance(none_price, NonePrice), "Expected an instance of NonePrice"

def test_noneprice_boolean():
    none_price = NonePrice()
    assert not bool(none_price), "Expected bool representation to be False for a NonePrice instance"

def test_noneprice_comparison():
    none_price1 = NonePrice()
    none_price2 = NonePrice()
    assert none_price1 == none_price2, "Expected two instances of NonePrice to be equal"


def test_noneprice_float_conversion():
    none_price = NonePrice()
    with pytest.raises(TypeError):
        float(none_price)