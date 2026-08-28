# Module: pymonet.validation
import pytest
from pymonet.validation import Validation

# Test creating a successful Validation instance
def test_successful_validation():
    val_success = Validation(10, [])
    assert val_success.value == 10

# Test creating a failed Validation instance
def test_failed_validation():
    val_failure = Validation(None, ['Error message'])
    assert val_failure.errors == ['Error message']

# Test checking if the validation is successful
def test_is_success():
    val_success = Validation(10, [])
    val_failure = Validation(None, ['Error message'])
    
    if val_success.is_success():
        assert val_success.value == 10
    else:
        assert val_failure.errors == ['Error message']

# Test comparing two Validation instances for equality when they are the same
def test_validation_equality_same():
    val3 = Validation(5, ['First error', 'Second error'])
    val4 = Validation(5, ['First error', 'Second error'])
    assert val3 == val4

# Test comparing two Validation instances for equality when they are different
def test_validation_equality_different():
    val5 = Validation(None, [])
    val6 = Validation(10, ['Error message'])
    assert not (val5 == val6)
