
# Module: superstring.superstring
import pytest
from superstring.superstring import SuperStringSubstring

# Test initialization with base string and indices
def test_init():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss._base == "Hello, World!"
    assert sss._start_index == 7
    assert sss._end_index == 12

# Test retrieving the substring
def test_get_substring():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.get_substring() == "World"

# Test getting the length of the substring
def test_length():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.length() == 5

# Test retrieving a character at a specific index
def test_character_at():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.character_at(0) == "W"

# Test extracting a substring using different indices
def test_substring():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.substring(0) == "Hello"
    assert sss.substring(6, 11) == "World"

# Test getting a printable representation of the substring
def test_to_printable():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.to_printable() == "Hello"
    assert sss.to_printable(start_index=6) == "World"

# Test invalid index in character_at method
def test_character_at_invalid():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    with pytest.raises(IndexError):
        sss.character_at(10)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringSubstring_character_at_0
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_character_at_0.py:16:11: E1101: Instance of 'SuperStringSubstring' has no 'get_substring' member (no-member)


"""