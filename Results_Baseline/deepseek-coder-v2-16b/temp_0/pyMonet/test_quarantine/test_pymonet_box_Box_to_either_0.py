
import pytest
from pymonet.box import Box
from pymonet.either import Right

# Test creating a Box with an integer value
def test_create_box_with_integer():
    box = Box(123)
    assert hasattr(box, 'value'), "Box should have a 'value' attribute"
    assert getattr(box, 'value') == 123

# Test creating a Box with a string value
def test_create_box_with_string():
    box = Box("Hello, World!")
    assert hasattr(box, 'value'), "Box should have a 'value' attribute"
    assert getattr(box, 'value') == "Hello, World!"

# Test mapping the stored value to another type using `map`
def test_map_value():
    box = Box(123)
    mapped_box = box.map(lambda x: str(x))
    assert isinstance(mapped_box.value, str), "Mapped box should be a string"
    assert mapped_box.value == "123"

# Test binding a function to the stored value using `bind`
def test_bind_function():
    box = Box("Hello")
    bound_box = box.bind(lambda x: str.upper(x))
    assert bound_box.value == "HELLO"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_box_Box_to_either_0
pyMonet/Test4DT_tests/test_pymonet_box_Box_to_either_0.py:29:11: E1101: Instance of 'str' has no 'value' member (no-member)


"""