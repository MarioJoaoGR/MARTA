
import pytest
from flutes.iterator import MapList


def test_valid_transformation_function():
    # Test valid transformation function
    map_list = MapList(lambda x: x * 2, [1, 2, 3])
    assert map_list[0] == 2

def test_index_access():
    # Test indexing access
    map_list = MapList(lambda x: x + 1, [1, 2, 3])
    assert map_list[1] == 3

def test_slice_access():
    # Test slice access
    map_list = MapList(lambda x: x * 3, [1, 2, 3, 4, 5])
    assert map_list[1:4] == [6, 9, 12]

def test_iteration():
    # Test iteration
    map_list = MapList(lambda x: x - 1, [1, 2, 3])
    assert list(map_list) == [0, 1, 2]

def test_length():
    # Test length
    map_list = MapList(lambda x: x, [1, 2, 3, 4, 5])
    assert len(map_list) == 5

def test_bisect_left():
    # Test with bisect_left
    import bisect
    a = [1, 2, 3, 4, 5]
    squared_map_list = MapList(lambda x: x * x, a)
    pos = bisect.bisect_left(squared_map_list, 10)
    assert pos == 3

def test_bisect_left_with_product():
    # Test with bisect_left using product
    import bisect
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    product_map_list = MapList(lambda i: a[i] * b[i], range(len(a)))
    pos = bisect.bisect_left(product_map_list, 10)
    assert pos == 2