
import pytest
from pymonet.box import Box
from pymonet.either import Right

# Test creating a Box with an integer value
def test_create_box_with_integer():
    box = Box(123)
    assert getattr(box, 'value') == 123

# Test creating a Box with a string value
def test_create_box_with_string():
    box = Box("Hello, World!")
    assert getattr(box, 'value') == "Hello, World!"

# Test mapping the stored value to another type using `map`
def test_map_value():
    box = Box(123)
    mapped_box = box.map(lambda x: str(x))
    assert isinstance(mapped_box.value, str)
    assert getattr(mapped_box, 'value') == "123"

# Test binding a function to the stored value using `bind`
def test_bind_function():
    box = Box("Hello")
    bound_box = box.bind(lambda x: str.upper(x))