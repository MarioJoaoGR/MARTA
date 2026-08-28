
import pytest
from typing import List, Iterable, TypeVar
import weakref

T = TypeVar('T')

class LazyList:
    'A wrapper over an iterable to allow lazily converting it into a list. The iterable is only iterated up to the accessed indices.'
    
    def __init__(self, iterable: Iterable[T]):
        self.iter = iter(iterable)
        self.exhausted = False
        self.list: List[T] = []

    def __getitem__(self, index: int) -> T:
        while len(self.list) <= index and not self.exhausted:
            try:
                item = next(self.iter)
                self.list.append(item)
            except StopIteration:
                self.exhausted = True
                raise IndexError("Index out of range") from None
        if len(self.list) <= index:
            raise IndexError("Index out of range")
        return self.list[index]

    def __len__(self):
        if self.exhausted:
            return len(self.list)
        else:
            raise TypeError("__len__ is not available before the iterable is depleted")

# Test cases for LazyList class
def test_lazy_list_iteration():
    lazy_list = LazyList([1, 2, 3, 4])
    iterated_items = []
    for item in lazy_list:
        iterated_items.append(item)
    assert iterated_items == [1, 2, 3, 4]

def test_lazy_list_index_access():
    lazy_list = LazyList([1, 2, 3, 4])
    assert lazy_list[0] == 1
    assert lazy_list[2] == 3

def test_lazy_list_len_after_iteration():
    lazy_list = LazyList([1, 2, 3, 4])
    for _ in lazy_list:
        pass
    assert len(lazy_list) == 4

def test_lazy_list_index_error():
    lazy_list = LazyList([1, 2, 3, 4])
    with pytest.raises(IndexError):
        print(lazy_list[5])
