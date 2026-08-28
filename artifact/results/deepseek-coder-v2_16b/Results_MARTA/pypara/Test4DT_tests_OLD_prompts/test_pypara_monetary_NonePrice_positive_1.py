
import pytest
from pypara.monetary import NonePrice, NoMoney

def test_noneprice_float():
    price = NonePrice()
    with pytest.raises(TypeError):
        float(price)

def test_noneprice_int():
    price = NonePrice()
    with pytest.raises(TypeError):
        int(price)






def test_noneprice_lt():
    price1 = NonePrice()
    price2 = NonePrice()
    assert (price1 < price2) == False

def test_noneprice_le():
    price1 = NonePrice()
    price2 = NonePrice()
    assert (price1 <= price2) == True

def test_noneprice_gt():
    price1 = NonePrice()
    price2 = NonePrice()
    assert (price1 > price2) == False

def test_noneprice_ge():
    price1 = NonePrice()
    price2 = NonePrice()
    assert (price1 >= price2) == True