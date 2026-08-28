
import pytest
from ansible.plugins.filter.core import flatten

def is_sequence(element):
    return isinstance(element, list) or isinstance(element, tuple)

# Test case for flattening a list without specifying levels or skipping nulls
def test_flatten_one_level():
    result = flatten([1, [2, 3], [[4, 5], 6]])
    assert result == [1, 2, 3, 4, 5, 6]

# Test case for flattening a list and ignoring 'None', 'null' values
def test_flatten_with_skip_nulls():
    result = flatten([1, [2, None, 'null', [3, 4]], [[5, 6], 7]])
    assert result == [1, 2, 3, 4, 5, 6, 7]

# Test case for flattening a list up to one level (default behavior)

# Test case for flattening a list up to two levels
def test_flatten_up_to_two_levels():
    result = flatten([1, [2, [3, [4, 5]]]], levels=2)
    assert result == [1, 2, 3, [4, 5]]