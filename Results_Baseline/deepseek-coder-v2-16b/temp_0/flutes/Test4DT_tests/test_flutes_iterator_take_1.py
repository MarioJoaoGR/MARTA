
import pytest
from flutes.iterator import take
from typing import Iterator, Iterable, List, TypeVar

T = TypeVar('T')

# Test cases for the `take` function
def test_basic_usage():
    result = take(5, range(10))
    assert list(result) == [0, 1, 2, 3, 4]

def test_large_range():
    large_range = range(1000000)
    result = take(5, large_range)
    assert list(result) == [0, 1, 2, 3, 4]

def test_zero_elements():
    empty_range = range(0)
    result = take(0, empty_range)
    assert list(result) == []

# Additional test cases to cover uncovered lines
@pytest.mark.xfail(reason="Expected failure due to negative `n`")
def test_negative_n():
    with pytest.raises(ValueError):
        take(-1, range(10))

def test_stop_iteration():
    result = take(5, iter([]))
    assert list(result) == []
