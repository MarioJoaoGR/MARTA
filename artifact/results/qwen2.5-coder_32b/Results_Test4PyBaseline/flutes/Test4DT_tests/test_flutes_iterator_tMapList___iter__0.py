# Module: flutes.iterator
import pytest
from flutes.iterator import MapList

def test_maplist_basic_transformation():
    # Test basic transformation using a simple function
    def square(x):
        return x * x
    
    a = [1, 2, 3, 4, 5]
    map_list_instance = MapList(square, a)
    
    assert map_list_instance[0] == 1
    assert map_list_instance[2] == 9
    assert list(map_list_instance) == [1, 4, 9, 16, 25]

def test_maplist_index_transformation():
    # Test transformation using a function that operates on indices
    def multiply_elements(i):
        return a[i] * b[i]
    
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    map_list_instance_2 = MapList(multiply_elements, range(len(a)))
    
    assert map_list_instance_2[0] == 2
    assert map_list_instance_2[2] == 12
    assert list(map_list_instance_2) == [2, 6, 12, 20, 30]

def test_maplist_lambda_transformation():
    # Test using lambda functions for transformations
    map_list_lambda = MapList(lambda x: x + 5, [10, 20, 30])
    
    assert map_list_lambda[0] == 15
    assert map_list_lambda[1] == 25
    assert list(map_list_lambda) == [15, 25, 35]

def test_maplist_string_transformation():
    # Test using a transformation function with strings
    def uppercase(s):
        return s.upper()
    
    words = ["apple", "banana", "cherry"]
    map_list_strings = MapList(uppercase, words)
    
    assert map_list_strings[0] == "APPLE"
    assert map_list_strings[2] == "CHERRY"
    assert list(map_list_strings) == ["APPLE", "BANANA", "CHERRY"]

def test_maplist_empty_list():
    # Test with an empty list
    map_list_empty = MapList(lambda x: x, [])
    
    assert list(map_list_empty) == []

def test_maplist_single_element():
    # Test with a single element
    map_list_single = MapList(lambda x: x * 2, [5])
    
    assert map_list_single[0] == 10
    assert list(map_list_single) == [10]

def test_maplist_negative_numbers():
    # Test with negative numbers
    def negate(x):
        return -x
    
    negatives = [-1, -2, -3]
    map_list_negatives = MapList(negate, negatives)
    
    assert map_list_negatives[0] == 1
    assert map_list_negatives[2] == 3
    assert list(map_list_negatives) == [1, 2, 3]

def test_maplist_mixed_types():
    # Test with mixed types (should raise TypeError if function is not compatible)
    def square(x):
        return x * x
    
    mixed = [1, 'a', 3]
    map_list_mixed = MapList(square, mixed)
    
    assert map_list_mixed[0] == 1
    with pytest.raises(TypeError):
        _ = map_list_mixed[1]  # Attempting to square a string should raise TypeError
    assert map_list_mixed[2] == 9

def test_maplist_bisect_left():
    import bisect
    
    # Test using bisect.bisect_left with MapList
    def square(x):
        return x * x
    
    a = [1, 2, 3, 4, 5]
    map_list_instance = MapList(square, a)
    
    pos = bisect.bisect_left(map_list_instance, 10)
    assert pos == 3

def test_maplist_bisect_right():
    import bisect
    
    # Test using bisect.bisect_right with MapList
    def square(x):
        return x * x
    
    a = [1, 2, 3, 4, 5]
    map_list_instance = MapList(square, a)
    
    pos = bisect.bisect_right(map_list_instance, 9)
    assert pos == 3
