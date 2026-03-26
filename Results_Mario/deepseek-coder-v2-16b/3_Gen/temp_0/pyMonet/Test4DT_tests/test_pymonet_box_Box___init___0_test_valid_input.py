
import pytest
from pymonet.box import Box

def test_valid_input():
    # Test creating a Box with an integer value
    box_int = Box(123)
    assert isinstance(box_int, Box)
    assert box_int.value == 123
    
    # Test creating a Box with a string value
    box_str = Box("Hello, World!")
    assert isinstance(box_str, Box)
    assert box_str.value == "Hello, World!"
    
    # Test creating a Box with a float value
    box_float = Box(123.45)
    assert isinstance(box_float, Box)
    assert box_float.value == 123.45
    
    # Test creating a Box with a list value
    box_list = Box([1, 2, 3])
    assert isinstance(box_list, Box)
    assert box_list.value == [1, 2, 3]
    
    # Test creating a Box with a dictionary value
    box_dict = Box({"key": "value"})
    assert isinstance(box_dict, Box)
    assert box_dict.value == {"key": "value"}
    
    # Test creating a Box with a boolean value
    box_bool = Box(True)
    assert isinstance(box_bool, Box)
    assert box_bool.value is True
