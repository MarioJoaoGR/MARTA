
import pytest
from pymonet.validation import Validation

# Scenario 1: Test standard input for successful validation
def test_valid_input():
    success_validation = Validation(value=42, errors=[])
    assert success_validation.value == 42
    assert len(success_validation.errors) == 0

# Scenario 2: Test edge cases such as None and empty lists
def test_edge_case():
    failure_validation_none = Validation(value=None, errors=['Error message'])
    assert failure_validation_none.value is None
    assert len(failure_validation_none.errors) == 1
    assert failure_validation_none.errors[0] == 'Error message'

    failure_validation_empty_list = Validation(value=10, errors=[])
    assert failure_validation_empty_list.value == 10
    assert len(failure_validation_empty_list.errors) == 0

# Scenario 3: Test handling invalid inputs and error messages
def test_invalid_input():
    failure_validation_with_errors = Validation(value=None, errors=['Error message 1', 'Error message 2'])
    assert failure_validation_with_errors.value is None
    assert len(failure_validation_with_errors.errors) == 2
    assert failure_validation_with_errors.errors[0] == 'Error message 1'
    assert failure_validation_with_errors.errors[1] == 'Error message 2'
