
import pytest
from pymonet.box import Box

# Test scenarios
def test_valid_input():
    box1 = Box(123)
    box2 = Box(123)
    assert box1 == box2
    assert box1.value == 123
    assert box2.value == 123

def test_edge_case():
    box_none = Box(None)
    box_empty = Box([])
    assert box_none.value is None
    assert len(box_empty.value) == 0

def test_invalid_input():
    box_string = Box('string')
    box_dict = Box({})
    assert isinstance(box_string.value, str)
    assert isinstance(box_dict.value, dict)
