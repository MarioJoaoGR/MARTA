
import pytest
from typing import Iterable, List, TypeVar
import weakref

T = TypeVar('T')

class LazyList:
    """A wrapper over an iterable to allow lazily converting it into a list. The iterable is only iterated up to the accessed indices.
    
    Parameters:
        iterable (Iterable[T]): The iterable to wrap.
        
    Returns:
        None
        
    Example usage:
        >>> lazy_list = LazyList([1, 2, 3, 4])
        >>> for item in lazy_list:
        ...     print(item)
        # Output will be 1, then 2, then 3, then 4 as the iterable is iterated over.
        
        >>> lazy_list = LazyList([1, 2, 3, 4])
        >>> print(lazy_list[0])  # Accessing the first element of the list will not iterate further.
        # Output: 1
        
        >>> lazy_list = LazyList([1, 2, 3, 4])
        >>> print(len(lazy_list))  # This will raise a TypeError because the iterable is still being iterated over.
        # Raises TypeError: __len__ is not available before the iterable is depleted
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

    def __len__(self):
        if self.exhausted:
            return len(self.list)
        else:
            raise TypeError("__len__ is not available before the iterable is depleted")

def test_invalid_len():
    lazy_list = LazyList([1, 2, 3, 4])
    with pytest.raises(TypeError):
        len(lazy_list)
