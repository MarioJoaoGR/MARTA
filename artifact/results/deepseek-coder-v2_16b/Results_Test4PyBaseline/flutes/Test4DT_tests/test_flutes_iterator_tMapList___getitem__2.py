
import pytest
from typing import Callable, Sequence, TypeVar
import bisect

# Define type variables for generic types T and R
T = TypeVar('T')
R = TypeVar('R')

class MapList(object):
    def __init__(self, func: Callable[[T], R], lst: Sequence[T]):
        self.func = func
        self.list = lst

    def __getitem__(self, idx):
        if isinstance(idx, int):
            return self.func(self.list[idx])
        return [self.func(x) for x in self.list[idx]]

    def __iter__(self):
        return map(self.func, self.list)

    def __len__(self):
        return len(self.list)

# Test cases for MapList class
def test_maplist_basic():
    a = [1, 2, 3, 4, 5]
    mlist = MapList(lambda x: x * x, a)
    assert mlist[0] == 1  # 1^2
    assert mlist[1] == 4  # 2^2
    assert mlist[2] == 9  # 3^2
    assert len(mlist) == 5

def test_maplist_slice():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    mlist_slice = MapList(lambda x: a[x] * b[x], range(len(a)))
    pos = bisect.bisect_left(mlist_slice, 10)
    assert pos == 2  # since 3^2 * 4 == 9 and 4^2 * 5 == 16 are the first elements >= 10

def test_maplist_iteration():
    a = [1, 2, 3, 4, 5]
    mlist = MapList(lambda x: x * x, a)
    transformed_items = [item for item in mlist]
    assert transformed_items == [1, 4, 9, 16, 25]

def test_maplist_different_transformations():
    c = [3, 6, 9, 12, 15]
    mlist_cube = MapList(lambda x: x ** 3, c)
    transformed_items = [item for item in mlist_cube]
    assert transformed_items == [27, 216, 729, 1728, 3375]

def test_maplist_string_transformations():
    words = ["hello", "world", "this", "is", "a", "test"]
    mlist_lengths = MapList(lambda word: len(word), words)
    transformed_items = [item for item in mlist_lengths]
    assert transformed_items == [5, 5, 4, 2, 1, 4]
