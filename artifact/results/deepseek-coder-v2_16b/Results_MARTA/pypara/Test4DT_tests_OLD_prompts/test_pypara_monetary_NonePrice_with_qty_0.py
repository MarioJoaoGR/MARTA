
import pytest
from pypara.monetary import NonePrice, NoMoney
from decimal import Decimal

def test_noneprice_creation():
    price = NonePrice()
    assert bool(price) == False, "Expected bool(NonePrice()) to be False"

def test_compare_noneprice_instances():
    price1 = NonePrice()
    price2 = NonePrice()
    assert price1 == price2, "Expected two instances of NonePrice to be equal"


def test_convert_to_float_raise_typeerror():
    price = NonePrice()
    with pytest.raises(TypeError):
        float_value = float(price)

def test_with_qty_method_returns_self():
    price = NonePrice()
    new_price = price.with_qty(Decimal('100'))
    assert isinstance(new_price, NonePrice), "Expected with_qty to return the same instance"