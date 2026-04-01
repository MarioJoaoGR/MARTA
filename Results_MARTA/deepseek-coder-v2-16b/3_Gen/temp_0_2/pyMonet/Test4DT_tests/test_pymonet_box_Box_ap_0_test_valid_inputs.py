
import pytest
from pymonet.box import Box

def test_valid_inputs():
    # Test with integer value
    box1 = Box(123)
    assert box1.value == 123
    
    # Test with string value
    box2 = Box("Hello, World!")
    assert box2.value == "Hello, World!"
    
    # Test with list value
    box3 = Box([1, 2, 3])
    assert box3.value == [1, 2, 3]
    
    # Test with dictionary value
    box4 = Box({"key": "value"})
    assert box4.value == {"key": "value"}
