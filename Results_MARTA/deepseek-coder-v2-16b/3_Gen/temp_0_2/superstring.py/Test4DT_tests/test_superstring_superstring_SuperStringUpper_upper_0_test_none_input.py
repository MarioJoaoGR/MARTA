
import pytest
from superstring.superstring import SuperStringUpper

def test_none_input():
    # Create an instance of SuperStringUpper with a given string
    ssu = SuperStringUpper(None)  # Passing None as base to simulate no input
    
    # Convert the string to uppercase (which should do nothing since base is None)
    result = ssu.upper()
    
    # The internal base attribute should still be None
    assert result._base == None
