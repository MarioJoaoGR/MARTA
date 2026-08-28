# Module: flutes.iterator
import pytest
from flutes.iterator import LazyList

def test_lazy_list_with_generator():
    def my_generator():
        for i in range(5):
            yield i * i

    lazy_list = LazyList(my_generator())
    
    # Test accessing elements by index
    assert lazy_list[0] == 0
    assert lazy_list[1] == 1
    assert lazy_list[2] == 4
    
    # Convert to list and check all elements
    assert list(lazy_list) == [0, 1, 4, 9, 16]
    
    # Check length after exhaustion
    assert len(lazy_list) == 5

def test_lazy_list_with_list():
    lazy_list = LazyList([10, 20, 30])
    
    # Test accessing elements by index
    assert lazy_list[0] == 10
    assert lazy_list[1] == 20
    
    # Convert to list and check all elements
    assert list(lazy_list) == [10, 20, 30]
    
    # Check length after exhaustion
    assert len(lazy_list) == 3

def test_lazy_list_iteration():
    lazy_list = LazyList(range(5))
    
    # Test iteration
    result = []
    for item in lazy_list:
        result.append(item)
        
    assert result == [0, 1, 2, 3, 4]
    
    # Check length after exhaustion
    assert len(lazy_list) == 5

def test_lazy_list_slices():
    lazy_list = LazyList(range(10))
    
    # Test slicing
    assert lazy_list[2:5] == [2, 3, 4]
    
    # Convert to list and check all elements
    assert list(lazy_list) == list(range(10))
    
    # Check length after exhaustion
    assert len(lazy_list) == 10

def test_lazy_list_exhaustion():
    lazy_list = LazyList(range(3))
    
    # Exhaust the iterable
    assert list(lazy_list) == [0, 1, 2]
    
    # Check length after exhaustion
    assert len(lazy_list) == 3

def test_lazy_list_custom_iterable():
    class MyIterable:
        def __iter__(self):
            for i in range(3):
                yield i * 2

    my_iterable = MyIterable()
    lazy_list = LazyList(my_iterable)
    
    # Test accessing elements by index
    assert lazy_list[0] == 0
    assert lazy_list[1] == 2
    
    # Convert to list and check all elements
    assert list(lazy_list) == [0, 2, 4]
    
    # Check length after exhaustion
    assert len(lazy_list) == 3

def test_lazy_list_len_before_exhaustion():
    lazy_list = LazyList(range(5))
    
    # Test that TypeError is raised when trying to get length before exhaustion
    with pytest.raises(TypeError):
        len(lazy_list)
