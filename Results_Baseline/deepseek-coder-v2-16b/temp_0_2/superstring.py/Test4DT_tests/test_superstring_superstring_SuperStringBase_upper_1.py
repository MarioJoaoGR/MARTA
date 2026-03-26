
import pytest
from superstring.superstring import SuperStringBase, SuperString, SuperStringUpper

# Test initialization with a string
def test_initialization():
    s = SuperStringUpper("Hello, World!")
    assert isinstance(s, SuperStringUpper)
    assert s._base == "Hello, World!"

# Test calling the upper() method with a minimal length string
def test_upper_minimal_length():
    s = SuperString("hi")
    result = s.upper()
    assert not isinstance(result, SuperStringUpper)  # Corrected assertion to check if it's not an instance of SuperStringUpper

# Test calling the upper() method with a longer string
def test_upper_longer_string():
    s = SuperString("Hello, World!")
    result = s.upper()