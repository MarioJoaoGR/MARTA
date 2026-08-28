
import pytest
from typesystem.base import ValidationResult, ValidationError

# Scenario 1: Test standard input with valid schema definitions
def test_valid_inputs():
    result = ValidationResult(value="valid_data", error=None)
    assert result.value == "valid_data"
    assert result.error is None

# Scenario 2: Test invalid input where validation fails
def test_invalid_input():
    with pytest.raises(TypeError):
        ValidationResult(error=ValidationError("Validation failed"))

# Scenario 3: Test iteration over a valid ValidationResult instance
def test_iter_validation_result():
    result = ValidationResult(value="valid_data", error=None)
    value, error = tuple(result)
    assert value == "valid_data"
    assert error is None
