
import itertools
from typing import Iterable, Tuple, Any
import pytest

def _pairwise(iterable: Iterable, end=None) -> Iterable[Tuple[Any, Any]]:
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.zip_longest(a, b, fillvalue=end)

# Test with a list of integers

# Test with a tuple of numbers

# Test with a string

# Test with an empty list
def test_pairwise_empty_list():
    result = list(_pairwise([]))
    assert result == []

# Test with a single-element list and specifying an end value
def test_pairwise_single_element_with_end():
    result = list(_pairwise([42], end="only"))
    assert result == [(42, "only")]

# Test with a list of strings and specifying an end value
def test_pairwise_strings_with_end():
    result = list(_pairwise(["a", "b", "c"], end="end"))
    assert result == [('a', 'b'), ('b', 'c'), ('c', 'end')]