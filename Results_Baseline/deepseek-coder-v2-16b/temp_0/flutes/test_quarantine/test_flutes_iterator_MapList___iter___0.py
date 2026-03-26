
# Module: flutes.iterator
import pytest
from typing import Callable, Iterator, Sequence, TypeVar
import bisect  # Importing here since it's used in multiple tests

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

def test_maplist_with_range():
    b = [2, 3, 4, 5, 6]
    ml = MapList(lambda i: a[i] * b[i], range(len(a)))
    result = list(ml)
    assert result == [2, 6, 12, 20, 30]
    pos = bisect.bisect_left(list(ml), 10)  # Convert ml to list since bisect expects a sequence
    assert pos == 2

def test_maplist_custom_lambda():
    c = [7, 8, 9, 10, 11]
    ml = MapList(lambda x: x - 1, c)
    result = list(ml)
    assert result == [6, 7, 8, 9, 10]
    pos = bisect.bisect_left(list(ml), 9)  # Convert ml to list since bisect expects a sequence
    assert pos == 3

def test_maplist_with_tuple():
    d = (3, 5, 7, 9, 11)
    ml = MapList(lambda x: x * 2, d)
    result = list(ml)
    assert result == [6, 10, 14, 18, 22]
    pos = bisect.bisect_left(list(ml), 10)  # Convert ml to list since bisect expects a sequence
    assert pos == 2

# Run the tests
if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_MapList___iter___0
flutes/Test4DT_tests/test_flutes_iterator_MapList___iter___0.py:46:27: E0602: Undefined variable 'a' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_MapList___iter___0.py:46:50: E0602: Undefined variable 'a' (undefined-variable)


"""