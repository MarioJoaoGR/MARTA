
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
