
import pytest
from pypara.monetary import NonePrice

def test_valid_input():
    price = NonePrice()
    assert isinstance(price, NonePrice)
    assert bool(price) is False
    with pytest.raises(TypeError):
        float(price)

def test_edge_case():
    price = NonePrice()
    or_list = []
    with pytest.raises(TypeError):
        float(price)
