
import pytest
from flutes.iterator import Range  # Assuming this is the correct import path

def test_invalid_inputs():
    with pytest.raises(ValueError):
        Range()  # No arguments provided
        Range(1, 2, 3, 4)  # More than three arguments provided
        Range(1)  # Only one argument provided (should be treated as stop only)

def test_range_creation():
    r = Range(10)
    assert isinstance(r, Range)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1
    assert r.length == 10

def test_range_creation_with_start_stop():
    r = Range(1, 10)
    assert isinstance(r, Range)
    assert r.l == 1
    assert r.r == 10
    assert r.step == 1
    assert r.length == 9

def test_range_creation_with_start_stop_step():
    r = Range(1, 11, 2)
    assert isinstance(r, Range)
    assert r.l == 1
    assert r.r == 11
    assert r.step == 2
    assert r.length == 5
