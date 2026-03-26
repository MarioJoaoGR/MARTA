
import pytest
from typing import Iterable, List, TypeVar
import weakref

T = TypeVar('T')

class LazyList:
    """A wrapper over an iterable to allow lazily converting it into a list. The iterable is only iterated up to the accessed indices.
    
    Parameters:
        iterable (Iterable): The iterable to wrap.
        
    Returns:
        None
        
    Example:
        To create a LazyList from an iterable, you can use the following code:
        
        ```python
        my_list = [1, 2, 3, 4, 5]
        lazy_list = LazyList(my_list)
        
        # Access elements of the lazy list one by one
        for element in lazy_list:
            print(element)
        ```
        
        In this example, the iterable `[1, 2, 3, 4, 5]` is wrapped in a LazyList. Elements are accessed lazily as you iterate over the lazy list. Only the elements up to the point of iteration are stored and iterated upon.
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
    
    def _fetch_until(self, idx: int):
        while len(self.list) <= idx and not self.exhausted:
            try:
                element = next(self.iter)
                self.list.append(element)
            except StopIteration:
                self.exhausted = True
    
    def __getitem__(self, idx):
        if isinstance(idx, slice):
            self._fetch_until(idx.stop - 1)
        else:
            self._fetch_until(idx)
        return self.list[idx]

# Test function for test_valid_case
def test_valid_case():
    lst = LazyList([1, 2, 3, 4])
    
    assert lst[0] == 1
    assert lst[1] == 2
    assert lst[2] == 3
    assert lst[3] == 4
    
    # Test iteration over the lazy list
    iterated_elements = []
    for element in lst:
        iterated_elements.append(element)
    assert iterated_elements == [1, 2, 3, 4]

# Run the test
if __name__ == "__main__":
    pytest.main()
