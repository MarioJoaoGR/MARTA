
import pytest
from flutes.iterator import drop
from typing import Iterable, Iterator, List

# Test cases for the `drop` function
def test_drop_positive():
    result = list(drop(5, range(10)))  # Drop the first 5 elements from a range of numbers
    assert result == [5, 6, 7, 8, 9]

def test_drop_single():
    result = list(drop(1, [10, 20, 30, 40]))  # Drop the first element from a list
    assert result == [20, 30, 40]

def test_drop_negative():
    with pytest.raises(ValueError) as e:
        result = list(drop(-1, range(10)))  # Drop negative value should raise ValueError
    assert str(e.value) == "`n` should be non-negative"

def test_drop_tuple():
    result = list(drop(2, (100, 200, 300, 400)))  # Drop the first 2 elements from a tuple
    assert result == [300, 400]

def test_drop_zero():
    result = list(drop(0, range(10)))  # Drop zero elements should return the original iterable
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Additional test cases to cover uncovered lines (88-89)
def test_drop_negative_value():
    with pytest.raises(ValueError):
        list(drop(-1, range(10)))  # Drop negative value should raise ValueError

def test_drop_large_n():
    result = list(drop(10, range(5)))  # Drop more elements than the length of the iterable
    assert len(result) == 0

def test_drop_empty_iterable():
    result = list(drop(3, []))  # Drop from an empty iterable
    assert len(result) == 0
