
import pytest
from flutes.iterator import LazyList

def test_error_handling():
    # Create a LazyList instance with an iterable that will raise an error when iterated over
    class ErrorIterable:
        def __iter__(self):
            raise ValueError("Test error")
    
    lazy_list = None
    try:
        lazy_list = LazyList(ErrorIterable())
    except ValueError as e:
        assert str(e) == "Test error"
        return  # If we catch the exception, we don't need to continue with the test.
    
    pytest.fail("Expected a ValueError but no exception was raised.")
