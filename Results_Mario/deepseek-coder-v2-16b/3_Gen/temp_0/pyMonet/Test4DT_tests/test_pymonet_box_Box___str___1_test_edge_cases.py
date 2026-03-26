
import pytest
from pymonet.box import Box

def test_edge_cases():
    # Test None value
    box_none = Box(None)
    assert str(box_none) == 'Box[value=None]'
    
    # Test empty string value
    box_empty_string = Box('')
    assert str(box_empty_string) == 'Box[value=]'
    
    # Test zero integer value
    box_zero_int = Box(0)
    assert str(box_zero_int) == 'Box[value=0]'
    
    # Test empty list value
    box_empty_list = Box([])
    assert str(box_empty_list) == 'Box[value=[]]'
    
    # Test empty dictionary value
    box_empty_dict = Box({})
    assert str(box_empty_dict) == 'Box[value={}]'
