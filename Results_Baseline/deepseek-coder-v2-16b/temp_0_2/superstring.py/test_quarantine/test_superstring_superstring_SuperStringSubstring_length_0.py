
# Module: superstring.superstring
import pytest
from superstring.superstring import SuperStringSubstring

# Test initialization with valid parameters
def test_init_valid():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss._base == "Hello, World!"
    assert sss._start_index == 7
    assert sss._end_index == 12

# Test initialization with invalid parameters (negative start index)
def test_init_invalid_negative_start():
    with pytest.raises(ValueError):
        SuperStringSubstring("Hello, World!", -1, 5)

# Test initialization with invalid parameters (start index greater than length of base string)
def test_init_invalid_start_greater_than_length():
    with pytest.raises(ValueError):
        SuperStringSubstring("Hello, World!", 13, 15)

# Test initialization with invalid parameters (negative end index)
def test_init_invalid_negative_end():
    with pytest.raises(ValueError):
        SuperStringSubstring("Hello, World!", 5, -1)

# Test initialization with invalid parameters (end index greater than length of base string)
def test_init_invalid_end_greater_than_length():
    with pytest.raises(ValueError):
        SuperStringSubstring("Hello, World!", 5, 20)

# Test getting the substring with valid indices
def test_get_substring_valid():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.get_substring() == "World"

# Test getting the substring with invalid indices (start index greater than end index)
def test_get_substring_invalid_indices():
    with pytest.raises(ValueError):
        sss = SuperStringSubstring("Hello, World!", 12, 7)
        sss.get_substring()

# Test getting the length of the substring
def test_length():
    sss = SuperStringSubstring("Hello, World!", 0, 5)
    assert sss.length() == 5

# Test getting a specific character in the substring
def test_character_at():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    char = sss.character_at(0)
    assert char == "W"

# Test getting a printable representation of the substring
def test_to_printable():
    sss = SuperStringSubstring("Hello, World!", 0, 5)
    printable_substring = sss.to_printable()
    assert printable_substring == "Hello"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringSubstring_length_0
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_length_0.py:36:11: E1101: Instance of 'SuperStringSubstring' has no 'get_substring' member (no-member)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_length_0.py:42:8: E1101: Instance of 'SuperStringSubstring' has no 'get_substring' member (no-member)


"""