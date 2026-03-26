
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
        # Create a LazyList from an iterable
        lazy_list = LazyList([1, 2, 3, 4])
        
        # Access elements lazily
        print(next(lazy_list))  # Output: 1
        print(next(lazy_list))  # Output: 2
        
        # Convert the entire list when needed
        full_list = list(lazy_list)
        print(full_list)        # Output: [1, 2, 3, 4]
        
    Notes:
        - The iterable is only iterated up to the accessed indices.
        - Accessing elements beyond the length of the iterable will raise an IndexError after the iterable is exhausted.
        - The `__len__` method is not available until the iterable is depleted.
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

def test_error_case():
    lazy_list = LazyList([1, 2, 3])
    
    with pytest.raises(TypeError):
        len(lazy_list)
        
    # Consume the iterator to mark it as exhausted
    for _ in lazy_list:
        pass
    
    assert len(lazy_list) == 3

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList___len___2_test_error_case
flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___2_test_error_case.py:69:13: E1133: Non-iterable value lazy_list is used in an iterating context (not-an-iterable)


"""