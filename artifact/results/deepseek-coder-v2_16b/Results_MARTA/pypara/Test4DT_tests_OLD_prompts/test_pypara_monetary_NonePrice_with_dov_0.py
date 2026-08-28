
import pytest
from unittest.mock import patch
from pypara.monetary import NonePrice, Date

def test_valid_input():
    price = NonePrice()
    assert bool(price) is False
    with pytest.raises(TypeError):
        float(price)

def test_edge_case():
    with patch('pypara.monetary.NonePrice.__bool__', return_value=False):
        price = NonePrice()
        with pytest.raises(TypeError):
            float(price)

def test_invalid_input():
    price = NonePrice()
    with pytest.raises(TypeError):
        float(price)
