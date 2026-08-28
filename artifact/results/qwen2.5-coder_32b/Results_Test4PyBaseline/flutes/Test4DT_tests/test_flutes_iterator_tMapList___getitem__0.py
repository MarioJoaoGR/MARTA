
# Test case  
import pytest
from flutes.iterator import MapList

def test_maplist_basic_transformation():
    # Test basic transformation with a simple function
    map_list_instance = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert map_list_instance[0] == 1
    assert map_list_instance[2] == 9
    assert map_list_instance[4] == 25

def test_maplist_slice():
    # Test slicing functionality
    map_list_instance = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert list(map_list_instance[1:4]) == [4, 9, 16]

def test_maplist_bisect():
    # Test using bisect with a transformed list
    import bisect
    map_list_instance = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    pos = bisect.bisect_left(map_list_instance, 10)
    assert pos == 3

def test_maplist_index_based_transformation():
    # Test transformation with index-based function
    import bisect
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    map_list_instance = MapList(lambda i: a[i] * b[i], range(len(a)))
    pos = bisect.bisect_left(map_list_instance, 10)
    assert pos == 2

def test_maplist_empty_list():
    # Test with an empty list
    map_list_instance = MapList(lambda x: x * x, [])
    assert len(list(map_list_instance)) == 0

def test_maplist_single_element():
    # Test with a single element
    map_list_instance = MapList(lambda x: x * x, [3])
    assert map_list_instance[0] == 9

def test_maplist_negative_indexing():
    # Test negative indexing
    map_list_instance = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert map_list_instance[-1] == 25