
import pytest
from pypara.monetary import Price, Currency, Date

@pytest.fixture
def price():
    p = Price()
    return p

def test_price_creation(price):
    assert hasattr(price, 'ccy') is False
    assert hasattr(price, 'qty') is False
    assert hasattr(price, 'dov') is False
    assert hasattr(price, 'defined') is False
    assert hasattr(price, 'undefined') is False

