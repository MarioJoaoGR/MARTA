
import pytest
from pypara.monetary import SomeMoney

def test_valid_input():
    money = SomeMoney(ccy='USD', qty=100, dov='2023-01-01')
    assert money.as_boolean() is True

def test_edge_case():
    money = SomeMoney(ccy='USD', qty=0, dov='2023-01-01')
    assert money.as_boolean() is False

def test_invalid_input():
    with pytest.raises(TypeError):
        SomeMoney()
