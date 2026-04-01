
import pytest
from pymonet.box import Box

def test_valid_inputs():
    box1 = Box(456)
    box2 = Box(456)
    not_a_box = 'Not a Box'
    
    assert box1 == box2
    assert not (box1 == not_a_box)
