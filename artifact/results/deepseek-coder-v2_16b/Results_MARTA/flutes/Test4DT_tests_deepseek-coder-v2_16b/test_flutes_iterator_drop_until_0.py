
import pytest
from flutes.iterator import drop_until
from typing import Callable, Iterable, Iterator, TypeVar

T = TypeVar('T')

def test_invalid_input_none_predicate():
    iterable = range(10)
    with pytest.raises(TypeError):
        list(drop_until(None, iterable))

def test_all_elements_dropped():
    def always_false(x):
        return False
    
    iterable = range(10)
    result = drop_until(always_false, iterable)
    assert list(result) == []

def test_some_elements_not_dropped():
    def predicate(x):
        return x > 5
    
    iterable = range(10)
    expected = [6, 7, 8, 9]
    result = drop_until(predicate, iterable)
    assert list(result) == expected
