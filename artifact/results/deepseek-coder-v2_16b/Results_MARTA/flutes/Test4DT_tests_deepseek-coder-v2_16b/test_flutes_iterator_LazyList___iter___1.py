
import pytest
from typing import Iterable, List, TypeVar
import weakref

T = TypeVar('T')

class LazyList:
    'A wrapper over an iterable to allow lazily converting it into a list. The iterable is only iterated up to the accessed indices.'
    
    def __init__(self, iterable: Iterable[T]):
        self.iter = iter(iterable)
        self.exhausted = False
        self.list: List[T] = []

    def __iter__(self):
        if self.exhausted:
            return iter(self.list)
        return self.LazyListIterator(self)

    class LazyListIterator:
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

    def __getitem__(self, index: int) -> T:
        while len(self.list) <= index:
            try:
                next_item = next(self.iter)
                self.list.append(next_item)
            except StopIteration:
                raise IndexError("Index out of range")
        return self.list[index]

    def __len__(self):
        if not self.exhausted:
            while True:
                try:
                    next(self.iter)
                    self.list.append(None)  # Placeholder to indicate an item was accessed
                except StopIteration:
                    break
            self.exhausted = True
        return len(self.list)

# Test cases for LazyList class
def test_lazy_list_iteration():
    numbers = [1, 2, 3, 4]
    lazy_list = LazyList(numbers)
    iterated_items = []
    for item in lazy_list:
        iterated_items.append(item)
    assert iterated_items == [1, 2, 3, 4]

def test_lazy_list_getitem():
    numbers = [1, 2, 3, 4]
    lazy_list = LazyList(numbers)
    assert lazy_list[0] == 1
    assert lazy_list[2] == 3
    with pytest.raises(IndexError):
        lazy_list[10]

def test_lazy_list_len():
    numbers = [1, 2, 3, 4]
    lazy_list = LazyList(numbers)
    assert len(lazy_list) == 4
    # Accessing elements beyond the original length should not affect the length calculation
    with pytest.raises(IndexError):
        _ = lazy_list[10]
    assert len(lazy_list) == 4
