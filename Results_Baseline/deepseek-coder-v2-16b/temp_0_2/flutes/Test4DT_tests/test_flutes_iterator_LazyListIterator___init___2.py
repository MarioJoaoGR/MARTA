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

# Test cases for LazyListIterator
def test_lazy_list_iterator():
    lazy_list = LazyList([10, 20, 30])
    iterator = LazyListIterator(lazy_list)
    
    items = []
    for item in iterator:
        items.append(item)
    
    assert items == [10, 20, 30]

def test_empty_lazy_list():
    lazy_list = LazyList([])
    iterator = LazyListIterator(lazy_list)
    
    with pytest.raises(StopIteration):
        next(iterator)

def test_single_item_lazy_list():
    lazy_list = LazyList([42])
    iterator = LazyListIterator(lazy_list)
    
    items = []
    for item in iterator:
        items.append(item)
    
    assert items == [42]

def test_multiple_items_lazy_list():
    lazy_list = LazyList([1, 2, 3, 4, 5])
    iterator = LazyListIterator(lazy_list)
    
    items = []
    for item in iterator:
        items.append(item)
    
    assert items == [1, 2, 3, 4, 5]
