
import pytest
from pymonet.box import Box

def test_invalid_inputs():
    # Test creating a Box with None as input
    box_none = Box(None)
    assert box_none.value is None, "Expected value to be None"
    
    # Test creating a Box with an empty string as input
    box_empty_string = Box("")
    assert box_empty_string.value == "", "Expected value to be an empty string"
    
    # Test creating a Box with a list as input
    box_list = Box([1, 2, 3])
    assert isinstance(box_list.value, list), "Expected value to be a list"
    
    # Test creating a Box with a dictionary as input
    box_dict = Box({"key": "value"})
    assert isinstance(box_dict.value, dict), "Expected value to be a dictionary"
