# Module: flutes.iterator
import pytest
from typing import List
import weakref

class LazyList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_item(self, index):
        return self.items[index]

class LazyListIterator:
    def __init__(self, lst: 'LazyList'):
        self.list = weakref.ref(lst)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            obj = self.list().get_item(self.index)
        except IndexError:
            raise StopIteration
        self.index += 1
        return obj

# Example usage
@pytest.fixture
def lazy_list():
    lst = LazyList()
    lst.add_item(10)
    lst.add_item(20)
    lst.add_item(30)
    return lst

def test_lazy_list_iterator(lazy_list):
    iterator = LazyListIterator(lazy_list)
    items = []
    for item in iterator:
        items.append(item)
    assert items == [10, 20, 30]

def test_empty_lazy_list():
    lazy_list = LazyList()
    iterator = LazyListIterator(lazy_list)
    with pytest.raises(StopIteration):
        next(iterator)

def test_single_item_lazy_list():
    lazy_list = LazyList()
    lazy_list.add_item(100)
    iterator = LazyListIterator(lazy_list)
    items = []
    for item in iterator:
        items.append(item)
    assert items == [100]
