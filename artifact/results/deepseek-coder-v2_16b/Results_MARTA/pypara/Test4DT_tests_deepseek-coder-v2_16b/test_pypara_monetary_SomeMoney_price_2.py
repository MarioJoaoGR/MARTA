
import pytest
from pypara.monetary import SomeMoney

def test_valid_inputs():
    money_obj = SomeMoney(ccy='USD', qty=10, dov=20)
    assert isinstance(money_obj, SomeMoney)
    assert money_obj.ccy == 'USD'
    assert money_obj.qty == 10
    assert money_obj.dov == 20

def test_edge_cases():
    money_obj = SomeMoney(ccy='EUR', qty=5, dov=1)
    assert isinstance(money_obj, SomeMoney)
    assert money_obj.ccy == 'EUR'
    assert money_obj.qty == 5
    assert money_obj.dov == 1

def test_invalid_inputs():
    with pytest.raises(TypeError):
        SomeMoney()
