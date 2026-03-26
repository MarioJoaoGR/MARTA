
import pytest
from flutes.iterator import Range

# Test cases for the Range class initialization and indexing
def test_range_creation():
    r = Range(10)
    assert r[0] == 0, "Indexing should start from 0 when only end is provided"
    assert r[2] == 2, "Indexing with step size 1 should return expected values"
    assert r[4] == 4, "Indexing with step size 1 should return expected values"

def test_range_creation_with_start_and_end():
    r = Range(1, 10 + 1)
    assert r[0] == 1, "Indexing should start from the provided start value"
    assert r[2] == 3, "Indexing with step size 1 should return expected values"
    assert r[4] == 5, "Indexing with step size 1 should return expected values"

def test_range_creation_with_start_end_and_step():
    r = Range(1, 11, 2)
    assert r[0] == 1, "Indexing should start from the provided start value"
    assert r[2] == 5, "Indexing with step size 2 should return expected values"
    assert r[4] == 9, "Indexing with step size 2 should return expected values"

def test_range_negative_indexing():
    r = Range(1, 11, 2)
    assert r[-1] == 9, "Negative indexing should work correctly and map to the positive index from the end"
    assert r[-3] == 5, "Negative indexing should work correctly and map to the positive index from the end"
    assert r[-5] == 1, "Negative indexing should work correctly and map to the positive index from the end"

def test_range_slice_notation():
    r = Range(1, 11, 2)