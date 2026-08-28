
import pytest
from pypara.monetary import NonePrice, NoMoney

def test_valid_input():
    none_price = NonePrice()
    assert not bool(none_price), "NonePrice should return False when converted to boolean"
    with pytest.raises(TypeError):
        float(none_price)

def test_invalid_input():
    none_price = NonePrice()
    with pytest.raises(TypeError):
        float(none_price)
