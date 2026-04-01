
import pytest
from pymonet.monad_try import Try

def test_invalid_input():
    # Define a simple function that raises an exception for invalid input
    def unsafe_function(x):
        if isinstance(x, int) and x > 0:
            return x * 2
        else:
            raise ValueError("Input must be a positive integer")
    
    # Test the Try.of method with an invalid argument (a string instead of an integer)
    try_object = Try.of(unsafe_function, "invalid input")
    
    # Assert that the operation failed and the correct exception is raised
    assert not try_object.is_success
    assert isinstance(try_object.value, ValueError)
    assert str(try_object.value) == "Input must be a positive integer"
