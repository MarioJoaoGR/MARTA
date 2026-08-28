
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
    assert not failure_validation.is_success()
    assert failure_validation.errors == ['Error message']

# Test the __str__ method for successful validation
def test_successful_validation_str():
    success_validation = Validation(value=10, errors=[])
    assert str(success_validation) == 'Validation.success[10]'

# Test the __str__ method for failed validation
def test_failed_validation_str():
    failure_validation = Validation(value=None, errors=['Error message'])
    assert str(failure_validation) == 'Validation.fail[None, [\'Error message\']]'

# Test bind function

# Test apply function
def test_apply_function():
    def divide_by_two(val):
        if val is not None:
            return val / 2
        else:
            raise ValueError("Cannot divide by zero")
    
    failure_validation = Validation(value=None, errors=['Error message'])
    with pytest.raises(ValueError) as excinfo:
        applied_validation = failure_validation.ap(divide_by_two)
    assert str(excinfo.value) == "Cannot divide by zero"

# Test to_either_success method

# Test to_either_failure method

# Test to_maybe_success method

# Test to_maybe_failure method