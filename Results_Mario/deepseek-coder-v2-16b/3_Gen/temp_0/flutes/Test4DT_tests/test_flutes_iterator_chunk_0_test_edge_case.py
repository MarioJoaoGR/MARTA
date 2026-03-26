
import pytest
from flutes.iterator import chunk
from typing import Iterable, List, Iterator, TypeVar

T = TypeVar('T')

def test_chunk():
    # Test with a small number of items that should be split into chunks correctly
    iterable = [1, 2, 3, 4, 5]
    n = 2
    expected_output = [[1, 2], [3, 4], [5]]
    
    result = list(chunk(n, iterable))
    assert result == expected_output

def test_chunk_with_single_item():
    # Test with a single item that should be in its own chunk
    iterable = [1]
    n = 2
    expected_output = [[1]]
    
    result = list(chunk(n, iterable))
    assert result == expected_output

def test_chunk_with_empty_iterable():
    # Test with an empty iterable that should yield no chunks
    iterable = []
    n = 2
    expected_output = []
    
    result = list(chunk(n, iterable))
    assert result == expected_output

def test_chunk_with_zero():
    # Test raising ValueError when n is zero or negative
    iterable = [1, 2, 3]
    n = 0
    
    with pytest.raises(ValueError):
        list(chunk(n, iterable))

def test_chunk_with_negative_number():
    # Test raising ValueError when n is negative
    iterable = [1, 2, 3]
    n = -1
    
    with pytest.raises(ValueError):
        list(chunk(n, iterable))
