
import pytest
from pysnooper.tracer import Tracer

# Define a simple context manager for logging
class LoggingContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")

# Define a simple function to be wrapped
def add_numbers(a, b):
    return a + b

# Define a function that handles None or empty inputs gracefully
def handle_edge_cases(value):
    if value is None:
        return 0
    if isinstance(value, list) and not value:
        return []
    return value

# Define a function that raises exceptions on invalid input
def validate_and_add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return a + b

# Simulate simple_wrapper by defining it to take an explicit function argument
def simple_wrapper(function, *args, **kwargs):
    with LoggingContextManager():
        return function(*args, **kwargs)

# Test scenarios
def test_happy_path():
    result = simple_wrapper(add_numbers, 5, 3)
    assert result == 8

def test_edge_cases():
    result_none = simple_wrapper(handle_edge_cases, None)
    assert result_none == 0

    result_empty_list = simple_wrapper(handle_edge_cases, [])
    assert result_empty_list == []

def test_invalid_inputs():
    with pytest.raises(ValueError):
        simple_wrapper(validate_and_add, 'a', 3)

    with pytest.raises(ValueError):
        simple_wrapper(validate_and_add, 5, 'b')
