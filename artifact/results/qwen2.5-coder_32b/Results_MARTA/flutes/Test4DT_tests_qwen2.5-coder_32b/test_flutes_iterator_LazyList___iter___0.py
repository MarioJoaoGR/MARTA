
import pytest
from flutes.iterator import LazyList

def test_empty_iterable():
    lazy_list_empty = LazyList([])
    assert list(lazy_list_empty) == []

def test_non_iterable_input():
    with pytest.raises(TypeError):
        LazyList(None)

def test_single_element():
    lazy_list_single = LazyList([42])
    assert list(lazy_list_single) == [42]

def test_multiple_elements():
    lazy_list_multiple = LazyList(range(5))
    assert list(lazy_list_multiple) == [0, 1, 2, 3, 4]

def test_generator_input():
    def my_generator():
        for i in range(3):
            yield i * i
    lazy_list_gen = LazyList(my_generator())
    assert list(lazy_list_gen) == [0, 1, 4]
