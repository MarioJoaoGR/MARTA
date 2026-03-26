
import pytest
from superstring.superstring import SuperStringUpper

# Test initialization with a Base String
def test_initialization():
    s = SuperStringUpper("Hello, World!")
    assert s._base == "Hello, World!"

# Test converting to Uppercase
def test_upper():
    s = SuperStringUpper("Hello, World!")
    result = s.upper()