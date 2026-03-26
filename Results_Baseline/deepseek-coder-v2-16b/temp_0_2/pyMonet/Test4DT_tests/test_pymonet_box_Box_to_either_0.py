# Module: pymonet.box
import pytest
from pymonet.box import Box
from pymonet.either import Right, Left

# Test initialization with different types of values
def test_init():
    box_int = Box(123)
    assert box_int.value == 123
    
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"
    
    box_list = Box([1, 2, 3])
    assert isinstance(box_list.value, list) and box_list.value == [1, 2, 3]

# Test the to_either method
def test_to_either():
    box = Box("data")
    either = box.to_either()
    assert isinstance(either, Right)
    assert either.value == "data"

# Test equality of two boxes with the same value
def test_equality():
    box1 = Box(456)
    box2 = Box(456)
    assert box1 == box2

# Test inequality of two boxes with different values
def test_inequality():
    box1 = Box(123)
    box2 = Box("Hello")
    assert not (box1 == box2)

# Test the map method on a function that transforms the value
def test_map():
    box = Box(42)
    mapped_box = box.map(lambda x: str(x))
    assert isinstance(mapped_box, Box)
    assert mapped_box.value == "42"

# Test the map method with a function that does not change the value
def test_map_identity():
    box = Box("Hello")
    identity_box = box.map(lambda x: x)
    assert isinstance(identity_box, Box)
    assert identity_box.value == "Hello"
