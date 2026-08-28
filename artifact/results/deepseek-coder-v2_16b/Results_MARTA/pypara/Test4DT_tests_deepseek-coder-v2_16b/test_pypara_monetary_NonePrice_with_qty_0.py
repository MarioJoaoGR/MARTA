
import pytest
from pypara.monetary import NonePrice

def test_valid_case():
    price = NonePrice()
    assert bool(price) is False
    with pytest.raises(TypeError):
        float(price)

def test_edge_case():
    price = NonePrice()
    assert bool(price) is False
    with pytest.raises(TypeError):
        float(price)

def test_error_handling():
    price = NonePrice()
    with pytest.raises(TypeError):
        float(price)
