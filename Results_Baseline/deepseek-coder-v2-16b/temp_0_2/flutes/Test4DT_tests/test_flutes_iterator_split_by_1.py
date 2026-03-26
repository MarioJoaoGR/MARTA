
import pytest
from typing import List, Iterable
from flutes.iterator import split_by

# Helper function to convert a generator to a list for comparison
def gen_to_list(gen):
    return [item for item in gen]

# Test cases for splitting by criterion function
def test_split_by_criterion():
    numbers = range(10)
    criterion = lambda x: x % 3 == 0
    result = list(split_by(numbers, criterion=criterion))
    assert result == [[1, 2], [4, 5], [7, 8]]

# Test cases for splitting by separator character
def test_split_by_separator():
    string = " Split by: "
    result = list(split_by(string, empty_segments=True, separator=' '))