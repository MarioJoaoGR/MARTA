
import pytest
from pypara.monetary import SomeMoney, SomePrice

def test_valid_inputs():
    money_obj = SomeMoney(ccy='USD', qty=100, dov=200)
    assert isinstance(money_obj, SomeMoney)
    assert money_obj.ccy == 'USD'
    assert money_obj.qty == 100
    assert money_obj.dov == 200

def test_edge_cases():
    money_obj = SomeMoney(ccy='EUR', qty=0, dov=0)
    assert isinstance(money_obj, SomeMoney)
    assert money_obj.ccy == 'EUR'
    assert money_obj.qty == 0
    assert money_obj.dov == 0

def test_invalid_inputs():
    with pytest.raises(TypeError):
        SomeMoney()
