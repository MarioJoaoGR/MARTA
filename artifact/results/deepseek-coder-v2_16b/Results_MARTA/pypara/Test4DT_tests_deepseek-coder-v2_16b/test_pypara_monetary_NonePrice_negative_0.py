
import pytest
from pypara.monetary import NonePrice

def test_noneprice_equality():
    np1 = NonePrice()
    np2 = NonePrice()
    assert np1 == np2, "Two instances of NonePrice should be equal"



def test_noneprice_abs_value():
    np = NonePrice()
    assert abs(np) == np, "Absolute value of an undefined price should be the same price"

def test_noneprice_addition():
    np1 = NonePrice()
    np2 = NonePrice()
    result = np1 + np2
    assert isinstance(result, NonePrice), "Adding two undefined prices should yield another undefined price"

def test_noneprice_negative():
    np = NonePrice()
    assert np.negative() == np, "Negating an undefined price should return the same undefined price"