
import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    # Test when no arguments are provided
    with pytest.raises(ValueError):
        Range()
    
    # Test when more than three arguments are provided
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)
    
    # Test when one argument is provided (should be treated as end)
    r = Range(10)
    assert r[0] == 0
    assert len(r) == 10
    
    # Test when two arguments are provided (start and end)
    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[2] == 3
    assert len(r) == 10
    
    # Test when three arguments are provided (start, end, and step)
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 5
    assert len(r) == 5
