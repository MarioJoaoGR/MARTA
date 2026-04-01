
import pytest
from itertools import count
from typing import Iterable, Iterator, TypeVar

T = TypeVar('T')

def drop(n: int, iterable: Iterable[T]) -> Iterator[T]:
    if n < 0:
        raise ValueError("`n` should be non-negative")
    it = iter(iterable)
    for _ in range(n):
        next(it)
    yield from it

def test_drop():
    # Test with a normal list
    assert list(drop(3, [1, 2, 3, 4, 5])) == [4, 5]
    
    # Test with an empty list
    assert list(drop(0, [])) == []
    
    # Test with None (should raise ValueError)
    with pytest.raises(ValueError):
        list(drop(-1, range(5)))
    
    # Test with a negative number (should raise ValueError)
    with pytest.raises(ValueError):
        list(drop(-1, [1, 2, 3]))
    
    # Test with None as iterable (should raise TypeError)
    with pytest.raises(TypeError):
        list(drop(3, None))
    
    # Test with a generator expression
    gen = (i for i in range(5))
    assert list(drop(2, gen)) == [2, 3, 4]
    
    # Test with an iterator that stops early
    it = iter([1, 2, 3])
    drop_it = drop(3, it)
    with pytest.raises(StopIteration):
        next(drop_it)
