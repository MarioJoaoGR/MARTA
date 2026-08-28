
import pytest
from flutes.iterator import LazyList

def test_valid_iterable():
    # Test with a valid iterable: a list
    lazy_list = LazyList([1, 2, 3])
    assert list(lazy_list) == [1, 2, 3]

def test_invalid_iterable():
    # Test with an invalid iterable: an integer (should raise TypeError)
    with pytest.raises(TypeError):
        LazyList(123)

def test_generator_iterable():
    # Test with a generator
    def my_generator():
        for i in range(3):
            yield i * i

    lazy_list = LazyList(my_generator())
    assert list(lazy_list) == [0, 1, 4]

def test_empty_iterable():
    # Test with an empty iterable: an empty list
    lazy_list = LazyList([])
    assert list(lazy_list) == []

def test_index_access():
    # Test accessing elements by index
    lazy_list = LazyList([10, 20, 30])
    assert lazy_list[0] == 10
    assert lazy_list[1] == 20

def test_slice_access():
    # Test accessing slices
    lazy_list = LazyList([10, 20, 30, 40, 50])
    assert lazy_list[:2] == [10, 20]
    assert lazy_list[1:4] == [20, 30, 40]
