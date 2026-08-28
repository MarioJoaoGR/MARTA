
import pytest
from flutes.iterator import drop

def test_drop_positive_n():
    assert list(drop(3, [10, 20, 30, 40, 50])) == [40, 50]
    assert ''.join(drop(2, "hello")) == "llo"
    assert list(drop(5, range(10))) == [5, 6, 7, 8, 9]

def test_drop_zero_n():
    assert list(drop(0, ['a', 'b', 'c'])) == ['a', 'b', 'c']
    assert list(drop(0, range(5))) == [0, 1, 2, 3, 4]
    assert ''.join(drop(0, "test")) == "test"

def test_drop_n_equal_to_length():
    assert list(drop(5, range(5))) == []
    assert list(drop(3, "abc")) == []

def test_drop_n_greater_than_length():
    assert list(drop(10, range(5))) == []
    assert list(drop(4, "abc")) == []

def test_drop_with_generator_expression():
    gen = (x * x for x in range(10))