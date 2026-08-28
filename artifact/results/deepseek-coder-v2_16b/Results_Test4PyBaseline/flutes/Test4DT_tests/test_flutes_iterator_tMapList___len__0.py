
import pytest
from typing import Callable, Sequence, TypeVar
import bisect

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

    def __getitem__(self, index):
        return self.func(self.list[index])

    def __len__(self) -> int:
        return len(self.list)

# Test cases for MapList class
def test_maplist_basic():
    # Define a transformation function
    def square(x):
        return x * x

    # Create a list to be wrapped
    original_list = [1, 2, 3, 4, 5]

    # Wrap the list with MapList and perform a transformation
    mapped_list = MapList(square, original_list)

    # Use bisect_left to find the index of the first element whose square is >= 10
    pos = bisect.bisect_left(mapped_list, 10)
    assert pos == 3  # since 4^2 is the first element >= 10

def test_maplist_lambda():
    # Create a list to be wrapped
    original_list = [1, 2, 3, 4, 5]

    # Wrap the list with MapList and perform a transformation using a lambda function
    mapped_list = MapList(lambda x: x * x, original_list)

    # Use bisect_left to find the index of the first element whose square is >= 10
    pos = bisect.bisect_left(mapped_list, 10)
    assert pos == 3  # since 4^2 is the first element >= 10

def test_maplist_complex():
    # Define a transformation function that uses indices to access elements from two lists
    def multiply_elements(i):
        return original_list[i] * another_list[i]

    # Create the lists to be wrapped
    original_list = [1, 2, 3, 4, 5]
    another_list = [2, 3, 4, 5, 6]

    # Wrap the list with MapList and perform a transformation using the defined function
    mapped_list = MapList(multiply_elements, range(len(original_list)))

    # Use bisect_left to find the index where the product of corresponding elements is >= 10
    pos = bisect.bisect_left(mapped_list, 10)
    assert pos == 2  # since 3 * 4 is the first pair whose product >= 10
