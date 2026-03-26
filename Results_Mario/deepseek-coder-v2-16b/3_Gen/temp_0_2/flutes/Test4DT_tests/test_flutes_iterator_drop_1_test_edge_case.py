
import pytest
from flutes.iterator import drop

def test_drop_positive():
    assert list(drop(3, range(10))) == [3, 4, 5, 6, 7, 8, 9]

def test_drop_zero():
    assert list(drop(0, range(10))) == list(range(10))

def test_drop_negative():
    with pytest.raises(ValueError):
        list(drop(-1, range(10)))

def test_drop_larger_than_iterable():
    assert list(drop(10, range(5))) == []

def test_drop_empty_iterable():
    assert list(drop(3, [])) == []
