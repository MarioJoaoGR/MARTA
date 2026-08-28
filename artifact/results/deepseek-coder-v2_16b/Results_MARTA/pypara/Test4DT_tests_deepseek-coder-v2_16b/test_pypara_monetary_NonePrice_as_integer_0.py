
import pytest
from pypara.monetary import NonePrice

def test_valid_case():
    price = NonePrice()
    assert bool(price) is False, "Expected bool value of NonePrice to be False"
    with pytest.raises(TypeError):
        int(price)
    with pytest.raises(TypeError):
        float(price)

def test_edge_case():
    price = NonePrice()
    with pytest.raises(TypeError):
        int(price)
    with pytest.raises(TypeError):
        float(price)

def test_error_case():
    price = NonePrice()
    with pytest.raises(TypeError):
        int(price)
    with pytest.raises(TypeError):
        float(price)
