
import pytest
from flutes.iterator import split_by
from typing import List, Iterable, Iterator

# Test cases for split_by function
def test_split_by_basic():
    result = list(split_by([1, 2, 3, 4], separator=2))
    assert result == [[1], [3, 4]]

def test_split_by_string():
    result = list(split_by("hello world", separator=" "))