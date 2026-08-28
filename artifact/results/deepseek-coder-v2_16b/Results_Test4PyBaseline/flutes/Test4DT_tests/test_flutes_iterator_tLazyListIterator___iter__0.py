
import pytest
from typing import List
import weakref

# Assuming LazyList and its elements are defined somewhere
class LazyList:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def get_item(self, index):
        # Simulate fetching an item from the list
        return f"Item at index {index}"

class LazyListIterator:
    def __init__(self, lst: 'LazyList[T]'):
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

# Test cases for LazyListIterator
def test_lazy_list_iterator_initialization():
    lazy_list = LazyList()
    iterator = LazyListIterator(lazy_list)
    assert iterator.index == 0
    assert weakref.getweakrefcount(lazy_list) > 0

def test_lazy_list_iterator_iteration():
    lazy_list = LazyList([1, 2, 3, 4, 5])
    iterator = LazyListIterator(lazy_list)
    items = []
    for _ in range(6):
        items.append(next(iterator))