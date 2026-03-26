
import pytest
from pymonet.validation import Validation

# Test the initialization of the Validation class with a success value and an empty errors list
def test_validation_init():
    val = Validation(10, [])
    assert val.value == 10
    assert val.errors == []

# Test adding an error to the Validation instance
def test_add_error():
    val = Validation(10, [])
    val.errors.append("Invalid input")
    assert val.errors == ["Invalid input"]

# Test creating a failed Validation instance with an error message
def test_validation_fail():
    failed_val = Validation.fail(["Error message"])
    assert failed_val.value is None
    assert failed_val.errors == ["Error message"]

# Test the map method of the Try class (assuming it exists and behaves as described)
def test_try_map(monkeypatch):
    # Mocking a function to use with map
    def square(x):
        return x * x
    
    # Assuming Try has a map method that applies a function to its value if successful
    try_instance = Validation(3, True)  # Successful Try instance
    mapped_try = try_instance.map(square)
    assert mapped_try.value == 9  # Since 3^2 is 9

# Test the bind method of the Try class (assuming it exists and behaves as described)
def test_try_bind(monkeypatch):
    # Mocking a function to use with bind
    def square(x):
        return Validation(x * x, True)
    
    try_instance = Validation(3, True)  # Successful Try instance
    result = try_instance.bind(square)
    assert result.value == 9  # Since 3^2 is 9

# Test the map method of the Left class (assuming it exists and behaves as described)
def test_left_map():
    left_value = Validation.fail(["error"])
    mapped_left = left_value.map(lambda x: f"Error: {x}")