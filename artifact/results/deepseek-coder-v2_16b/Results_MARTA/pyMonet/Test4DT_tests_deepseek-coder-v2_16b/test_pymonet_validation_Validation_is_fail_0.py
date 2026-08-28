
import pytest
from pymonet.validation import Validation

# Test initialization of a successful validation instance
def test_successful_initialization():
    valid = Validation(value=42, errors=[])
    assert not valid.is_fail()
    assert valid.value == 42

# Test initialization of a failed validation instance
def test_failed_initialization():
    invalid = Validation(value=None, errors=['Error message'])
    assert invalid.is_fail()
    assert invalid.value is None
    assert len(invalid.errors) == 1
    assert invalid.errors[0] == 'Error message'

# Test method to check if validation failed
def test_is_fail():
    success_validation = Validation(value=10, errors=[])
    assert not success_validation.is_fail()
    
    failure_validation = Validation(value=None, errors=['Error message'])
    assert failure_validation.is_fail()
