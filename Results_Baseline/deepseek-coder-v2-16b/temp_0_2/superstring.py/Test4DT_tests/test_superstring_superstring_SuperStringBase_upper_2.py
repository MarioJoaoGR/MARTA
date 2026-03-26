
import pytest
from superstring.superstring import SuperStringBase, SuperString, SuperStringUpper

# Test initialization with a string
def test_initialization():
    s = SuperStringUpper("Hello, World!")
    assert isinstance(s, SuperStringUpper)
    assert s._base == "Hello, World!"

# Test calling the upper() method
def test_upper():
    s = SuperStringUpper("Hello, World!")
    result = s.upper()
    assert isinstance(result, SuperStringUpper)