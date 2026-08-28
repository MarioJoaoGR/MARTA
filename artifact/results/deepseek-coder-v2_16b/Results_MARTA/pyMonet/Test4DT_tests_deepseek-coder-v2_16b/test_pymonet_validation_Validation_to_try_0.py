
import pytest
from pymonet.validation import Validation

# Scenario 1: Test standard input with valid values and no errors
def test_valid_input_happy_path():
    success_validation = Validation(value=10, errors=[])
    assert success_validation.value == 10
    assert len(success_validation.errors) == 0
    assert success_validation.is_success() is True

# Scenario 2: Test edge case with None value and empty errors list
def test_edge_case_none_and_empty_errors():
    edge_case_validation = Validation(value=None, errors=[])
    assert edge_case_validation.value is None
    assert len(edge_case_validation.errors) == 0
    assert edge_case_validation.is_success() is True

# Scenario 3: Test handling of invalid input by raising ValueError
def test_invalid_input_error_handling():
    try:
        raise ValueError('Test Error')
    except ValueError as e:
        failed_validation = Validation(value=None, errors=[str(e)])
        assert failed_validation.value is None
        assert len(failed_validation.errors) == 1
        assert failed_validation.errors[0] == 'Test Error'
        assert failed_validation.is_success() is False
