
# Module: flutes.iterator
# test_range.py
from flutes.iterator import Range
import pytest

@pytest.fixture
def range_instance():
    return Range(1, 10 + 1)

def test_range_creation():
    r = Range(1, 10 + 1)
    assert isinstance(r, Range), "Range instance should be created successfully"

def test_index_access():
    r = Range(1, 10 + 1)
    assert r[0] == 1, "Indexing at position 0 should return the start value"
    assert r[2] == 3, "Indexing at position 2 should return the third element in the sequence"