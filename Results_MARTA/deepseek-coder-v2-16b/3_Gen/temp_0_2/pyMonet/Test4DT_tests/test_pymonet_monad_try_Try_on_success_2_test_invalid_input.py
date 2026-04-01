
import pytest
from pymonet.monad_try import Try

def test_invalid_input():
    # Test that passing an invalid input does not raise an exception and returns self
    try_object = Try(None, False)
    assert try_object.is_success == False
    
    def print_value(val):
        pass  # This function is a placeholder to simulate the callback function

    result = try_object.on_success(print_value)
    assert isinstance(result, Try)
    assert result.is_success == False
