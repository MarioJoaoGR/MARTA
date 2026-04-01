
import pytest
from typing import Iterable, List
import weakref

class LazyList:
    """A wrapper over an iterable to allow lazily converting it into a list. The iterable is only iterated up to the accessed indices.
    
    Parameters:
        iterable (Iterable): The iterable to wrap.
        
    Example:
        >>> lazy_list = LazyList([1, 2, 3, 4])
        >>> for item in lazy_list:
        ...     print(item)
        ...     if item == 2:
        ...         break
        ... 
        1
        2
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

    def __iter__(self):
        if self.exhausted:
            return iter(self.list)
        return self.LazyListIterator(self)

def test_valid_input():
    lazy_list = LazyList([1, 2, 3, 4])
    expected_output = [1, 2, 3, 4]
    actual_output = []
    
    for item in lazy_list:
        actual_output.append(item)
        if item == 2:
            break
    
    assert actual_output == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList___iter___0_test_valid_input
flutes/Test4DT_tests/test_flutes_iterator_LazyList___iter___0_test_valid_input.py:39:42: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_LazyList___iter___0_test_valid_input.py:42:24: E0602: Undefined variable 'T' (undefined-variable)


"""