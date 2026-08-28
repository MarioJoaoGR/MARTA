
import pytest
from flutes.iterator import MapList



def test_valid_function_and_list():
    # Test with a valid function and list
    map_list_instance = MapList(lambda x: x * x, [1, 2, 3])
    assert map_list_instance[0] == 1
    assert map_list_instance[1] == 4

def test_length_of_maplist():
    # Test the length of the MapList instance
    map_list_instance = MapList(lambda x: x * x, [1, 2, 3])
    assert len(map_list_instance) == 3

def test_index_out_of_range():
    # Test accessing an index out of range
    map_list_instance = MapList(lambda x: x * x, [1, 2, 3])
    with pytest.raises(IndexError):
        _ = map_list_instance[5]

def test_iteration_over_maplist():
    # Test iteration over the MapList instance
    map_list_instance = MapList(lambda x: x * x, [1, 2, 3])
    expected_values = [1, 4, 9]
    for i, value in enumerate(map_list_instance):
        assert value == expected_values[i]

def test_slice_of_maplist():
    # Test slicing the MapList instance
    map_list_instance = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    sliced_values = map_list_instance[1:4]
    assert sliced_values == [4, 9, 16]

def test_empty_maplist():
    # Test with an empty list
    map_list_instance = MapList(lambda x: x * x, [])
    assert len(map_list_instance) == 0