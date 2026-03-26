
import pytest
from flutes.iterator import Range

def test_range_indexing():
    # Test with end value only
    r1 = Range(10)
    assert r1[0] == 0
    assert r1[2] == 2
    assert r1[4] == 4
    
    # Test with start, end values
    r2 = Range(1, 10 + 1)
    assert r2[0] == 1
    assert r2[2] == 3
    assert r2[4] == 5
    
    # Test with start, end, and step values
    r3 = Range(1, 11, 2)
    assert r3[0] == 1
    assert r3[1] == 3
    assert r3[2] == 5
    
    # Test negative indexing (if supported by the implementation)
    if hasattr(r3, "__getitem__"):
        assert r3[-1] == 9  # Assuming the last element index is -1 for step of 2 from 1 to 10
        assert r3[-2] == 7  # Second last element
