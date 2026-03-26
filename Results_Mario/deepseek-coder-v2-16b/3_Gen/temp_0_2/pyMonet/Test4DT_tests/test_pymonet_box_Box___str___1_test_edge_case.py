
import pytest
from pymonet.box import Box

def test_edge_case():
    # Test None
    box1 = Box(None)
    assert str(box1) == 'Box[value=None]'
    
    # Test empty list
    box2 = Box([])
    assert str(box2) == 'Box[value=[]]'
    
    # Test non-empty string
    box3 = Box('Hello')
    assert str(box3) == 'Box[value=Hello]'
