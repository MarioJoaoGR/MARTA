
import pytest
from pypara.monetary import SomeMoney

def test_valid_input():
    money = SomeMoney(ccy='USD', qty=100, dov='2023-01-01')
    assert isinstance(money, SomeMoney)
    assert money.as_integer() == 100

def test_edge_case():
    money = SomeMoney(ccy='USD', qty=0, dov='2023-01-01')
    assert isinstance(money, SomeMoney)
    assert money.as_integer() == 0

def test_invalid_input():
    with pytest.raises(TypeError):
        money = SomeMoney()
