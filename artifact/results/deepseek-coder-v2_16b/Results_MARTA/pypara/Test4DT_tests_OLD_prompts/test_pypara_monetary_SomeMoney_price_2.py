
import pytest
from pypara.monetary import SomeMoney, SomePrice

# Test valid inputs scenario
def test_valid_inputs():
    money = SomeMoney(ccy='USD', qty=100, dov=200)
    assert isinstance(money, SomeMoney)
    assert money.ccy == 'USD'
    assert money.qty == 100
    assert money.dov == 200

# Test edge cases scenario
def test_edge_cases():
    money = SomeMoney(ccy='EUR', qty=50, dov=150)
    assert isinstance(money, SomeMoney)
    assert money.ccy == 'EUR'
    assert money.qty == 50
    assert money.dov == 150

# Test invalid inputs scenario
def test_invalid_inputs():
    with pytest.raises(TypeError):
        SomeMoney()
