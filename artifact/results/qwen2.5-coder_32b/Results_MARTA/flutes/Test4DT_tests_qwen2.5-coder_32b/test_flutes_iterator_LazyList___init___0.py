
import pytest
from flutes.iterator import LazyList

def test_lazy_list_with_empty_iterable():
    lazy_list_empty = LazyList([])
    assert list(lazy_list_empty) == []

def test_lazy_list_with_none_iterable():
    with pytest.raises(TypeError):
        LazyList(None)

def test_lazy_list_with_generator():
    def my_generator():
        for i in range(5):
            yield i * i

    lazy_list_gen = LazyList(my_generator())
    assert list(lazy_list_gen) == [0, 1, 4, 9, 16]

def test_lazy_list_with_list():
    my_list = [1, 2, 3, 4, 5]
    lazy_list_from_list = LazyList(my_list)
    assert list(lazy_list_from_list) == [1, 2, 3, 4, 5]

def test_lazy_list_element_access():
    def my_generator():
        for i in range(5):
            yield i * i

    lazy_list_gen = LazyList(my_generator())
    assert lazy_list_gen[0] == 0
    assert lazy_list_gen[2] == 4

def test_lazy_list_slice_access():
    def my_generator():
        for i in range(5):
            yield i * i

    lazy_list_gen = LazyList(my_generator())
    assert list(lazy_list_gen[:3]) == [0, 1, 4]

def test_lazy_list_length_after_exhaustion():
    def my_generator():
        for i in range(5):
            yield i * i

    lazy_list_gen = LazyList(my_generator())
    list(lazy_list_gen)  # Exhaust the generator
    assert len(lazy_list_gen) == 5
