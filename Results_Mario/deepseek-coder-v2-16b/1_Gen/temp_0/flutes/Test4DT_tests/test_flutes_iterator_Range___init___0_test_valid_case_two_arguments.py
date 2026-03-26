
import pytest
from flutes.iterator import Range

def test_valid_case_two_arguments():
    # Test when only end is provided (start defaults to 0, step defaults to 1)
    r = Range(10)
    assert r[0] == 0
    assert len(r) == 10
    
    # Test when start and end are provided (step defaults to 1)
    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5
    assert len(r) == 10
    
    # Test when start, end, and step are provided
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 5
    assert r[4] == 9
    assert len(r) == 5
