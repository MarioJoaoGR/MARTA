
# Module: ansible.module_utils.common.collections
from ansible.module_utils.common.collections import is_sequence
import pytest
from collections.abc import Sequence

# Helper function to check if an object is a string
def is_string(obj):
    return isinstance(obj, (str, bytes))

# Test cases for the `is_sequence` function
@pytest.mark.parametrize("seq, include_strings, expected", [
    ([1, 2, 3], False, True),          # List, not including strings by default
    ((1, 2, 3), False, True),           # Tuple, not including strings by default
    ({1, 2, 3}, False, False),         # Set, not including strings by default (expected to be False)
    ("Hello", False, False),            # String, not including strings by default
    ("Hello", True, True),              # String, including strings
    (b"Hello", False, False),           # Bytes, not including strings by default
    (b"Hello", True, True),             # Bytes, including strings
    ([], False, True),                  # Empty list
    ((), False, True),                  # Empty tuple
    (set(), False, False),              # Empty set, not including strings by default (expected to be False)
])
def test_is_sequence(seq, include_strings, expected):
    assert is_sequence(seq, include_strings) == expected

# Additional test cases for uncovered lines 94-95 and 97

# Test case for a non-sequence type (int)
def test_non_sequence():
    seq = 123
    include_strings = False
    assert not is_sequence(seq, include_strings), "Expected non-sequence to return False"

# Test case for including strings when specified
def test_include_strings():
    seq = "Hello"
    include_strings = True
    assert is_sequence(seq, include_strings), "Expected string to be recognized as a sequence with include_strings=True"

# Test case for including bytes when specified
def test_include_bytes():
    seq = b"Hello"
    include_strings = True
    assert is_sequence(seq, include_strings), "Expected bytes to be recognized as a sequence with include_strings=True"

# Test case for checking if None is considered a sequence
def test_none_is_not_sequence():
    seq = None
    include_strings = False
    assert not is_sequence(seq, include_strings), "Expected None to return False as it's not a sequence"
