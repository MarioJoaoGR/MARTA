
import pytest
from pymonet.monad_try import Try

def test_valid_input():
    # Define a simple function that returns its argument multiplied by 2
    def safe_function(x):
        return x * 2
    
    # Test with valid input, should not raise an exception
    result = Try.of(safe_function, 5)
    assert result.value == 10
    assert result.is_success is True
