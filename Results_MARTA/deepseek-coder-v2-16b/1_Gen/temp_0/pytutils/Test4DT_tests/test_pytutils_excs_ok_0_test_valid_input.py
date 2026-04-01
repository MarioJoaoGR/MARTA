
import pytest
from pytutils.excs import ok

def test_valid_input():
    # Test passing through ZeroDivisionError
    try:
        with ok(ZeroDivisionError):
            assert 1 / 0 == float('inf')  # This should not raise an error because ZeroDivisionError is passed.
    except ZeroDivisionError:
        pytest.fail("Expected no exception, got ZeroDivisionError")
    
    # Test passing through ValueError
    try:
        with ok(ValueError):
            with pytest.raises(ValueError):
                raise ValueError("Test exception")  # This should not raise an error because ValueError is passed.
    except ValueError:
        pytest.fail("Expected no exception, got ValueError")
    
    # Test passing through multiple exceptions
    try:
        with ok(ZeroDivisionError, ValueError):
            assert 1 / 0 == float('inf')  # This should not raise an error because ZeroDivisionError is passed.
            with pytest.raises(ValueError):
                raise ValueError("Test exception")  # This should not raise an error because ValueError is passed.
    except (ZeroDivisionError, ValueError):
        pytest.fail("Expected no exception, got one of the specified exceptions")
