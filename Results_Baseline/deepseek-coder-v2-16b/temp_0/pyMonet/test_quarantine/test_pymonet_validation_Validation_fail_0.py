
# Module: pymonet.validation
import pytest
from pymonet.validation import Validation

# Test initialization of successful Validation instance
def test_successful_initialization():
    val = Validation(10, [])
    assert val.value == 10
    assert val.errors == []

# Test initialization of failed Validation instance
def test_failed_initialization():
    val_with_errors = Validation(None, ["Error message"])
    assert val_with_errors.value is None
    assert val_with_errors.errors == ["Error message"]

# Test adding an error to the errors list
def test_add_error():
    val = Validation(None, [])
    val.add_error("Error occurred")
    assert val.errors == ["Error occurred"]

# Test applying a function using map method
def double(x):
    return x * 2

def test_map_method():
    val = Validation(5, [])
    mapped_val = val.map(double)
    assert mapped_val.value == 10
    assert mapped_val.errors == []

# Test checking if the validation was successful
def test_is_success():
    val = Validation(42, [])
    assert val.is_success() is True

    val_with_error = Validation(None, ["Error occurred"])
    assert val_with_error.is_success() is False

# Test string representation of the Validation instance
def test_str_representation():
    val = Validation(42, [])
    assert str(val) == "Validation.success[42]"

    val_with_error = Validation(None, ["Error occurred"])
    assert str(val_with_error) == "Validation.fail[None, ['Error occurred']]"

# Test returning a failed Validation with None as value and errors list
def test_validation_fail():
    failed_validation = Validation.fail(["Error message"])
    assert failed_validation.value is None
    assert failed_validation.errors == ["Error message"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_fail_0
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_fail_0.py:21:4: E1101: Instance of 'Validation' has no 'add_error' member (no-member)


"""