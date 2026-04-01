
import pytest
from pymonet.box import Box

def test_valid_input():
    box1 = Box(5)
    box2 = Box('Hello, World!')
    
    assert box1.value == 5
    assert box2.value == 'Hello, World!'
