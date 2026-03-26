
import pytest
from superstring import SuperString

# Test cases for substring method with default end index
def test_substring_default_end():
    s = SuperString("Hello, World!")
    assert str(s.substring(0)) == "Hello, World!"
    assert str(s.substring(7)) == "World!"
    assert str(s.substring(13)) == ""

# Test cases for substring method with specified start and end indices
def test_substring_specified_indices():
    s = SuperString("Hello, World!")