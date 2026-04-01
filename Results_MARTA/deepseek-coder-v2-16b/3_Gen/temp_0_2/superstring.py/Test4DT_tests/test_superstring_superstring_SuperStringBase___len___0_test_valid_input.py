
import pytest
from unittest.mock import MagicMock
from superstring.superstring import SuperStringBase

def test_valid_input():
    # Create a mock subclass of SuperStringBase
    class MockSubclass(SuperStringBase):
        def length(self):
            return 10  # Mock implementation for testing

    # Instantiate the mock subclass
    instance = MockSubclass()
    
    # Use MagicMock to create a mock object with len method
    mock_object = MagicMock()
    mock_object.__len__.return_value = 10  # Set the return value of __len__ to 10
    
    # Assign the mocked object to the instance's length method
    instance.length = lambda: mock_object.__len__()
    
    # Test the __len__ method
    assert len(instance) == 10
