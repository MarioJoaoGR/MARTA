
import pytest
from pypara.monetary import NonePrice

def test_bool_representation():
    np = NonePrice()
    assert not bool(np), "Expected bool representation of NonePrice to be False"

def test_float_conversion():
    np = NonePrice()
    with pytest.raises(TypeError):
        float(np)

def test_int_conversion():
    np = NonePrice()
    with pytest.raises(TypeError):
        int(np)
