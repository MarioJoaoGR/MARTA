
import pytest
from pymonet.validation import Validation

# Test valid input scenario
def test_valid_input():
    success_validation = Validation(value=10, errors=[])
    assert success_validation.is_success() is True
    assert success_validation.value == 10

# Test edge case where validation fails with None as the value and a list containing 'Error message'
def test_edge_case_none():
    failure_validation = Validation(value=None, errors=['Error message'])
    assert failure_validation.is_success() is False
    assert failure_validation.errors == ['Error message']

# Test invalid input where validation fails with an error but no value is provided
def test_invalid_input():
    invalid_validation = Validation(value=None, errors=[ValueError('Invalid input')])
    assert invalid_validation.is_success() is False
    assert len(invalid_validation.errors) == 1
    assert isinstance(invalid_validation.errors[0], ValueError)
