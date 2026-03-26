
# Module: superstring.superstring
import pytest
from superstring.superstring import SuperStringSubstring

# Test initialization with valid base string and indices
def test_init_valid():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss._base == "Hello, World!"
    assert sss._start_index == 7
    assert sss._end_index == 12

# Test initialization with invalid indices (negative start index)
def test_init_invalid_negative_start():
    with pytest.raises(ValueError):
        SuperStringSubstring("Hello, World!", -1, 12)

# Test initialization with invalid indices (start index greater than end index)
def test_init_invalid_start_greater_than_end():
    with pytest.raises(ValueError):
        SuperStringSubstring("Hello, World!", 12, 7)

# Test getting the substring with valid start and end indices
def test_get_substring_valid():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.get_substring() == "World"

# Test getting the substring with default indices (start=0, end=length of base string)
def test_get_substring_default():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.get_substring() == "World"

# Test getting the substring with invalid indices (negative start index)
def test_get_substring_invalid_negative_start():
    sss = SuperStringSubstring("Hello, World!", -1, 12)
    with pytest.raises(IndexError):
        sss.get_substring()

# Test getting the substring with invalid indices (start index greater than end index)
def test_get_substring_invalid_start_greater_than_end():
    sss = SuperStringSubstring("Hello, World!", 12, 7)
    with pytest.raises(IndexError):
        sss.get_substring()

# Test getting the length of the substring
def test_length():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.length() == 5

# Test getting a specific character in the substring
def test_character_at():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.character_at(0) == "W"

# Test extracting a substring using different start and end indices
def test_substring():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.substring(0) == "Hello"
    assert sss.substring(6, 11) == "World"

# Test getting a printable representation of the substring with default indices
def test_to_printable():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.to_printable() == "World"

# Test getting a printable representation of the substring with specified start and end indices
def test_to_printable_specified_indices():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.to_printable(start_index=6) == "World"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringSubstring_to_printable_0
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0.py:26:11: E1101: Instance of 'SuperStringSubstring' has no 'get_substring' member (no-member)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0.py:31:11: E1101: Instance of 'SuperStringSubstring' has no 'get_substring' member (no-member)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0.py:37:8: E1101: Instance of 'SuperStringSubstring' has no 'get_substring' member (no-member)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0.py:43:8: E1101: Instance of 'SuperStringSubstring' has no 'get_substring' member (no-member)


"""