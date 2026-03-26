
import pytest
from typing import Callable, Iterator, Sequence, TypeVar

T = TypeVar('T')
R = TypeVar('R')

class MapList:
    """A wrapper over a list that allows lazily performing transformations on the list elements. It's basically the built-in :py:func:`map` function, with support for indexing operators. An example use case:
    
    .. code:: python
    
        >>> import bisect
    
        >>> # Find index of the first element in `a` whose square is >= 10.
        ... a = [1, 2, 3, 4, 5]
        ... pos = bisect.bisect_left(MapList(lambda x: x * x, a), 10)
        3
    
        >>> # Find the first index `i` such that `a[i] * b[i]` is >= 10.
        ... b = [2, 3, 4, 5, 6]
        ... pos = bisect.bisect_left(MapList(lambda i: a[i] * b[i], range(len(a))), 10)
        2
    
    :param func: The transformation to perform on list elements.
    :param lst: The list to wrap.
    """
    def __init__(self, func: Callable[[T], R], lst: Sequence[T]):
        self.func = func
        self.list = lst

    def __iter__(self) -> Iterator[R]:
        return map(self.func, self.list)

# Test cases for MapList class
def test_maplist_basic():
    a = [1, 2, 3, 4, 5]
    ml = MapList(lambda x: x * x, a)
    result = list(ml)
    assert result == [1, 4, 9, 16, 25]

def test_maplist_with_bisect():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    ml = MapList(lambda i: a[i] * b[i], range(len(a)))
    result = list(ml)