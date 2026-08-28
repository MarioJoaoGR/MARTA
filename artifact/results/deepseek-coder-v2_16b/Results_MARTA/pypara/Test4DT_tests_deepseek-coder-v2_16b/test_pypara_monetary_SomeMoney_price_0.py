
import pytest
from pypara.monetary import SomeMoney

# Test for valid input scenario
def test_valid_input():
    money_obj = SomeMoney(ccy='USD', qty=100, dov=200)
    assert isinstance(money_obj, SomeMoney)
    assert money_obj.ccy == 'USD'
    assert money_obj.qty == 100
    assert money_obj.dov == 200

# Test for invalid input scenario
def test_invalid_input():
    with pytest.raises(TypeError):
        SomeMoney()

# Test for edge case where None is passed as an argument
def test_edge_case():
    with pytest.raises(TypeError):
        money_obj_none = SomeMoney(None)
        assert money_obj_none is None
