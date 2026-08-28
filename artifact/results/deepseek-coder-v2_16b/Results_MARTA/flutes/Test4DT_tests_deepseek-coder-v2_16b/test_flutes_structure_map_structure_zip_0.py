
import pytest
from flutes.structure import map_structure_zip
from typing import Callable, Collection, Sequence

# Define a sample function to be used with map_structure_zip
def add(a, b):
    return a + b

# Example list of collections (lists)
objs = [[1, 2], [3, 4]]

# Test case for valid input
def test_valid_input():
    result = map_structure_zip(add, objs)
    assert result == [4, 6]

# Example list of collections with different structures that cannot be mapped directly
objs_invalid = [{'a': 1}, {'b': 2}]

# Test case for invalid input