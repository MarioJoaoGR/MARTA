# Module: pymonet.either
import pytest
from pymonet.either import Right
from pymonet.validation import Validation

# Test cases for the to_validation method of the Right class

def test_to_validation_basic():
    right = Right(42)
    val = right.to_validation()
    assert val.value == 42

def test_to_validation_with_string():
    right_str = Right("success")
    val_str = right_str.to_validation()
    assert val_str.value == "success"

def test_to_validation_with_none():
    right_none = Right(None)
    val_none = right_none.to_validation()
    assert val_none.value is None

def test_to_validation_with_empty_list():
    empty_right = Right([])
    val_empty = empty_right.to_validation()
    assert val_empty.value == []

def test_to_validation_with_error():
    right_error = Right("error")
    val_error = right_error.to_validation()
    assert val_error.value == "error"

# Additional edge cases can be added to cover more scenarios
