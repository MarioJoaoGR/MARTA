
import pytest
from typing import Iterable, List, Optional, TypeVar
import weakref

T = TypeVar('T')

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
    
    def __getitem__(self, idx: int) -> T:
        if idx < 0 or len(self.list) <= idx:
            self._fetch_until(idx)
        return self.list[idx]

# Test function for test_valid_case
def test_valid_case():
    lst = LazyList([1, 2, 3, 4])
    assert list(lst) == [1, 2, 3, 4]
    assert lst[0] == 1
    assert lst[2] == 3
    with pytest.raises(IndexError):
        lst[-1]  # This should raise an IndexError since the list is not populated yet for negative index

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        lst = LazyList([1, 2, 3, 4])
        assert list(lst) == [1, 2, 3, 4]
        assert lst[0] == 1
        assert lst[2] == 3
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_0_test_valid_case.py:69: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.03s ===============================

"""