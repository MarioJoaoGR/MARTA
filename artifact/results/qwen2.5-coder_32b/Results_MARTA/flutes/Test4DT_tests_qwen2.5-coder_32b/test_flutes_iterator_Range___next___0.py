
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
    r = Range(10)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4

def test_range_length():
    r = Range(1, 11, 2)
    assert len(r) == 5
