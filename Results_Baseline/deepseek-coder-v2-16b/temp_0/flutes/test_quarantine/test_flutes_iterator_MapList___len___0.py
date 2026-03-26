
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
        self.list = lst

    def __len__(self) -> int:
        return len(self.list)

# Test cases for MapList class
def test_maplist_basic():
    # Define a transformation function that squares each element in the list
    def square(x):
        return x * x

    # Create a list of numbers
    a = [1, 2, 3, 4, 5]

    # Wrap the list with MapList and apply the transformation function
    mapped_list = MapList(square, a)

    # Use bisect.bisect_left to find the index of the first element whose square is >= 10
    pos = bisect.bisect_left(mapped_list, 10)
    assert pos == 3, f"Expected index 3 but got {pos}"

def test_maplist_lambda():
    # Create a list of numbers
    b = [2, 3, 4, 5, 6]

    # Wrap the list with MapList and use a lambda function to transform elements
    mapped_list = MapList(lambda x: x * x, b)

    # Use bisect.bisect_left to find the index where the product of corresponding elements is >= 10
    pos = bisect.bisect_left(mapped_list, lambda i: a[i] * b[i], 10)
    assert pos == 2, f"Expected index 2 but got {pos}"

def test_maplist_range():
    # Define the list and its length
    a = [1, 2, 3, 4, 5]
    b_length = len(a)

    # Wrap the range of indices with MapList and use a lambda function to transform elements
    mapped_list = MapList(lambda i: a[i] * b[i], range(b_length))

    # Use bisect.bisect_left to find the index where the product of corresponding elements is >= 10
    pos = bisect.bisect_left(mapped_list, lambda i: a[i] * b[i], 10)
    assert pos == 2, f"Expected index 2 but got {pos}"

# Run the tests
if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_MapList___len___0
flutes/Test4DT_tests/test_flutes_iterator_MapList___len___0.py:49:10: E0602: Undefined variable 'bisect' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_MapList___len___0.py:60:10: E0602: Undefined variable 'bisect' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_MapList___len___0.py:60:52: E0602: Undefined variable 'a' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_MapList___len___0.py:69:43: E0602: Undefined variable 'b' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_MapList___len___0.py:72:10: E0602: Undefined variable 'bisect' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_MapList___len___0.py:72:59: E0602: Undefined variable 'b' (undefined-variable)


"""