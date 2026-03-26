
# Module: superstring.superstring
import pytest
from superstring.superstring import SuperStringUpper

# Test initialization with a base string
def test_init():
    s = SuperStringUpper("Hello, World!")
    assert s._base == "Hello, World!"

# Test conversion to lowercase
def test_lower():
    s = SuperStringUpper("Hello, World!")
    result = s.lower()