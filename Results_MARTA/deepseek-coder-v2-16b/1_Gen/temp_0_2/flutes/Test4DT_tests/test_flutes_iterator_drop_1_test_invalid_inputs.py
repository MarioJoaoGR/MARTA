
import pytest
from itertools import count
from typing import Iterable, Iterator

def drop(n: int, iterable: Iterable[int]) -> Iterator[int]:
    if n < 0:
        raise ValueError("`n` should be non-negative")
    it = iter(iterable)
    for _ in range(n):
        next(it)
    yield from it

def test_invalid_inputs():
    with pytest.raises(ValueError, match="`n` should be non-negative"):
        list(drop(-1, range(10)))
    with pytest.raises(ValueError, match="`n` should be non-negative"):
        next(drop(-1, (i for i in range(10))))
