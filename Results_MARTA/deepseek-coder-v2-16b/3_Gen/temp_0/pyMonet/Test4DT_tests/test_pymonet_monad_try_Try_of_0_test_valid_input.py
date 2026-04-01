
import pytest
from pymonet.monad_try import Try

def test_valid_input():
    def valid_function(x):
        return x + 1
    
    # Test a function call that should succeed
    result = Try.of(valid_function, 2)
    assert result.is_success is True
    assert result.value == 3
    
    # Test a function call that should fail
    def failing_function():
        raise ValueError("Test error")
    
    result = Try.of(failing_function)
    assert result.is_success is False
    assert str(result.value) == "Test error"
