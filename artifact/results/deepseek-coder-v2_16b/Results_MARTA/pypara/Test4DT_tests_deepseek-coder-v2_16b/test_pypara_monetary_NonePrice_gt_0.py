
import pytest
from pypara.monetary import NonePrice, Price, NoMoney



def test_noneprice_bool():
    none_price = NonePrice()
    assert not bool(none_price), "NonePrice should evaluate to False in a boolean context"