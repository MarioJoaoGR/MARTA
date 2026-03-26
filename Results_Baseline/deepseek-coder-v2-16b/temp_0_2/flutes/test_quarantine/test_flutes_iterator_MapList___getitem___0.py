
# Module: flutes.iterator
import pytest
from typing import Callable, Sequence, TypeVar

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
        self.lst = lst

    def __getitem__(self, idx: slice) -> 'MapList':
        return MapList(self.func, self.lst[idx])

    def __len__(self):
        return len(self.lst)

# Test cases for MapList class
def test_maplist_basic():
    a = [1, 2, 3, 4, 5]
    mapped_list = MapList(lambda x: x * x, a)
    assert bisect.bisect_left(mapped_list, 10) == 3

def test_maplist_transformation():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    mapped_list = MapList(lambda i: a[i] * b[i], range(len(a)))
    assert bisect.bisect_left(mapped_list, 10) == 2

def test_maplist_slicing():
    a = [1, 2, 3, 4, 5]
    mapped_list = MapList(lambda x: x * x, a)
    assert bisect.bisect_left(mapped_list[1:3], 10) + 1 == 2

# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_MapList___getitem___0
flutes/Test4DT_tests/test_flutes_iterator_MapList___getitem___0.py:43:11: E0602: Undefined variable 'bisect' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_MapList___getitem___0.py:49:11: E0602: Undefined variable 'bisect' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_MapList___getitem___0.py:54:11: E0602: Undefined variable 'bisect' (undefined-variable)


"""