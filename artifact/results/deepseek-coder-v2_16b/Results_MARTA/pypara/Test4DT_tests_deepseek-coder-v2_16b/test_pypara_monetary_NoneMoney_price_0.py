
import pytest
from pypara.monetary import NoneMoney, NonePrice, NoPrice

def test_valid_case():
    nm = NoneMoney()
    assert bool(nm) is False  # Check if it evaluates to False in a boolean context
    with pytest.raises(TypeError):
        raise TypeError("NoneMoney does not support arithmetic operations")

def test_edge_case():
    price = NonePrice()
    assert bool(price) is False  # Check if it evaluates to False in a boolean context
    assert price == NonePrice()  # Check equality with another NonePrice instance
    with pytest.raises(TypeError):
        raise TypeError("NonePrice does not support arithmetic operations")

def test_invalid_input():
    nm = NoneMoney()
    price = NonePrice()
    assert bool(nm) is False  # Check if it evaluates to False in a boolean context
    assert bool(price) is False  # Check if it evaluates to False in a boolean context
    with pytest.raises(TypeError):
        raise TypeError("NoneMoney and NonePrice do not support arithmetic operations")
