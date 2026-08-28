
import pytest
from flutes.iterator import MapList


def test_valid_initialization():
    # Test with valid arguments
    map_list = MapList(lambda x: x * x, [1, 2, 3])
    assert list(map_list) == [1, 4, 9]

def test_index_access():
    # Test indexing access
    map_list = MapList(lambda x: x + 10, [1, 2, 3])
    assert map_list[0] == 11
    assert map_list[1] == 12

def test_slice_access():
    # Test slice access
    map_list = MapList(lambda x: x * 2, [1, 2, 3, 4, 5])
    assert list(map_list[1:4]) == [4, 6, 8]

def test_iteration():
    # Test iteration over elements
    map_list = MapList(lambda x: x - 1, [10, 20, 30])
    assert list(map_list) == [9, 19, 29]

def test_length():
    # Test length of the MapList instance
    map_list = MapList(lambda x: x, [1, 2, 3, 4, 5])
    assert len(map_list) == 5

def test_bisect_left():
    # Test using bisect_left with MapList
    import bisect
    map_list = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    pos = bisect.bisect_left(map_list, 10)
    assert pos == 3

def test_complex_transformation():
    # Test with a more complex transformation function
    map_list = MapList(lambda x: x * 2 + 3, [1, 2, 3])
    assert list(map_list) == [5, 7, 9]