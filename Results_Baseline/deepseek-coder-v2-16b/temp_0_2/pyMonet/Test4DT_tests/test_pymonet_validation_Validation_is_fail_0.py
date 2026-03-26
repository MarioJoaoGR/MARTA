# Module: pymonet.validation
# test_validation.py
from pymonet.validation import Validation
import pytest

# Test creating a successful validation instance
def test_successful_validation():
    val = Validation(value=10, errors=[])
    assert val.value == 10
    assert not val.is_fail()

# Test creating a failed validation instance
def test_failed_validation():
    val_with_errors = Validation(value=None, errors=["Error message"])
    assert val_with_errors.errors == ["Error message"]
    assert val_with_errors.is_fail()

# Test the is_fail method with an empty errors list
def test_empty_errors():
    val = Validation(value=10, errors=[])
    assert not val.is_fail()

# Test the is_fail method with non-empty errors list
def test_non_empty_errors():
    val_with_errors = Validation(value=None, errors=["Error message"])
    assert val_with_errors.is_fail()

# Test creating a successful validation instance using the success factory method
def test_successful_validation_factory():
    val = Validation.success(10)
    assert val.value == 10
    assert not val.is_fail()

# Test creating a failed validation instance using the fail factory method
def test_failed_validation_factory():
    val_with_errors = Validation.fail(["Error message"])
    assert val_with_errors.errors == ["Error message"]
    assert val_with_errors.is_fail()
