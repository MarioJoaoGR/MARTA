
import pytest
from pymonet.validation import Validation

def test_successful_validation():
    valid = Validation(value=10, errors=[])
    assert valid.value == 10
    assert valid.errors == []

def test_failed_validation():
    invalid = Validation(value=None, errors=['Error message 1', 'Error message 2'])
    assert invalid.value is None
    assert invalid.errors == ['Error message 1', 'Error message 2']

def test_validation_comparison():
    val1 = Validation(42, [])
    val2 = Validation(42, [])
    assert val1 == val2

def test_error_handling():
    with pytest.raises(ValueError):
        raise ValueError("Test Error")
