
import pytest
from flutes.iterator import split_by
from typing import List, Iterable, Iterator

def test_valid_case_separator():
    iterable = [1, 2, 3, 'a', 'b', 'c']
    result = list(split_by(iterable, separator=3))
    assert result == [[1, 2], ['a', 'b', 'c']]
