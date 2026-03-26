# Module: pymonet.box
import pytest
from pymonet.box import Box
from pymonet.maybe import Maybe

# Test initialization of Box with different types of data
def test_box_initialization():
    box_int = Box(123)
    assert box_int.value == 123
    
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"

# Test the to_maybe method of Box
def test_to_maybe():
    box = Box(42)
    maybe_box = box.to_maybe()
    assert not maybe_box.is_nothing
    assert maybe_box.value == 42

# Test the map method (assuming it exists and works as expected)
def test_map():
    box = Box(123)
    mapped_box = box.map(lambda x: str(x))
    assert mapped_box.value == "123"

# Test equality between two Boxes with the same value
def test_equality():
    box1 = Box(456)
    box2 = Box(456)
    assert box1 == box2

# Test inequality between two Boxes with different values
def test_inequality():
    box1 = Box(123)
    box2 = Box(456)
    assert not (box1 == box2)
