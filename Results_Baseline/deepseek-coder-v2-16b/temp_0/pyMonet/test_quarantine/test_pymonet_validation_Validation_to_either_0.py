
# Module: pymonet.validation
import pytest
from pymonet.validation import Validation
from pymonet.either import Left, Right

# Test initialization with no errors
def test_init_no_errors():
    val = Validation(10, [])
    assert val.value == 10
    assert val.errors == []

# Test initialization with errors
def test_init_with_errors():
    val = Validation(None, ["Error message"])
    assert val.value is None
    assert val.errors == ["Error message"]

# Test adding an error to the validation instance
def test_add_error():
    val = Validation(None, [])
    val.add_error("Error occurred")  # Corrected method call
    assert val.errors == ["Error occurred"]

# Test mapping a function over the validation value
def test_map():
    def double(x):
        return x * 2
    
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

# Test converting validation to Either monad when successful
def test_to_either_success():
    val = Validation(42, [])
    either_val = val.to_either()
    assert isinstance(either_val, Right)
    assert either_val.value == 42

# Test converting validation to Either monad when failed
def test_to_either_failure():
    val = Validation(None, ["Error occurred"])
    either_val = val.to_either()
    assert isinstance(either_val, Left)
    assert either_val.value == ["Error occurred"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_either_0
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_either_0.py:22:4: E1101: Instance of 'Validation' has no 'add_error' member (no-member)


"""