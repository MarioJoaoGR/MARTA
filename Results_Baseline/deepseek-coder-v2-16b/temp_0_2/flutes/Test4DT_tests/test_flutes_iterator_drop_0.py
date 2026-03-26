# Module: flutes.iterator
import pytest
from typing import Iterable, Iterator, TypeVar

T = TypeVar('T')

# Import the function here
from flutes.iterator import drop

def test_drop_positive_n():
    result = list(drop(5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert result == [5, 6, 7, 8, 9]

def test_drop_zero():
    result = list(drop(0, [1, 2, 3, 4, 5]))
    assert result == [1, 2, 3, 4, 5]

def test_drop_all():
    result = list(drop(10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert result == []

def test_drop_negative_n_raises_ValueError():
    with pytest.raises(ValueError) as e:
        list(drop(-1, [0, 1, 2, 3, 4]))
    assert str(e.value) == "`n` should be non-negative"

def test_drop_empty_iterable():
    result = list(drop(5, []))
    assert result == []

def test_drop_string_iterable():
    result = list(drop(3, 'abcdefg'))
    assert result == ['d', 'e', 'f', 'g']

def test_drop_generator():
    def generate_numbers():
        for i in range(20):
            yield i
    
    result = list(drop(8, generate_numbers()))
    assert result == [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
