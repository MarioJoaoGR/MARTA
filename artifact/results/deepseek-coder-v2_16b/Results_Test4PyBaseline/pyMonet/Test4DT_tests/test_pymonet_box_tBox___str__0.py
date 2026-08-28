
import pytest
from pymonet.box import Box

# Test creating a Box with an integer value
def test_create_box_with_integer():
    box = Box(42)
    assert box.value == 42

# Test creating a Box with a string value
def test_create_box_with_string():
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"

# Test the map method to transform the value inside the Box
def test_map_method():
    def add_one(x):
        return x + 1
    
    box = Box(42)
    mapped_box = box.map(add_one)
    assert mapped_box.value == 43

# Test the bind method to transform the value inside the Box
def test_bind_method():
    def double_value(x):
        return x * 2
    
    box = Box(5)
    bound_box = box.bind(double_value)