
import pytest
from superstring.superstring import SuperStringUpper

# Test initialization with a base string
def test_init():
    s = SuperStringUpper("Hello, World!")
    assert s._base == "Hello, World!"

# Test converting the entire base string to uppercase
def test_upper():
    s = SuperStringUpper("Hello, World!")
    result = s.upper()