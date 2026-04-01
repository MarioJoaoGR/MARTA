
import pytest
from pymonet.box import Box

def test_valid_inputs():
    # Test with integer input
    box_int = Box(42)
    assert box_int.value == 42
    
    # Test with string input
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"
    
    # Test with float input
    box_float = Box(3.14)
    assert box_float.value == 3.14
    
    # Test with list input
    box_list = Box([1, 2, 3])
    assert box_list.value == [1, 2, 3]
    
    # Test with dictionary input
    box_dict = Box({"key": "value"})
    assert box_dict.value == {"key": "value"}
    
    # Test with None input
    box_none = Box(None)
    assert box_none.value is None
