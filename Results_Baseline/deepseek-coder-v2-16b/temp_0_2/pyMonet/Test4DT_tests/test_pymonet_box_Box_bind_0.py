# Module: pymonet.box
import pytest
from pymonet.box import Box

# Test case for creating a Box with an Integer Value
def test_create_box_with_integer():
    box = Box(123)
    assert box.value == 123

# Test case for creating a Box with a String Value
def test_create_box_with_string():
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"

# Test case for applying a function to the stored value
def test_apply_function_to_stored_value():
    def square(x):
        return x * x
    box = Box(5)
    mapped_box = box.bind(square)
    assert mapped_box == 25

# Test case for comparing two Boxes for Equality
def test_compare_boxes_for_equality():
    box1 = Box(456)
    box2 = Box(456)
    assert box1 == box2

# Test case for example usage with a String Value
def test_example_usage_with_string_value():
    box_str = Box("Hello, World!")
    mapped_box = box_str.bind(lambda x: str(x))
    assert mapped_box == "Hello, World!"

# Test case for example usage with an Integer Value
def test_example_usage_with_integer_value():
    box = Box(123)
    mapped_box = box.bind(lambda x: str(x))
    assert mapped_box == "123"

# Test case for example usage with equality check between different types and values
def test_example_usage_with_equality_check():
    box1 = Box(456)
    box2 = Box("Hello, World!")
    assert not (box1 == box2)
