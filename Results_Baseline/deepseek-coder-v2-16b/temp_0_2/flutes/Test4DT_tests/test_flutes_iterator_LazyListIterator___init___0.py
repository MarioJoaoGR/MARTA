# Module: flutes.iterator
import pytest
from typing import List
import weakref

class LazyList:
    def __init__(self, data=None):
        self.data = data if data is not None else []
    
    def __getitem__(self, index):
        return self.data[index]

class LazyListIterator:
    """
    A class representing an iterator for a lazy list, which fetches elements on demand.

    Attributes:
        list (weakref.ref): A weak reference to the underlying LazyList object.
        index (int): The current index of the iteration.

    Methods:
        __iter__(): Returns the iterator itself.
        __next__(): Retrieves the next element from the lazy list if available, otherwise raises StopIteration.
    """
    def __init__(self, lst: 'LazyList[T]'):
        self.list = weakref.ref(lst)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            obj = self.list()[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return obj

# Fixture to create a LazyList and its iterator for testing
@pytest.fixture
def lazy_list():
    return LazyList([10, 20, 30])

# Test case to check the initialization of the iterator
def test_lazy_list_iterator_initialization(lazy_list):
    iterator = LazyListIterator(lazy_list)
    assert isinstance(iterator, LazyListIterator)
    assert iterator.index == 0
    assert weakref.ref(lazy_list)() is lazy_list

# Test case to iterate over the lazy list and check the elements
def test_lazy_list_iterator_iteration(lazy_list):
    iterator = LazyListIterator(lazy_list)
    items = []
    for item in iterator:
        items.append(item)
    assert items == [10, 20, 30]

# Test case to check the iteration raises StopIteration when exhausted
def test_lazy_list_iterator_exhausted():
    lazy_list = LazyList([1])
    iterator = LazyListIterator(lazy_list)
    assert next(iterator) == 1
    with pytest.raises(StopIteration):
        next(iterator)
