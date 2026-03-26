
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

# Test case for edge case
def test_edge_case():
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Access elements lazily
    assert next(lazy_list) == 1
    assert next(lazy_list) == 2
    
    # Convert the entire list when needed
    full_list = list(lazy_list)
    assert full_list == [1, 2, 3, 4]
    
    # Check len after exhaustion
    with pytest.raises(TypeError):
        len(lazy_list)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___2_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        lazy_list = LazyList([1, 2, 3, 4])
    
        # Access elements lazily
>       assert next(lazy_list) == 1
E       TypeError: 'LazyList' object is not an iterator

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___2_test_edge_case.py:67: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___2_test_edge_case.py::test_edge_case
============================== 1 failed in 0.09s ===============================
"""