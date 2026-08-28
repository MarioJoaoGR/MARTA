
import pytest
from pymonet.box import Box

# Test valid input scenario
def test_valid_input():
    box = Box(42)
    assert box.value == 42

# Test edge case scenario with None, empty lists, and boundary values
def test_edge_case():
    box_none = Box(None)
    assert box_none.value is None
    
    box_empty_list = Box([])
    assert box_empty_list.value == []

# Test invalid input scenario with error handling
def test_invalid_input():
    try:
        box_invalid = Box('string')
    except TypeError as e:
        assert str(e) == "expected type for value is <class 'NoneType'>"
