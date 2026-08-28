
import pytest
from pymonet.validation import Validation

# Scenario 1: Test standard input with valid value and no errors
def test_valid_input():
    success_validation = Validation(value=10, errors=[])
    assert success_validation.value == 10
    assert not success_validation.errors

# Scenario 2: Test edge case with None as value and empty errors list
def test_edge_case_none():
    edge_case_validation = Validation(value=None, errors=[])
    assert edge_case_validation.value is None
    assert not edge_case_validation.errors

# Scenario 3: Test invalid input with errors provided
def test_invalid_input():
    invalid_validation = Validation(value=10, errors=['Error message'])
    assert invalid_validation.value == 10
    assert len(invalid_validation.errors) == 1
    assert 'Error message' in invalid_validation.errors
