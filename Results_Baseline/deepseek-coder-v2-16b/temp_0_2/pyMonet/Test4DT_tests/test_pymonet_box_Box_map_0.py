# Module: pymonet.box
import pytest
from pymonet.box import Box

# Test initialization of Box with different types of data
def test_init():
    box = Box(123)
    assert box.value == 123
    
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"

# Test map function with a lambda function that converts the value to string
def test_map():
    box = Box(123)
    mapped_box = box.map(lambda x: str(x))
    assert mapped_box.value == "123"
    
    box_str = Box("Hello, World!")
    mapped_box_str = box_str.map(lambda x: str(x))
    assert mapped_box_str.value == "Hello, World!"

# Test map function with a lambda function that converts the value to uppercase
def test_map_uppercase():
    box_str = Box("Hello, World!")
    uppercased_box_str = box_str.map(lambda x: x.upper())
    assert uppercased_box_str.value == "HELLO, WORLD!"

# Test map function with a lambda function that adds 1 to the value
def test_map_add_one():
    box = Box(123)
    incremented_box = box.map(lambda x: x + 1)
    assert incremented_box.value == 124

# Test map function with a lambda function that multiplies the value by 2
def test_map_multiply():
    box = Box(10)
    doubled_box = box.map(lambda x: x * 2)
    assert doubled_box.value == 20
