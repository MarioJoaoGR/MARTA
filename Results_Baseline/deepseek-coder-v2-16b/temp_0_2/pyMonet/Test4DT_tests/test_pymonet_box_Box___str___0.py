# Module: pymonet.box
import pytest
from pymonet.box import Box

# Test initialization with different types of values
def test_init():
    box = Box(123)
    assert box.value == 123
    
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"

# Test the __str__ method
def test_str():
    box = Box(123)
    assert str(box) == 'Box[value=123]'
    
    box_str = Box("Hello, World!")
    assert str(box_str) == 'Box[value=Hello, World!]'

# Test the map method
def test_map():
    box = Box(123)
    mapped_box = box.map(lambda x: str(x))
    assert mapped_box.value == "123"
    
    box_str = Box("Hello, World!")
    mapped_box_str = box_str.map(lambda x: x.upper())
    assert mapped_box_str.value == "HELLO, WORLD!"

# Test equality between two Boxes with the same value
def test_equality():
    box1 = Box(456)
    box2 = Box(456)
    assert box1 == box2
    
    # Different values should not be equal
    box3 = Box(789)
    assert not (box1 == box3)

# Test inequality between two Boxes with different values
def test_inequality():
    box1 = Box(456)
    box2 = Box(789)
    assert box1 != box2
    
    # Same value should be equal
    box3 = Box(456)
    assert not (box1 != box3)
