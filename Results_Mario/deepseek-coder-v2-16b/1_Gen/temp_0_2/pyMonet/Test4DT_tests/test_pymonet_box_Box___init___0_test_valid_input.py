
import pytest
from pymonet.box import Box

def test_valid_input():
    # Test with integer value
    box_int = Box(123)
    assert box_int.value == 123
    
    # Test with string value
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"
    
    # Test with float value
    box_float = Box(123.45)
    assert box_float.value == 123.45
    
    # Test with list value
    box_list = Box([1, 2, 3])
    assert box_list.value == [1, 2, 3]
    
    # Test with dictionary value
    box_dict = Box({"key": "value"})
    assert box_dict.value == {"key": "value"}
    
    # Test with None value
    box_none = Box(None)
    assert box_none.value is None
