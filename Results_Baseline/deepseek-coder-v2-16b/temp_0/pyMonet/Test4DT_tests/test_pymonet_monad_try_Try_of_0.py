
import pytest
from pymonet.monad_try import Try

# Test cases for the __init__ method of the Try class
def test_try_init():
    # Successful operation
    successful_try = Try(42, is_success=True)
    assert successful_try.value == 42
    assert successful_try.is_success is True

    # Failed operation
    failed_try = Try("Operation failed", is_success=False)
    assert failed_try.value == "Operation failed"
    assert failed_try.is_success is False

# Test cases for the of method in the Try class
def test_try_of():
    # Function that does not raise an exception
    def safe_function(x):
        return x + 1
    
    successful_try = Try.of(safe_function, 41)
    assert successful_try.value == 42
    assert successful_try.is_success is True

    # Function that raises an exception
    def failing_function():
        raise ValueError("Error occurred")
    
    failed_try = Try.of(failing_function)
    assert isinstance(failed_try.value, ValueError)
    assert failed_try.is_success is False

# Test cases for the map method in the Try class
def test_try_map():
    # Successful operation with a function that doubles the value
    successful_try = Try(42, is_success=True)
    mapped_try = successful_try.map(lambda x: x * 2)
    assert mapped_try.value == 84
    assert mapped_try.is_success is True

    # Failed operation should not change the result when mapping
    failed_try = Try("Operation failed", is_success=False)
    failed_mapped_try = failed_try.map(lambda x: x * 2)
    assert failed_mapped_try.value == "Operation failed"
    assert failed_mapped_try.is_success is False

# Test cases for the bind method in the Try class
def test_try_bind():
    # Successful operation with a function that increments the value
    successful_try = Try(41, is_success=True)
    bound_try = successful_try.bind(lambda x: x + 1)