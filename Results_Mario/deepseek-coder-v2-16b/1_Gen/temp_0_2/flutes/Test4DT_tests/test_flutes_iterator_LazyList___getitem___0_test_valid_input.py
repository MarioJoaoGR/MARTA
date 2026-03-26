
import pytest
from typing import Iterable, List, TypeVar
import weakref

T = TypeVar('T')

class LazyList:
    """A wrapper over an iterable to allow lazily converting it into a list. The iterable is only iterated up to the accessed indices.
    
    Parameters:
        iterable (Iterable[T]): The iterable to wrap.
        
    Examples:
        >>> lazy_list = LazyList([1, 2, 3, 4])
        >>> print(list(lazy_list))  # Output: [1, 2, 3, 4]
        >>> print(lazy_list[0])      # Output: 1
        >>> print(lazy_list[2])      # Output: 3
        
    The `LazyList` class provides a way to access elements of an iterable in a lazy manner. Elements are only fetched from the iterable as they are accessed, up to the requested index. Once exhausted, accessing further indices will not fetch additional elements but will raise an IndexError if the index is out of range.
    """
    def __init__(self, iterable: Iterable[T]):
        self.iter = iter(iterable)
        self.exhausted = False
        self.list: List[T] = []

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

    def __getitem__(self, idx: int) -> T:
        while len(self.list) <= idx and not self.exhausted:
            try:
                item = next(self.iter)
                self.list.append(item)
            except StopIteration:
                self.exhausted = True
                raise IndexError("Index out of range")
        if idx >= len(self.list):
            raise IndexError("Index out of range")
        return self.list[idx]

def test_valid_input():
    lazy_list = LazyList([1, 2, 3, 4])
    assert list(lazy_list) == [1, 2, 3, 4]
    assert lazy_list[0] == 1
    assert lazy_list[1] == 2
    assert lazy_list[2] == 3
    assert lazy_list[3] == 4
    with pytest.raises(IndexError):
        lazy_list[4]
