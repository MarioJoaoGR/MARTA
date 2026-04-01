
import pytest
from pymonet.box import Box

def test_edge_cases():
    # Test None value
    box_none = Box(None)
    assert box_none.value is None
    
    # Test empty list
    box_empty_list = Box([])
    assert box_empty_list.value == []
    
    # Test boundary values (e.g., 0, "", [], {})
    box_zero = Box(0)
    assert box_zero.value == 0
    
    box_empty_string = Box("")
    assert box_empty_string.value == ""
    
    box_empty_dict = Box({})
    assert box_empty_dict.value == {}
    
    # Test non-default boundary values (e.g., 1, "hello", [1], {"key": "value"})
    box_one = Box(1)
    assert box_one.value == 1
    
    box_string = Box("hello")
    assert box_string.value == "hello"
    
    box_list = Box([1])
    assert box_list.value == [1]
    
    box_dict = Box({"key": "value"})
    assert box_dict.value == {"key": "value"}
