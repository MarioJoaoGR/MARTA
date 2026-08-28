
import pytest
from flutes.iterator import Range



def test_range_single_argument():
    r = Range(10)
    assert list(r) == list(range(10))

def test_range_two_arguments():
    r = Range(1, 11)
    assert list(r) == list(range(1, 11))

def test_range_three_arguments():
    r = Range(1, 11, 2)
    assert list(r) == list(range(1, 11, 2))

def test_range_indexing():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 5

def test_range_slicing():
    r = Range(1, 11)
    assert list(r[:3]) == [1, 2, 3]
    assert list(r[::2]) == [1, 3, 5, 7, 9]

def test_range_reverse_slicing():
    r = Range(1, 11)
    assert list(r[::-1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def test_range_length():
    r = Range(1, 11, 2)
    assert len(r) == 5