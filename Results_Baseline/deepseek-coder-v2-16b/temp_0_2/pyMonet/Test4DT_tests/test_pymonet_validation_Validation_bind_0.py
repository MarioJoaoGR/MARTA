# Module: pymonet.validation
import pytest
from pymonet.validation import Validation

# Test initialization of Validation class
def test_validation_initialization():
    val = Validation(10, [])
    assert val.value == 10
    assert val.errors == []

# Test adding errors to Validation instance
def test_add_error_to_validation():
    val = Validation(10, [])
    val.errors.append("Invalid input")
    assert val.errors == ["Invalid input"]

# Test bind method with a successful folder function
def test_bind_with_successful_folder():
    def square_if_positive(x):
        if x > 0:
            return Validation(x * x, [])
        else:
            return Validation(None, ["Value must be positive"])
    
    val = Validation(5, [])
    result = val.bind(square_if_positive)
    assert result.value == 25
    assert result.errors == []

# Test bind method with a failing folder function
def test_bind_with_failing_folder():
    def square_if_positive(x):
        if x > 0:
            return Validation(x * x, [])
        else:
            return Validation(None, ["Value must be positive"])
    
    val = Validation(-1, [])
    result = val.bind(square_if_positive)
    assert result.value is None
    assert result.errors == ["Value must be positive"]

# Test bind method with a folder function that returns another Validation instance with errors
def test_bind_with_folder_returning_validation_with_errors():
    def add_error(x):
        return Validation(x, ["Additional error"])
    
    val = Validation(5, [])
    result = val.bind(add_error)
    assert result.value == 5
    assert result.errors == ["Additional error"]

# Test bind method with a folder function that returns another Validation instance without errors
def test_bind_with_folder_returning_validation_without_errors():
    def square_if_positive(x):
        if x > 0:
            return Validation(x * x, [])
        else:
            return Validation(None, ["Value must be positive"])
    
    val = Validation(5, [])
    result = val.bind(lambda x: Validation(x * x, []))
    assert result.value == 25
    assert result.errors == []
