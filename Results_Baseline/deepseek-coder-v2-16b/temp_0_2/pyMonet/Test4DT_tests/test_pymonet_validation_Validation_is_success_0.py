# Module: pymonet.validation
import pytest
from pymonet.validation import Validation

# Test case to check if the Validation instance is created with a value and an empty error list
def test_initialization():
    val = Validation(10, [])
    assert val.value == 10
    assert val.errors == []

# Test case to check if the is_success method returns True for an empty errors list
def test_is_success_true():
    val = Validation(10, [])
    assert val.is_success() is True

# Test case to check if the is_success method returns False for a non-empty errors list
def test_is_success_false():
    val = Validation(None, ["Error message"])
    assert val.is_success() is False

# Test case to check if adding an error makes is_success return False
def test_adding_error():
    val = Validation(10, [])
    val.errors.append("New Error")
    assert len(val.errors) == 1
    assert val.is_success() is False

# Test case to check if the is_success method works correctly with a pre-filled errors list
def test_initial_error():
    val = Validation(None, ["Initial Error"])
    assert val.is_success() is False
