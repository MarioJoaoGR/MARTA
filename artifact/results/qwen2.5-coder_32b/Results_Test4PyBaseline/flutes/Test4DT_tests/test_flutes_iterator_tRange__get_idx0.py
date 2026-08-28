
import pytest
from flutes.iterator import Range

def test_range_single_argument():
    r = Range(10)
    assert list(r) == list(range(10))
    assert r[0] == 0
    assert r[9] == 9

def test_range_two_arguments():
    r = Range(1, 11)
    assert list(r) == list(range(1, 11))
    assert r[0] == 1
    assert r[9] == 10

def test_range_three_arguments():
    r = Range(1, 11, 2)
    assert list(r) == list(range(1, 11, 2))
    assert r[0] == 1
    assert r[4] == 9

def test_range_negative_indexing():
    r = Range(1, 11, 2)
    assert r[-1] == 9