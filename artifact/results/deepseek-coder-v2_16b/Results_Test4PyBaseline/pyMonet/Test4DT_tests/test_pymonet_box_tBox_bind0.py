# Module: pymonet.box
import pytest
from pymonet.box import Box

# Test initialization with different types of data
def test_init():
    # Initialize with an integer
    box = Box(42)
    assert box.value == 42
    
    # Initialize with a string
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"
    
    # Initialize with a list
    box_list = Box([1, 2, 3])
    assert box_list.value == [1, 2, 3]

# Test bind method with different mappers
def test_bind():
    def double_value(x):
        return x * 2
    
    # Bind a function that doubles the value
    box = Box(5)
    bound_box = box.bind(double_value)
    assert bound_box == 10
    
    # Bind a function that adds one to the value
    def add_one(x):
        return x + 1
    
    box = Box(42)
    mapped_box = box.bind(add_one)
    assert mapped_box == 43

# Test bind method with a function that returns a different type
def test_bind_different_type():
    def to_string(x):
        return str(x)
    
    # Bind a function that converts the value to string
    box = Box(5)
    bound_box = box.bind(to_string)
    assert bound_box == "5"

# Test bind method with a function that returns None (for void functions)
def test_bind_void_function():
    def print_value(x):
        print(x)
    
    # Bind a function that prints the value
    box = Box("Hello")
    bound_box = box.bind(print_value)
    assert bound_box is None  # The actual type of the returned value from the void function should be checked in an interactive session or further code
