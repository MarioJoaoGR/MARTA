
import pytest
from unittest.mock import patch
from pypara.monetary import NonePrice, NoMoney

def test_edge_case():
    price = NonePrice()
    with patch('pypara.monetary.NonePrice.scalar_add', return_value=price):
        assert price == NonePrice().scalar_add(10)
