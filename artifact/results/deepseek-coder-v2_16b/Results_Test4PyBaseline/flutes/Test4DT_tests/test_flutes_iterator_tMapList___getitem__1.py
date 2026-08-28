
import pytest
from typing import Callable, Sequence, TypeVar
import bisect  # Importing here since it was not recognized previously

T = TypeVar('T')
R = TypeVar('R')

class MapList:
    def __init__(self, func: Callable[[T], R], lst: Sequence[T]):
        self.func = func
        self.list = lst

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.func(self.list[item])
        return [self.func(x) for x in self.list[item]]

    def __len__(self):
        return len(self.list)

def square(x: int) -> int:
    return x * x

def multiply_by_two(x: int) -> int:
    return x * 2

# Test cases for MapList class with different transformation functions

@pytest.fixture
def maplist_square():
    return MapList(square, [1, 2, 3, 4, 5])

@pytest.fixture
def maplist_multiply_by_two():
    return MapList(multiply_by_two, [1, 2, 3, 4, 5])

# Test cases for integer indexing
def test_maplist_integer_index(maplist_square):
    assert maplist_square[0] == 1  # 1^2
    assert maplist_square[1] == 4  # 2^2
    with pytest.raises(IndexError):
        maplist_square[10]  # Index out of range should raise an error

# Test cases for slice indexing
def test_maplist_slice_index(maplist_square):
    assert maplist_square[slice(1, 3)] == [4, 9]  # Squares of elements at indices 1 and 2

# Test cases for iteration
def test_maplist_iteration(maplist_multiply_by_two):
    result = []
    for item in maplist_multiply_by_two:
        result.append(item)
    assert result == [2, 4, 6, 8, 10]

# Test cases using bisect_left with MapList
def test_maplist_with_bisect_left():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    ml = MapList(lambda i: a[i] * b[i], range(len(a)))
    pos = bisect.bisect_left(ml, 10)
    assert pos == 2  # Since a[2]*b[2] = 3*4 = 12 which is the first pair >= 10

# Test cases for custom transformation function
def test_maplist_custom_function():
    ml = MapList(multiply_by_two, [1, 2, 3, 4, 5])
    assert ml[0] == 2  # 1 * 2
    assert ml[1] == 4  # 2 * 2
    result = []
    for item in ml:
        result.append(item)
    assert result == [2, 4, 6, 8, 10]

# Additional test cases to cover uncovered lines (393-395)
def test_maplist_getitem_invalid_index():
    ml = MapList(square, [1, 2, 3, 4, 5])
    with pytest.raises(TypeError):
        ml['invalid']  # Invalid index type should raise a TypeError

def test_maplist_getitem_negative_index():
    ml = MapList(square, [1, 2, 3, 4, 5])