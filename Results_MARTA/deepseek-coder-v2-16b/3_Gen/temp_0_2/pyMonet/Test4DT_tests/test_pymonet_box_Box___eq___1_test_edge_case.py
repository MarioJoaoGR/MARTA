
import pytest
from pymonet.box import Box

def test_edge_case():
    # Test None and empty list edge cases
    box_none = Box(None)
    box_empty_list = Box([])
    
    assert box_none.value is None
    assert isinstance(box_empty_list, Box)
    assert box_empty_list.value == []
