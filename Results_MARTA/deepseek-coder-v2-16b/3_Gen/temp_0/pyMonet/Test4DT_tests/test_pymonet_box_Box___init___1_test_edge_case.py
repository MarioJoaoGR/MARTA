
from pymonet.box import Box
import pytest

def test_edge_case():
    # Test None value
    box_none = Box(None)
    assert box_none.value is None
    
    # Test empty list
    box_empty_list = Box([])
    assert box_empty_list.value == []
    
    # Test boundary values (e.g., 0, "", etc.)
    box_zero = Box(0)
    assert box_zero.value == 0
    
    box_empty_string = Box("")
    assert box_empty_string.value == ""
