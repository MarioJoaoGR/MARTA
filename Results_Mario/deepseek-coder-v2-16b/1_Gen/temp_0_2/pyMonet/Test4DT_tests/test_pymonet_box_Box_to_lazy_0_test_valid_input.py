
import pytest
from pymonet.box import Box

def test_valid_input():
    # Test with integer value
    box = Box(42)
    assert box.value == 42
    
    # Test with string value
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"
