
import pytest
from pymonet.box import Box

def test_valid_input():
    # Test with an integer value
    box = Box(123)
    assert isinstance(box.value, int)
    assert box.value == 123
    
    # Test with a string value
    box = Box("Hello, World!")
    assert isinstance(box.value, str)
    assert box.value == "Hello, World!"
    
    # Test with a float value
    box = Box(123.45)
    assert isinstance(box.value, float)
    assert box.value == 123.45
    
    # Test with a list value
    box = Box([1, 2, 3])
    assert isinstance(box.value, list)
    assert box.value == [1, 2, 3]
    
    # Test with a dictionary value
    box = Box({"key": "value"})
    assert isinstance(box.value, dict)
    assert box.value == {"key": "value"}
    
    # Test with a boolean value
    box = Box(True)
    assert isinstance(box.value, bool)
    assert box.value is True
