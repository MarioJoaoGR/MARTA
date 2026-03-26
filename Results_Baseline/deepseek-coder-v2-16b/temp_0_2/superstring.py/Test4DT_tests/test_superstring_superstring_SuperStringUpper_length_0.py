
import pytest
from superstring.superstring import SuperStringUpper

# Test initialization with a string
def test_init():
    s = SuperStringUpper("Hello, World!")
    assert isinstance(s, SuperStringUpper)
    assert s._base == "Hello, World!"

# Test length method
def test_length():
    s = SuperStringUpper("Hello, World!")