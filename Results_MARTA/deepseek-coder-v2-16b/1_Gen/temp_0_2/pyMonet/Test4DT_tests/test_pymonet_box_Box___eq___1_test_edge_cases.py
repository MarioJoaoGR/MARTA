
import pytest
from pymonet.box import Box

def test_edge_cases():
    # Test with None
    box1 = Box(None)
    assert box1.value is None
    
    # Test with empty list
    empty_list_box = Box([])
    assert isinstance(empty_list_box.value, list) and not empty_list_box.value
    
    # Test boundary values (e.g., 0, "", etc.) can be added similarly by creating a Box with these values
