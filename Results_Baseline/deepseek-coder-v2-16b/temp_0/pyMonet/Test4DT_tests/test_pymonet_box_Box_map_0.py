# Module: pymonet.box
# test_box.py
from pymonet.box import Box
import pytest

# Test cases for the __init__ method
def test_box_init():
    box = Box(123)
    assert box.value == 123

    text_box = Box("Hello, World!")
    assert text_box.value == "Hello, World!"

# Test cases for the map method
def test_map():
    box = Box(123)
    mapped_box = box.map(lambda x: str(x))
    assert isinstance(mapped_box.value, str)
    assert mapped_box.value == "123"

    text_box = Box("Hello, World!")
    mapped_text_box = text_box.map(lambda x: x.upper())
    assert isinstance(mapped_text_box.value, str)
    assert mapped_text_box.value == "HELLO, WORLD!"

# Edge cases for the map method
def test_map_edge():
    empty_box = Box(None)
    mapped_empty_box = empty_box.map(lambda x: str(x))
    assert isinstance(mapped_empty_box.value, str)
    assert mapped_empty_box.value == "None"

# Test cases for the map method with different types
def test_map_different_types():
    box = Box([1, 2, 3])
    mapped_box = box.map(lambda x: type(x))
    assert isinstance(mapped_box.value, type)
    assert mapped_box.value == list

# Test cases for the map method with exceptions
def test_map_exceptions():
    box = Box(123)
    with pytest.raises(Exception):
        mapped_box = box.map(lambda x: 1 / (x - 123))  # Division by zero error
