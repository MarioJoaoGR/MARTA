
import pytest
from pymonet.box import Box

# Test valid inputs
def test_valid_inputs():
    box = Box(42)
    assert box.value == 42
    
    box_str = Box('Hello, World!')
    assert box_str.value == 'Hello, World!'
    
    box_list = Box([1, 2, 3])
    assert box_list.value == [1, 2, 3]

# Test edge cases
def test_edge_cases():
    box_none = Box(None)
    assert box_none.value is None
    
    box_empty_list = Box([])
    assert box_empty_list.value == []

# Test invalid inputs
def test_invalid_inputs():
    with pytest.raises(Exception):
        box = Box()
