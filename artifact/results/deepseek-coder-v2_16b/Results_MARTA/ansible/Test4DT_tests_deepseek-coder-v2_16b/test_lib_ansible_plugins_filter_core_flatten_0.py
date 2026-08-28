
import pytest
from ansible.plugins.filter.core import flatten

def is_sequence(obj):
    return isinstance(obj, (list, tuple))

# Test case for flattening a list without specifying levels or skipping nulls
def test_flatten_without_levels_or_skip_nulls():
    assert flatten([1, [2, 3], [[4, 5], 6]]) == [1, 2, 3, 4, 5, 6]

# Test case for flattening a list and ignoring 'None', 'null' values
def test_flatten_ignoring_nulls():
    assert flatten([1, [2, None, 'null', [3, 4]], [[5, 6], 7]]) == [1, 2, 3, 4, 5, 6, 7]

# Test case for flattening a list up to one level

# Test case for flattening a list up to two levels
def test_flatten_two_levels():
    assert flatten([1, [2, [3, [4, 5]]]], levels=2) == [1, 2, 3, [4, 5]]