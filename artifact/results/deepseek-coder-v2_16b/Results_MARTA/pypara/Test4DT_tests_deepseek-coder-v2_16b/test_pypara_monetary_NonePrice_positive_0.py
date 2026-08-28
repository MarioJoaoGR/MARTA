
import pytest
from pypara.monetary import NonePrice

def test_valid_input():
    price = NonePrice()
    assert bool(price) is False, "Price should be considered false if undefined"
    with pytest.raises(TypeError):
        float(price)

def test_edge_case():
    with pytest.raises(TypeError):
        NonePrice().as_float()

def test_invalid_input():
    price = NonePrice()
    with pytest.raises(TypeError):
        float(price)
