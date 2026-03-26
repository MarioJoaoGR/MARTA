
import pytest
from superstring.superstring import SuperStringUpper

# Test initialization with a string
def test_init():
    s = SuperStringUpper("Hello, World!")
    assert isinstance(s, SuperStringUpper)
    assert s._base == "Hello, World!"

# Test length method when _base is not overridden
def test_length_default():
    s = SuperStringUpper("Hello, World!")