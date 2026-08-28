
import pytest
from pymonet.validation import Validation

# Scenario 1: Test standard input with valid value and no errors
def test_valid_input():
    success_validation = Validation(value=10, errors=[])
    assert success_validation.value == 10
    assert len(success_validation.errors) == 0

# Scenario 2: Test edge case with None as value and empty list for errors
def test_edge_case():
    failed_instance = Validation(value=None, errors=[])
    assert failed_instance.value is None
    assert len(failed_instance.errors) == 0

# Scenario 3: Test invalid input with function that should raise an error
def test_invalid_input():
    success_validation = Validation(value=10, errors=[])
    
    def add_ten(x):
        return Validation(None, ['Error'])
    
    result = success_validation.bind(add_ten)
    assert result.value is None
    assert len(result.errors) == 1
    assert result.errors[0] == 'Error'
