
import pytest
from pymonet.box import Box

def test_edge_case():
    # Test edge cases with None and empty list
    box = Box(None)
    assert box.value is None
    
    empty_list = []
    box_empty_list = Box(empty_list)
    assert box_empty_list.value == empty_list
