
import pytest
from typing import Iterable, List, Iterator, TypeVar

T = TypeVar('T')

def chunk(n: int, iterable: Iterable[T]) -> Iterator[List[T]]:
    if n <= 0:
        raise ValueError("`n` should be positive")
    group = []
    for x in iterable:
        group.append(x)
        if len(group) == n:
            yield group
            group = []
    if len(group) > 0:
        yield group

def test_valid_input():
    # Test with a range of length exactly divisible by n
    n = 3
    iterable = range(10)
    expected_output = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    
    result = list(chunk(n, iterable))
    assert result == expected_output

    # Test with a range of length not exactly divisible by n
    n = 3
    iterable = range(9)
    expected_output = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    
    result = list(chunk(n, iterable))
    assert result == expected_output

    # Test with an empty iterable
    n = 3
    iterable = []
    expected_output = []
    
    result = list(chunk(n, iterable))
    assert result == expected_output
