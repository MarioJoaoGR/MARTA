
import pytest
from flutes.iterator import Range

# Test cases for Range class initialization and indexing
def test_range_creation():
    r = Range(10)
    assert r._get_idx(0) == 0, "Indexing from start should return the correct value"
    assert r._get_idx(2) == 2, "Indexing from start should return the correct value"
    assert r._get_idx(4) == 4, "Indexing from start should return the correct value"

def test_range_creation_with_start_and_end():
    r = Range(1, 10 + 1)
    assert r._get_idx(0) == 1, "Indexing with start and end should return the correct values"
    assert r._get_idx(2) == 3, "Indexing with start and end should return the correct values"
    assert r._get_idx(4) == 5, "Indexing with start and end should return the correct values"

def test_range_creation_with_start_end_and_step():
    r = Range(1, 11, 2)
    assert r._get_idx(0) == 1, "Indexing with start, end, and step should return the correct values"
    assert r._get_idx(2) == 5, "Indexing with start, end, and step should return the correct values"
    assert r._get_idx(4) == 9, "Indexing with start, end, and step should return the correct values"

def test_range_negative_indexing():
    r = Range(1, 11, 2)