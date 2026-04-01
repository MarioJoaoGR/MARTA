
import pytest
from pymonet.box import Box

def test_edge_cases():
    # Test with None value
    box_none = Box(None)
    assert box_none.value is None
    
    # Test with empty list
    box_empty = Box([])
    assert box_empty.value == []
