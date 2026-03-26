# Module: pymonet.box
import pytest
from pymonet.box import Box

# Test initialization with different types of data
def test_init():
    box_int = Box(123)
    assert box_int.value == 123
    
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"
    
    box_list = Box([1, 2, 3])
    assert isinstance(box_list.value, list) and box_list.value == [1, 2, 3]

# Test the map method to apply a function to the stored value
def test_map():
    def square(x):
        return x * x
    
    box = Box(5)
    mapped_box = box.map(square)
    assert mapped_box.value == 25

# Test equality comparison between two Box instances
def test_equality():
    box1 = Box(789)
    box2 = Box(789)
    assert box1 == box2
    
    box3 = Box(101112)
    assert not (box1 == box3)

# Test inequality comparison between two Box instances
def test_inequality():
    box1 = Box(456)
    box2 = Box(789)
    assert box1 != box2
    
    box3 = Box(456)
    assert not (box1 != box3)

# Test the map method with a function that returns a different type of data
def test_map_different_type():
    def to_string(x):
        return str(x)
    
    box = Box(456)
    mapped_box = box.map(to_string)
    assert isinstance(mapped_box.value, str) and mapped_box.value == "456"

# Test the map method with a function that returns None (or equivalent)
def test_map_returns_none():
    def return_none(x):
        return None
    
    box = Box("Hello")
    mapped_box = box.map(return_none)
    assert mapped_box.value is None

# Test the map method with a function that raises an error (if applicable)
def test_map_raises_error():
    def raise_error(x):
        raise ValueError("Test Error")
    
    box = Box(123)
    with pytest.raises(ValueError):
        mapped_box = box.map(raise_error)
