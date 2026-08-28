
import pytest
from typesystem.base import ValidationResult, ValidationError

# Scenario 1: Test standard input with valid schema definitions
def test_valid_inputs():
    value = {"key": "value"}
    result = ValidationResult(value=value)
    assert result.value == value
    assert repr(result) == f"ValidationResult(value={value!r})"

# Scenario 2: Test invalid input that should raise TypeError
def test_invalid_input():
    with pytest.raises(TypeError):
        ValidationResult(error=ValidationError("Test error"))
