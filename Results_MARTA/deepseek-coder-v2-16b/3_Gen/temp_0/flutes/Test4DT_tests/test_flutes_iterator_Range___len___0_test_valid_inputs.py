
import pytest
from flutes.iterator import Range

def test_valid_inputs():
    # Test with one argument (end)
    r = Range(10)
    assert len(r) == 10
    
    # Test with two arguments (start, end)
    r = Range(1, 10 + 1)
    assert len(r) == 10
    
    # Test with three arguments (start, end, step)
    r = Range(1, 11, 2)
    assert len(r) == 5
