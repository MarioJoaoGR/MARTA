
import pytest
from typing import List, Iterable, Optional, TypeVar
import weakref
from itertools import islice

# Import the function to be tested
T = TypeVar('T')  # Define a type variable for the generic type T

class LazyList:
    """A wrapper over an iterable to allow lazily converting it into a list. The iterable is only iterated up to the accessed indices.
    
    Parameters:
        iterable (Iterable[T]): The iterable to wrap.
        
    Examples:
        >>> lst = LazyList([1, 2, 3, 4])
        >>> print(list(lst))  # Output: [1, 2, 3, 4]
        >>> print(lst[0])      # Output: 1
        >>> print(lst[2])      # Output: 3
        
    How to use the function effectively:
        - Create a LazyList object by passing an iterable to its constructor.
        - Access elements using indexing (e.g., lst[index]). The list will be populated lazily up to that index.
        - If you need to convert the entire lazy list into a regular Python list, simply use `list(lst)` or convert it directly where needed.
    """
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
    def __init__(self, iterable: Iterable[T]):
        self.iter = iter(iterable)
        self.exhausted = False
        self.list: List[T] = []
    
    def _fetch_until(self, idx: Optional[int]) -> None:
        if self.exhausted:
            return
        try:
            if idx is not None and idx < 0:
                idx = None  # otherwise we won't know when the sequence ends
            while idx is None or len(self.list) <= idx:
                self.list.append(next(self.iter))
        except StopIteration:
            self.exhausted = True
            del self.iter
    
    def __getitem__(self, idx):
        if isinstance(idx, slice):
            start, stop, step = idx.indices(len(self))
            result = LazyList(islice(self.iter, start, stop, step))
            return list(result)  # Convert to a regular list for the sake of simplicity in this example
        else:
            self._fetch_until(idx)
            return self.list[idx]
    
    def __len__(self):
        if not self.exhausted:
            while True:
                try:
                    next(self.iter)
                    self.list.append(None)  # Mark as accessed
                except StopIteration:
                    break
            self.exhausted = True
        return len(self.list)
    
    def __iter__(self):
        while not self.exhausted:
            yield from self.list
            try:
                next(self.iter)
                self.list.append(None)  # Mark as accessed
            except StopIteration:
                break

# Test cases for LazyList class
def test_lazy_list_creation():
    my_list = [1, 2, 3, 4]
    lazy_list = LazyList(my_list)