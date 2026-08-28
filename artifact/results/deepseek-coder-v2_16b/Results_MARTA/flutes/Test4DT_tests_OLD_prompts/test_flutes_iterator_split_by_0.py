
import pytest
from flutes.iterator import split_by
from typing import List, Iterable

# Test case 1: Splitting a range by criterion
def test_split_by_criterion():
    result = list(split_by(range(10), criterion=lambda x: x % 3 == 0))
    assert result == [[1, 2], [4, 5], [7, 8]]

# Test case 2: Splitting a string by separator with empty segments allowed

# Test case 3: Splitting a string by separator without allowing empty segments
def test_split_by_separator_without_empty():
    result = list(split_by("Split.by:.Separator", separator='.'))
    assert result == [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], ['S', 'e', 'p', 'a', 'r', 'a', 't', 'o', 'r']]

# Test case 4: Splitting an empty iterable should return no segments