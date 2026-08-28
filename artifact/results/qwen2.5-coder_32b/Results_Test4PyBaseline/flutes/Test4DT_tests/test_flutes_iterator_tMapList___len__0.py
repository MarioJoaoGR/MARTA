# Module: flutes.iterator
import pytest
from flutes.iterator import MapList

def test_maplist_basic_transformation():
    a = [1, 2, 3, 4, 5]
    map_list_instance = MapList(lambda x: x * x, a)
    
    assert map_list_instance[0] == 1
    assert map_list_instance[1] == 4
    assert map_list_instance[2] == 9
    assert map_list_instance[3] == 16
    assert map_list_instance[4] == 25

def test_maplist_slice():
    a = [1, 2, 3, 4, 5]
    map_list_instance = MapList(lambda x: x * x, a)
    
    assert list(map_list_instance[1:4]) == [4, 9, 16]

def test_maplist_iteration():
    a = [1, 2, 3, 4, 5]
    map_list_instance = MapList(lambda x: x * x, a)
    
    expected = [1, 4, 9, 16, 25]
    for i, value in enumerate(map_list_instance):
        assert value == expected[i]

def test_maplist_bisect():
    import bisect
    
    a = [1, 2, 3, 4, 5]
    map_list_instance = MapList(lambda x: x * x, a)
    
    pos = bisect.bisect_left(map_list_instance, 10)
    assert pos == 3

def test_maplist_index_error():
    a = [1, 2, 3, 4, 5]
    map_list_instance = MapList(lambda x: x * x, a)
    
    with pytest.raises(IndexError):
        _ = map_list_instance[5]

def test_maplist_empty_list():
    map_list_instance = MapList(lambda x: x * x, [])
    
    assert len(map_list_instance) == 0
    assert list(map_list_instance) == []

def test_maplist_with_indices():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    map_list_instance = MapList(lambda i: a[i] * b[i], range(len(a)))
    
    assert list(map_list_instance) == [2, 6, 12, 20, 30]

def test_maplist_lambda_transformation():
    map_list_lambda = MapList(lambda x: x + 5, [10, 20, 30])
    
    assert map_list_lambda[0] == 15
    assert map_list_lambda[1] == 25
    assert map_list_lambda[2] == 35

def test_maplist_len():
    a = [1, 2, 3, 4, 5]
    map_list_instance = MapList(lambda x: x * x, a)
    
    assert len(map_list_instance) == 5
