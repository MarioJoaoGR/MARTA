
import pytest
from superstring.superstring import SuperStringSubstring

def test_edge_cases():
    # Test with None values
    substr = SuperStringSubstring(None, None, None)
    assert substr._base is None
    assert substr._start_index is None
    assert substr._end_index is None
    
    # Test with empty string and indices set to 0
    substr = SuperStringSubstring("", 0, 0)
    assert substr._base == ""
    assert substr._start_index == 0
    assert substr._end_index == 0
    
    # Test with valid base string and indices out of bounds
    substr = SuperStringSubstring("Hello", -1, len("Hello") + 1)
    assert substr._base == "Hello"
    assert substr._start_index == -1
    assert substr._end_index == len("Hello") + 1
    
    # Test with valid base string and indices within bounds
    substr = SuperStringSubstring("Hello", 1, 4)
    assert substr._base == "Hello"
    assert substr._start_index == 1
    assert substr._end_index == 4
