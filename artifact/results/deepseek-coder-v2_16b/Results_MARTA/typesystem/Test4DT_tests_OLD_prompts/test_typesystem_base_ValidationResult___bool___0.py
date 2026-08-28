
import pytest
from typesystem.base import ValidationResult, ValidationError
import typing

# Scenario 1: Successful validation
def test_validation_success():
    value = {"key": "value"}
    result = ValidationResult(value=value)
    assert bool(result) is True
    assert result.value == value
    assert result.error is None

# Scenario 2: Failed validation

# Scenario 3: Unpacking the result
def test_validation_unpack():
    value = {"key": "value"}
    result = ValidationResult(value=value)
    val, err = (result.value, result.error) if bool(result) else (None, result.error)
    assert val == value
    assert err is None or isinstance(err, ValidationError)

# Scenario 4: Conditional check using __bool__
def test_validation_conditional():
    value = {"key": "value"}
    result = ValidationResult(value=value)
    if bool(result):
        assert result.value == value
    else:
        assert result.error is not None

# Scenario 5: Using __repr__ for debugging
def test_validation_repr():
    value = {"key": "value"}
    result = ValidationResult(value=value)
    print(repr(result))  # Expected output: "ValidationResult(value={'key': 'value'})"
    assert repr(result) == f"ValidationResult(value={value})"