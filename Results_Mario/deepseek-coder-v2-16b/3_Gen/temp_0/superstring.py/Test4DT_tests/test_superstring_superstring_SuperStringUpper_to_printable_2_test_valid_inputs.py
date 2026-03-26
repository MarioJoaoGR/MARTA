
import pytest
from superstring.superstring import SuperString

class SuperStringUpper:
    def __init__(self, base):
        self._base = base

    def to_printable(self, start_index=None, end_index=None):
        return self._base.to_printable(start_index, end_index).upper()

def test_valid_inputs():
    s = SuperStringUpper(SuperString("Hello, World!"))
    
    # Test the entire string conversion to uppercase
    assert s.to_printable() == "HELLO, WORLD!"
    
    # Test substring conversion to uppercase with start and end indices provided
    assert s.to_printable(7, 12) == "WORLD"
    
    # Test entire string conversion when only start index is provided (should default to None)
    assert s.to_printable(None, None) == "HELLO, WORLD!"
    
    # Test substring conversion to uppercase with end index not provided
    assert s.to_printable(7, None) == "WORLD!"
    
    # Test substring conversion to uppercase with start index not provided
    assert s.to_printable(None, 5) == "HELLO"
