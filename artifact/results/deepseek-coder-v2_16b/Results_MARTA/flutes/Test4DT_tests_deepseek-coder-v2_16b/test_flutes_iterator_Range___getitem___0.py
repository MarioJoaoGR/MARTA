
import pytest
from flutes.iterator import Range



def test_valid_range():
    r = Range(5)
    assert list(r) == [0, 1, 2, 3, 4]

def test_range_with_start_and_end():
    r = Range(1, 10)
    assert list(r) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_range_with_start_end_and_step():
    r = Range(1, 10, 2)
    assert list(r) == [1, 3, 5, 7, 9]

def test_getitem_positive_index():
    r = Range(10)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4

def test_getitem_negative_index():
    r = Range(10)
    assert r[-1] == 9
    assert r[-3] == 7
    assert r[-5] == 5

def test_getitem_slice():
    r = Range(1, 10)
    assert list(r[1:4]) == [2, 3, 4]

def test_getitem_negative_slice():
    r = Range(1, 10)
    assert list(r[-5:-2]) == [5, 6, 7]