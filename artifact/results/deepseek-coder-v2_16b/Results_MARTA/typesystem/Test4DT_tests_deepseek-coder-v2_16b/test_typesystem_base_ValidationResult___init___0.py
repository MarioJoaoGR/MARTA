
import pytest
from typesystem.base import ValidationError, ValidationResult

# Scenario 1: Test standard input with valid schema definitions

# Scenario 2: Test initialization with only value
def test_init_with_only_value():
    result = ValidationResult(value="valid data")
    assert result.value == "valid data"
    assert result.error is None

# Scenario 3: Test initialization with only error

# Scenario 4: Test initialization with both value and error (should raise AssertionError)