
import pytest
from pymonet.monad_try import Try

def test_invalid_input():
    # Test with a valid function that returns a value
    def valid_function(x):
        return x + 1
    
    result = Try.of(valid_function, 1)
    assert result.is_success is True
    assert result.value == 2
    
    # Test with an invalid function that raises an exception
    def invalid_function():
        raise ValueError("Test error")
    
    result = Try.of(invalid_function)
    assert result.is_success is False
    assert str(result.value) == "Test error"
    
    # Test with a function that returns None, which should be considered as success
    def none_returning_function():
        return None
    
    result = Try.of(none_returning_function)
    assert result.is_success is True
    assert result.value is None
