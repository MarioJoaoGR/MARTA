
# Module: flutes.iterator
# test_range.py
from flutes.iterator import Range
import pytest

def test_range_creation():
    r = Range(10)
    assert r[0] == 0, "Indexing the first element of a range should return 0"
    assert r[2] == 2, "Indexing the third element of a range should return 2"
    assert r[4] == 4, "Indexing the fifth element of a range should return 4"

def test_range_creation_with_start_and_end():
    r = Range(1, 10 + 1)
    assert r[0] == 1, "Indexing the first element of a range with start and end should return the start value"
    assert r[2] == 3, "Indexing the third element of a range with start and end should return the correct value"
    assert r[4] == 5, "Indexing the fifth element of a range with start and end should return the correct value"

def test_range_creation_with_start_end_and_step():
    r = Range(1, 11, 2)
    assert r[0] == 1, "Indexing the first element of a range with start, end, and step should return the correct value"
    assert r[2] == 5, "Indexing the third element of a range with start, end, and step should return the correct value"
    assert r[4] == 9, "Indexing the fifth element of a range with start, end, and step should return the correct value"

def test_range_invalid_creation():
    with pytest.raises(ValueError):
        Range()
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)

def test_range_slicing():
    r = Range(1, 11, 2)
    s = slice(0, 5, 2)