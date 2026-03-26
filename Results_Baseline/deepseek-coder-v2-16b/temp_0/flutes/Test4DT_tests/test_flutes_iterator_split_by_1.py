
import pytest
from typing import List, Callable, Iterator, Iterable
from flutes.iterator import split_by

# Helper function to convert iterator to list for easier assertion
def list_from_iter(it):
    return [list(g) for g in it]

# Test cases for splitting by a criterion function
def test_split_by_criterion():
    criterion = lambda x: x % 3 == 0
    result = list_from_iter(split_by(range(10), criterion=criterion))
    assert result == [[1, 2], [4, 5], [7, 8]]

# Test cases for splitting by a separator character
def test_split_by_separator():
    result = list_from_iter(split_by(" Split by: ", empty_segments=True, separator=':'))  