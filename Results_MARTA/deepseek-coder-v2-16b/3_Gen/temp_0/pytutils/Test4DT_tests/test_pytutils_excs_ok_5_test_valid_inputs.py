
import pytest
from pytutils.excs import ok

def test_valid_inputs():
    # Test passing through ZeroDivisionError
    try:
        with ok(ZeroDivisionError):
            assert 1 / 0 == float('inf')  # This should not raise an error because we are passing the exception
    except ZeroDivisionError:
        pytest.fail("Expected no error but got one")
    
    # Test passing through ValueError
    try:
        with ok(ValueError):
            raise ValueError("Test exception")  # This should not raise an error because we are passing the exception
    except ValueError as e:
        assert str(e) == "Test exception"
    
    # Test no exceptions provided, it should pass through all exceptions
    try:
        with ok():
            raise Exception("General exception")  # This should not raise an error because we are passing the exception
    except Exception as e:
        assert str(e) == "General exception"
