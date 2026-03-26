
# Module: superstring.superstring
import pytest
from superstring.superstring import SuperStringSubstring

# Test initialization with both start and end indices provided
def test_init_with_both_indices():
    ss = SuperStringSubstring("Hello, World!", 7, 12)
    assert ss._base == "Hello, World!"
    assert ss._start_index == 7
    assert ss._end_index == 12

# Test initialization with only start index provided (default end index should be used)
def test_init_with_only_start_index():
    ss = SuperStringSubstring("Hello, World!", 7)
    assert ss._base == "Hello, World!"
    assert ss._start_index == 7
    assert ss._end_index == len("Hello, World!")

# Test initialization with both default indices (should use start index 0 and end of string as end index)
def test_init_with_default_indices():
    ss = SuperStringSubstring("Hello, World!", 0, 5)
    assert ss._base == "Hello, World!"
    assert ss._start_index == 0
    assert ss._end_index == 5

# Test get_substring method with provided start and end indices
def test_get_substring():
    ss = SuperStringSubstring("Hello, World!", 7, 12)
    assert ss.get_substring() == "World"

# Test to_printable method with default parameters (should return the entire substring)
def test_to_printable_default():
    ss = SuperStringSubstring("Hello, World!", 7, 12)
    assert ss.to_printable() == "World"

# Test to_printable method with specified start and end indices
def test_to_printable_specified_indices():
    ss = SuperStringSubstring("Hello, World!", 7, 12)
    assert ss.to_printable(0, 5) == "World"

# Test character_at method with a specific index within the substring
def test_character_at():
    ss = SuperStringSubstring("Hello, World!", 7, 12)
    assert ss.character_at(0) == "W"

# Test length method to get the length of the substring
def test_length():
    ss = SuperStringSubstring("Hello, World!", 7, 12)
    assert ss.length() == 5

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringSubstring_to_printable_0
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0.py:15:9: E1120: No value for argument 'end_index' in constructor call (no-value-for-parameter)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_to_printable_0.py:30:11: E1101: Instance of 'SuperStringSubstring' has no 'get_substring' member (no-member)


"""