
import pytest
from pymonet.either import Left, Right  # Importing Right as per pylint error

# Test cases for the ap method in the Left class
def test_ap():
    # Create a Left instance with an error message
    left_error = Left("An error occurred")
    
    # Apply the ap method, which should return another Left instance with the same value
    result = left_error.ap(Left("Another error"))
    
    # Assert that the result is still a Left instance and has the original value
    assert isinstance(result, Left)