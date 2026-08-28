
import pytest
from pypara.monetary import NonePrice, NoMoney

def test_valid_input():
    none_price = NonePrice()
    assert bool(none_price) is False
    with pytest.raises(TypeError):
        float(none_price)

def test_edge_case():
    none_price = NonePrice()
    with pytest.raises(TypeError):
        float(none_price)
    with pytest.raises(TypeError):
        int(none_price)

def test_invalid_input():
    none_price = NonePrice()
    with pytest.raises(TypeError):
        float(none_price)
