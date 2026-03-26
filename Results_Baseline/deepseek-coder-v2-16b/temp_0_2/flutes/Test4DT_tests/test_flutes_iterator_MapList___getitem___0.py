
# Module: flutes.iterator
import pytest
from flutes.iterator import MapList
import bisect  # Importing here since it's used in multiple tests

# Test initialization with a lambda function that squares each element
def test_maplist_initialization():
    mapped_list = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert list(mapped_list) == [1, 4, 9, 16, 25]

# Test indexing in the transformed list
def test_maplist_indexing():
    mapped_list = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert mapped_list[0] == 1
    assert mapped_list[1] == 4
    assert mapped_list[2] == 9
    assert mapped_list[3] == 16
    assert mapped_list[4] == 25

# Test slicing in the transformed list
def test_maplist_slicing():
    mapped_list = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert list(mapped_list[1:3]) == [4, 9]

# Test iteration over the transformed list
def test_maplist_iteration():
    mapped_list = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    result = []
    for item in mapped_list:
        result.append(item)
    assert result == [1, 4, 9, 16, 25]

# Test length of the transformed list
def test_maplist_length():
    mapped_list = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert len(mapped_list) == 5

# Test using MapList with bisect functions
def test_maplist_with_bisect():
    a = [1, 2, 3, 4, 5]
    mapped_list = MapList(lambda x: x * x, a)
    pos = bisect.bisect_left(mapped_list, 10)
    assert pos == 3

    b = [2, 3, 4, 5, 6]
    mapped_list = MapList(lambda i: a[i] * b[i], range(len(a)))
    pos = bisect.bisect_left(mapped_list, 10)
    assert pos == 2
