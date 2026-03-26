
import pytest
from pymonet.box import Box

def test_edge_cases():
    # Test None input
    box_none = Box(None)
    assert box_none.value is None
    
    # Test empty string input
    box_empty_string = Box("")
    assert box_empty_string.value == ""
    
    # Test zero input
    box_zero = Box(0)
    assert box_zero.value == 0
    
    # Test boolean True input
    box_true = Box(True)
    assert box_true.value is True
    
    # Test boolean False input
    box_false = Box(False)
    assert box_false.value is False
