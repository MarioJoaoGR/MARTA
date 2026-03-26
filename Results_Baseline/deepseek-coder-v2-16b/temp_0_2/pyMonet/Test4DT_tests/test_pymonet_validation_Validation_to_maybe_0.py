# Module: pymonet.validation
# test_validation.py
import pytest
from pymonet.validation import Validation
from pymonet.maybe import Maybe

# Test creating a Validation instance with a success value
def test_create_validation_with_success_value():
    val = Validation(10, [])
    assert val.value == 10
    assert val.errors == []

# Test adding an error to the Validation instance
def test_add_error_to_validation():
    val = Validation(None, [])
    val.errors.append("Invalid input")
    assert val.errors == ["Invalid input"]

# Test checking if the Validation is successful when it has no errors
def test_is_success_true():
    val_success = Validation(10, [])
    assert val_success.is_success() is True

# Test checking if the Validation is successful when it has errors
def test_is_success_false():
    val_with_errors = Validation(None, ["Error message"])
    assert val_with_errors.is_success() is False

# Test transforming Validation to Maybe when it is successful
def test_to_maybe_success():
    val = Validation(10, [])
    maybe_val = val.to_maybe()
    assert isinstance(maybe_val, Maybe)
    assert not maybe_val.is_nothing

# Test transforming Validation to Maybe when it has errors
def test_to_maybe_failure():
    val_with_errors = Validation(None, ["Error message"])
    maybe_val_fail = val_with_errors.to_maybe()
    assert isinstance(maybe_val_fail, Maybe)
    assert maybe_val_fail.is_nothing
