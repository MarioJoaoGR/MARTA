# Module: pymonet.validation
import pytest
from pymonet.validation import Validation

# Test creating a successful Validation instance
def test_successful_creation():
    val = Validation(value=10, errors=[])
    assert val.value == 10
    assert val.errors == []

# Test creating a failed Validation instance with an error message
def test_failed_creation():
    val_with_errors = Validation(value=None, errors=["Error message"])
    assert val_with_errors.value is None
    assert val_with_errors.errors == ["Error message"]

# Test checking if a successful Validation instance is successful
def test_is_success_true():
    val = Validation(value=10, errors=[])
    assert val.is_success() is True

# Test checking if a failed Validation instance is not successful
def test_is_success_false():
    val_with_errors = Validation(value=None, errors=["Error message"])
    assert val_with_errors.is_success() is False

# Test string representation of a successful Validation instance
def test_str_successful():
    val = Validation(value=10, errors=[])
    assert str(val) == "Validation.success[10]"

# Test string representation of a failed Validation instance
def test_str_failed():
    val_with_errors = Validation(value=None, errors=["Error message"])
    assert str(val_with_errors) == "Validation.fail[None, ['Error message']]"

# Test comparing two equal Validation instances for equality
def test_equal_instances():
    validation1 = Validation(value="success", errors=[])
    validation2 = Validation(value="success", errors=[])
    assert validation1 == validation2

# Test comparing two unequal Validation instances for inequality
def test_unequal_instances():
    validation1 = Validation(value="success", errors=[])
    validation3 = Validation(value="failure", errors=["error"])
    assert not (validation1 == validation3)
