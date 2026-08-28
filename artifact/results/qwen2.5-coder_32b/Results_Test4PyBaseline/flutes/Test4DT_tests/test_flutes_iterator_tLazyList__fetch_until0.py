# Module: flutes.iterator
import pytest
from flutes.iterator import LazyList

def test_lazy_list_with_generator():
    def my_generator():
        for i in range(5):
            yield i * 2

    lazy_list = LazyList(my_generator())

    # Test accessing elements lazily
    assert lazy_list[0] == 0
    assert lazy_list[1] == 2

    # Test iterating over the entire list
    assert list(lazy_list) == [0, 2, 4, 6, 8]

    # Test accessing a slice of elements
    assert lazy_list[2:5] == [4, 6, 8]

def test_lazy_list_with_list():
    lazy_list = LazyList([10, 20, 30])

    # Test accessing elements lazily
    assert lazy_list[0] == 10

    # Test iterating over the entire list
    assert list(lazy_list) == [10, 20, 30]

def test_lazy_list_with_tuple():
    lazy_list = LazyList((5, 10, 15))

    # Test accessing elements lazily
    assert lazy_list[1] == 10

    # Test iterating over the entire list
    assert list(lazy_list) == [5, 10, 15]

def test_lazy_list_with_infinite_generator():
    def infinite_generator():
        i = 0
        while True:
            yield i * 3
            i += 1

    lazy_infinite_list = LazyList(infinite_generator())

    # Test accessing the first few elements lazily
    assert lazy_infinite_list[0] == 0
    assert lazy_infinite_list[1] == 3

    # Test iterating over a slice of the infinite list (safe)
    assert list(lazy_infinite_list[:5]) == [0, 3, 6, 9, 12]

def test_lazy_list_index_error():
    def my_generator():
        for i in range(5):
            yield i * 2

    lazy_list = LazyList(my_generator())

    # Test accessing an out-of-bounds index
    with pytest.raises(IndexError):
        _ = lazy_list[10]

def test_lazy_list_empty_iterable():
    lazy_list = LazyList([])

    # Test iterating over an empty list
    assert list(lazy_list) == []

    # Test accessing an element from an empty list
    with pytest.raises(IndexError):
        _ = lazy_list[0]
