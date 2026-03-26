
import pytest
from typing import Iterable, List, Iterator, TypeVar
from flutes.iterator import chunk

T = TypeVar('T')

def test_chunk_basic():
    result = list(chunk(3, range(10)))
    assert result == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

def test_chunk_empty_iterable():
    result = list(chunk(3, []))
    assert result == []

def test_chunk_list_as_iterable():
    result = list(chunk(3, [1, 2, 3, 4, 5]))
    assert result == [[1, 2, 3], [4, 5]]

def test_chunk_string_as_iterable():
    result = list(chunk(3, "hello"))