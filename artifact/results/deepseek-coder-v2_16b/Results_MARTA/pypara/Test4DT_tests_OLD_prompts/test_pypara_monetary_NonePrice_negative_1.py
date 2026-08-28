
import pytest
from pypara.monetary import NonePrice

def test_noneprice_float_conversion():
    np = NonePrice()
    with pytest.raises(TypeError):
        float(np)

def test_noneprice_int_conversion():
    np = NonePrice()
    with pytest.raises(TypeError):
        int(np)



def test_noneprice_lt():
    np1 = NonePrice()
    np2 = NonePrice()
    assert not (np1 < np2)


def test_noneprice_gt():
    np1 = NonePrice()
    np2 = NonePrice()
    assert not (np1 > np2)
