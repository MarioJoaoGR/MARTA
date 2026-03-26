
import pytest
from superstring.superstring import SuperStringUpper  # Assuming this is the correct module path

def test_valid_input():
    class MockSuperStringBase:
        def __init__(self, base):
            self._base = base
        
        def length(self):
            return len(self._base)
    
    mock_base = MockSuperStringBase("Hello, World!")
    upper_str = SuperStringUpper(mock_base)
    
    assert upper_str.length() == 13  # "HELLO, WORLD!" has a length of 13
