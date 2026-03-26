
import pytest
from superstring import SuperString

# Test initialization with a string
def test_init():
    s = SuperString("Hello, World!")
    assert s._content == "Hello, World!"

# Test length calculation for the first time
def test_length_first_time():
    s = SuperString("Hello, World!")
    assert s.length() == 13

# Test cached length without recalculating
def test_length_cached():
    s = SuperString("Hello, World!")
    # First call should calculate the length
    assert s.length() == 13
    # Subsequent calls should return the cached value
    for _ in range(5):
        assert s.length() == 13

# Test edge case with an empty string
def test_length_empty_string():
    s = SuperString("")
    assert s.length() == 0

# Test length calculation after changing the content
def test_length_after_change():
    s = SuperString("Hello, World!")
    assert s.length() == 13
    s._content = "New content"