
import pytest
from pymonet.box import Box

def test_valid_input():
    box = Box(123)
    assert box.value == 123
    
    box = Box("Hello, World!")
    assert box.value == "Hello, World!"
