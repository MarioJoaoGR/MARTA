
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

# Define a mock function for testing purposes
def add(x: int, y: int) -> int:
    return x + y

@pytest.mark.parametrize("func, iterable, expected", [
    (add, [1, 2, 3, 4], [1, 3, 6, 10]),
    (lambda x, y: x * y, [1, 2, 3, 4], [1, 2, 6, 24])
])
def test_scanl(func, iterable, expected):
    result = list(scanl(func, iterable))
    assert result == expected
