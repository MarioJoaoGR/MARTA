
from superstring.superstring import SuperStringBase, SuperStringUpper
import pytest

def test_valid_input():
    # Create a mock for SuperStringBase
    class MockSuperStringBase:
        def __init__(self, string):
            self._string = string
        
        def length(self):
            return len(self._string)
    
    # Test with a valid input
    base_string = "hello, world!"
    mock_base = MockSuperStringBase(base_string)
    upper_string = SuperStringUpper(mock_base)
    
    assert upper_string.length() == len(base_string.upper())
