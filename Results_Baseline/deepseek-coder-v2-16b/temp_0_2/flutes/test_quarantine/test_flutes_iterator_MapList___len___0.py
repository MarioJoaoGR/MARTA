
# Module: flutes.iterator
import pytest
from typing import Callable, Sequence, TypeVar
from bisect import bisect_left

T = TypeVar('T')
R = TypeVar('R')

class MapList:
    """A wrapper over a list that allows lazily performing transformations on the list elements. It's basically the built-in :py:func:`map` function, with support for indexing operators. An example use case:
    
    .. code:: python
    
        >>> import bisect
    
        >>> # Find index of the first element in `a` whose square is >= 10.
        ... a = [1, 2, 3, 4, 5]
        ... mapped_list = MapList(lambda x: x * x, a)
        ... assert mapped_list[0] == 1  # 1^2
        ... assert mapped_list[1:3] == [4, 9]  # 2^2 and 3^2
        ... for i, item in enumerate(mapped_list):
        ...     assert item == a[i] * a[i]
    
        >>> # Find the first index `i` such that `a[i] * b[i]` is >= 10.
        ... b = [2, 3, 4, 5, 6]
        ... mapped_list = MapList(lambda i: a[i] * b[i], range(len(a)))
        ... pos = bisect.bisect_left(mapped_list, 10)
        ... assert pos == 2  # index where `a[i] * b[i]` is >= 10
    
    :param func: The transformation to perform on list elements.
    :param lst: The list to wrap.
    """
    def __init__(self, func: Callable[[T], R], lst: Sequence[T]):
        self.func = func
        self.list = lst

    def __getitem__(self, index):
        return self.func(self.list[index])

    def __len__(self) -> int:
        return len(self.list)

# Test cases for MapList class
def test_maplist_basic():
    a = [1, 2, 3, 4, 5]
    mapped_list = MapList(lambda x: x * x, a)
    assert mapped_list[0] == 1  # 1^2
    assert mapped_list[1:3] == [4, 9]  # 2^2 and 3^2
    for i, item in enumerate(mapped_list):
        assert item == a[i] * a[i]

def test_maplist_with_bisect():
    a = [1, 2, 3, 4, 5]
    mapped_list = MapList(lambda x: x * x, a)
    pos = bisect_left(mapped_list, 10)
    assert pos == 3  # index of the first element whose square is >= 10

def test_maplist_with_range():
    b = [2, 3, 4, 5, 6]
    mapped_list = MapList(lambda i: a[i] * b[i], range(len(a)))
    pos = bisect_left(mapped_list, 10)
    assert pos == 2  # index where `a[i] * b[i]` is >= 10

# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_MapList___len___0
flutes/Test4DT_tests/test_flutes_iterator_MapList___len___0.py:61:36: E0602: Undefined variable 'a' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_MapList___len___0.py:61:59: E0602: Undefined variable 'a' (undefined-variable)


"""