
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

def test_none_input():
    lazy_list = LazyList(None)
    with pytest.raises(TypeError):
        len(lazy_list)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
>       lazy_list = LazyList(None)

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___0_test_none_input.py:59: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Test4DT_tests.test_flutes_iterator_LazyList___len___0_test_none_input.LazyList object at 0x7f9ebe361650>
iterable = None

    def __init__(self, iterable: Iterable[T]):
>       self.iter = iter(iterable)
E       TypeError: 'NoneType' object is not iterable

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___0_test_none_input.py:48: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___0_test_none_input.py::test_none_input
============================== 1 failed in 0.07s ===============================
"""