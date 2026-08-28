
# Module: flutes.iterator
from flutes.iterator import drop
import pytest

def test_drop_positive_value():
    result = drop(3, [0, 1, 2, 3, 4, 5])
    assert list(result) == [3, 4, 5]

def test_drop_zero_value():
    result = drop(0, [0, 1, 2, 3, 4, 5])
    assert list(result) == [0, 1, 2, 3, 4, 5]

def test_drop_larger_than_iterable():
    result = drop(10, range(5))
    assert list(result) == []

def test_drop_negative_value():
    with pytest.raises(ValueError):
        list(drop(-5, range(10)))

def test_drop_from_empty_iterable():
    result = drop(3, [])
    assert list(result) == []

# Additional test cases for the `drop` function to cover uncovered lines 82 and 88-89

def test_drop_with_negative_n():
    with pytest.raises(ValueError):
        list(drop(-3, [0, 1, 2, 3, 4, 5]))

def test_drop_when_iterable_is_exhausted():
    result = drop(3, [0, 1])
    assert list(result) == []
