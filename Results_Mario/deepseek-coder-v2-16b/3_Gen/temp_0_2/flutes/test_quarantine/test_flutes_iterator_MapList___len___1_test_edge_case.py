
import unittest
from typing import Callable, Sequence

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

    def __len__(self) -> int:
        return len(self.list)

class TestMapList(unittest.TestCase):
    def test_empty_list(self):
        maplist = MapList(lambda x: x * 2, [])
        self.assertEqual(len(maplist), 0)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            MapList(lambda x: x * 2, None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_MapList___len___1_test_edge_case
flutes/Test4DT_tests/test_flutes_iterator_MapList___len___1_test_edge_case.py:25:39: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_MapList___len___1_test_edge_case.py:25:43: E0602: Undefined variable 'R' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_MapList___len___1_test_edge_case.py:25:61: E0602: Undefined variable 'T' (undefined-variable)


"""