
import pytest
from unittest.mock import MagicMock
from pymonet.box import Box  # Assuming this is the correct module path

def test_invalid_input():
    # Create a mock Box instance with an invalid type (e.g., int) for testing
    box = Box(123)  # This should be mocked instead of using the actual implementation
    
    # Define a mapper function that will raise an error when applied
    def invalid_mapper(x):
        if isinstance(x, str):
            return x * 2
        else:
            raise ValueError("Invalid input type")
    
    # Use pytest to assert that the bind method raises an appropriate exception
    with pytest.raises(ValueError) as excinfo:
        box.bind(invalid_mapper)
    
    # Check that the exception message matches our expectation
    assert str(excinfo.value) == "Invalid input type"
