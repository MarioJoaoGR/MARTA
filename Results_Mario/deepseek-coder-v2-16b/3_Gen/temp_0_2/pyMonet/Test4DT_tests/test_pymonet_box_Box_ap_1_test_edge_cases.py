
import pytest
from pymonet.box import Box

def test_edge_cases():
    # Test with None
    box_none = Box(None)
    assert box_none.value is None
    
    # Test with empty list
    box_empty_list = Box([])
    assert box_empty_list.value == []
    
    # Test with a boundary value (e.g., 0 or an empty string)
    box_zero = Box(0)
    assert box_zero.value == 0
    
    box_empty_string = Box("")
    assert box_empty_string.value == ""
