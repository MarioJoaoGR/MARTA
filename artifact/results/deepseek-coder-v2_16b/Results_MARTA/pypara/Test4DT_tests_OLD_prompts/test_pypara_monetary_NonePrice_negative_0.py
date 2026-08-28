
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



