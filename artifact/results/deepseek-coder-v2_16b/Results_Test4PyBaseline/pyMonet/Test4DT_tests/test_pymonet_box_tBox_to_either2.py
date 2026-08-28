
import pytest
from pymonet.box import Box
from pymonet.either import Right

# Test creating a Box with an integer
def test_create_box_with_integer():
    box = Box(42)
    assert box.value == 42

# Test creating a Box with a string
def test_create_box_with_string():
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"

# Test transforming the value in the Box using map
def test_map_function():
    def add_one(x):
        return x + 1
    
    box = Box(42)
    mapped_box = box.map(add_one)
    assert mapped_box.value == 43

# Test binding a function to transform the value in the Box
def test_bind_function():
    def double_value(x):
        return x * 2
    
    box = Box(5)
    bound_box = box.bind(double_value)