# Module: ansible.plugins.filter.core
import pytest
from ansible.plugins.filter.core import flatten

# Test cases for the flatten function
def test_flatten_basic():
    assert flatten([1, [2, 3], [[4, 5], 6]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_skip_nulls():
    assert flatten([1, [2, None], [[None, 5], 6]], skip_nulls=False) == [1, 2, None, None, 5, 6]

def test_flatten_specific_levels():
    assert flatten([1, [2, [3, [4, 5]]], [[[6, 7], 8], 9]], levels=2) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_flatten_all_levels():
    assert flatten([1, [2, [3, [4, 5]]], [[[6, 7], 8], 9]], levels=None) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_flatten_skip_nulls_default():
    assert flatten([1, [2, None], [[None, 5], 6]]) == [1, 2, 5, 6]

# Additional edge cases to consider:
def test_flatten_empty_list():
    assert flatten([]) == []

def test_flatten_no_nested_lists():
    assert flatten([1, 2, 3]) == [1, 2, 3]

def test_flatten_none_as_element():
    with pytest.raises(TypeError):
        flatten([1, None, [None]])  # This should raise a TypeError because the function does not handle 'None' directly without skip_nulls=False

# Test cases for handling different types within lists (optional but can be useful)
def test_flatten_mixed_types():
    with pytest.raises(TypeError):  # This should raise a TypeError due to mixed types in the list
        flatten([1, "string", [3]])
