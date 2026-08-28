
import pytest
from pypara.monetary import NonePrice

def test_noneprice_creation():
    price = NonePrice()
    assert isinstance(price, NonePrice), "Expected an instance of NonePrice"

def test_bool_representation():
    price = NonePrice()
    assert bool(price) is False, "Expected bool representation to be False for NonePrice"

def test_comparison():
    price1 = NonePrice()
    price2 = NonePrice()
    assert price1 == price2, "Expected comparison between two instances of NonePrice to be True"


def test_conversion_methods():
    price = NonePrice()
    with pytest.raises(TypeError):
        float_value = float(price)
    with pytest.raises(TypeError):
        int_value = int(price)