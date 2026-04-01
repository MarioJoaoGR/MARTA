
import pytest
from pymonet.box import Box

def test_valid_inputs():
    # Test with an integer
    box_int = Box(123)
    assert box_int.value == 123
    
    # Test with a string
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"
    
    # Test with a list
    box_list = Box([1, 2, 3])
    assert box_list.value == [1, 2, 3]
    
    # Test with a dictionary
    box_dict = Box({"key": "value"})
    assert box_dict.value == {"key": "value"}
    
    # Test with a nested structure
    nested_box = Box(Box(1))
    assert nested_box.value.value == 1
