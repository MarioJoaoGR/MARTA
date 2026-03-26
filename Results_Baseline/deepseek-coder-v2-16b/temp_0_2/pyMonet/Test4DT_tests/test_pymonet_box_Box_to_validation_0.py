# Module: pymonet.box
import pytest
from pymonet.box import Box
from pymonet.validation import Validation

# Test initialization of Box with different types of data
def test_box_initialization():
    box_int = Box(123)
    assert box_int.value == 123
    
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"

# Test the to_validation method of Box
def test_to_validation():
    box = Box(456)
    val = box.to_validation()
    assert isinstance(val, Validation)
    assert val.is_success()
    assert val.value == 456

# Test the to_validation method with a different type of data
def test_to_validation_different_type():
    box = Box("Hello")
    val = box.to_validation()
    assert isinstance(val, Validation)
    assert val.is_success()
    assert val.value == "Hello"

# Test the to_validation method with a nested structure
def test_to_validation_nested():
    box = Box([1, 2, 3])
    val = box.to_validation()
    assert isinstance(val, Validation)
    assert val.is_success()
    assert val.value == [1, 2, 3]
