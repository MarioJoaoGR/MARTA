# Module: flutes.iterator
import pytest
from flutes.iterator import LazyList

def test_lazy_list_with_generator():
    def my_generator():
        for i in range(5):
            yield i * i

    lazy_list = LazyList(my_generator())
    
    # Test accessing elements lazily
    assert lazy_list[0] == 0
    assert lazy_list[1] == 1
    
    # Convert to list and check all elements
    assert list(lazy_list) == [0, 1, 4, 9, 16]

def test_lazy_list_with_list():
    data = [10, 20, 30]
    lazy_list = LazyList(data)
    
    # Test accessing elements lazily
    assert lazy_list[0] == 10
    assert lazy_list[1] == 20
    
    # Convert to list and check all elements
    assert list(lazy_list) == [10, 20, 30]

def test_lazy_list_iteration():
    def my_generator():
        for i in range(5):
            yield i * i

    lazy_list = LazyList(my_generator())
    
    # Test iteration
    result = []
    for item in lazy_list:
        result.append(item)
        
    assert result == [0, 1, 4, 9, 16]

def test_lazy_list_slice():
    def my_generator():
        for i in range(5):
            yield i * i

    lazy_list = LazyList(my_generator())
    
    # Test slicing
    assert lazy_list[2:5] == [4, 9, 16]
    assert lazy_list[:3] == [0, 1, 4]
    assert lazy_list[3:] == [9, 16]

def test_lazy_list_index_error():
    def my_generator():
        for i in range(5):
            yield i * i

    lazy_list = LazyList(my_generator())
    
    # Test index error
    with pytest.raises(IndexError):
        _ = lazy_list[10]
