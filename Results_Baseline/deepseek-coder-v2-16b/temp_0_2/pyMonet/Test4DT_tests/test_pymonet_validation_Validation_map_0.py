
import pytest
from pymonet.validation import Validation

# Test initialization with success value and empty errors list
def test_initialization_with_success_value():
    val = Validation(10, [])
    assert val.value == 10
    assert val.errors == []

# Test adding errors to an existing validation instance
def test_adding_errors():
    val = Validation(10, [])
    val.errors.append("Invalid input")
    assert val.errors == ["Invalid input"]

# Test using the map method to transform the value
def test_map_method_with_valid_mapper():
    def double_value(x):
        return x * 2

    val = Validation(10, [])
    new_val = val.map(double_value)
    assert new_val.value == 20
    assert new_val.errors == []

# Test handling a failed transformation
def test_map_method_with_failing_function():
    def failing_function(x):
        raise ValueError("Failed transformation")

    val = Validation(10, [])
    with pytest.raises(ValueError) as exc_info:
        val.map(failing_function)
    assert str(exc_info.value) == "Failed transformation"

# Test creating a successful validation instance
def test_success():
    val_success = Validation.success(10)
    assert val_success.value == 10
    assert val_success.errors == []

# Test creating a failed validation instance
def test_fail():
    val_fail = Validation.fail(["Error message"])
    assert val_fail.errors == ["Error message"]
