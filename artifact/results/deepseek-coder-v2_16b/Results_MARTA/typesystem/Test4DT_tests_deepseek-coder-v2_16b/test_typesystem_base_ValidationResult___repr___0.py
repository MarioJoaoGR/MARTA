
import pytest
from typesystem.base import ValidationResult, ValidationError

# Scenario 1: Test standard input with valid schema definitions
def test_valid_inputs():
    value = {"key": "value"}
    result = ValidationResult(value=value)
    assert result.value == value
    assert result.error is None

# Scenario 2: Test invalid input and check the error type

# Scenario 3: Test edge case where both value and error are provided (should raise an exception)
def test_edge_case():
    with pytest.raises(TypeError):
        ValidationResult(error=ValidationError('Invalid data'))