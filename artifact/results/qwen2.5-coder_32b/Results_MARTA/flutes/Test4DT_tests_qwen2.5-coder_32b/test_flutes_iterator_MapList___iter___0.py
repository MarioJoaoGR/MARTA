
import pytest
from typing import Callable, Sequence
from flutes.iterator import MapList



def test_valid_function():
    # Test with a valid function, should not raise any error
    map_list = MapList(lambda x: x * 2, [1, 2, 3])
    assert list(map_list) == [2, 4, 6]

def test_index_access():
    # Test indexing access on the transformed list
    map_list = MapList(lambda x: x + 1, [10, 20, 30])
    assert map_list[0] == 11
    assert map_list[1] == 21

def test_slice_access():
    # Test slice access on the transformed list
    map_list = MapList(lambda x: x * 3, [1, 2, 3, 4, 5])
    assert list(map_list[1:4]) == [6, 9, 12]

def test_length():
    # Test length of the transformed list
    map_list = MapList(lambda x: x, [1, 2, 3, 4, 5])
    assert len(map_list) == 5

def test_iteration():
    # Test iteration over the transformed list
    map_list = MapList(lambda x: x - 1, [5, 6, 7])
    assert list(iter(map_list)) == [4, 5, 6]

def test_bisect_left():
    # Test integration with bisect.bisect_left
    import bisect
    map_list = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    pos = bisect.bisect_left(map_list, 10)
    assert pos == 3