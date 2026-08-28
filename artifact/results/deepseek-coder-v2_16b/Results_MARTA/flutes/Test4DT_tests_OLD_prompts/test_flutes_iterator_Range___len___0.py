
import pytest
from flutes.iterator import Range

def test_range_with_one_argument():
    r = Range(10)
    assert len(r) == 10
    assert list(r) == list(range(10))

def test_range_with_two_arguments():
    r = Range(1, 10 + 1)
    assert len(r) == 10
    assert list(r) == list(range(1, 11))

def test_range_with_three_arguments():
    r = Range(1, 11, 2)
    assert len(r) == 5
    assert list(r) == [1, 3, 5, 7, 9]
