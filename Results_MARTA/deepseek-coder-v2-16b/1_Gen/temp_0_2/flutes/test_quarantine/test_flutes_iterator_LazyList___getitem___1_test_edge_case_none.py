
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

    def __getitem__(self, idx: int) -> T:
        while len(self.list) <= idx and not self.exhausted:
            try:
                item = next(self.iter)
                self.list.append(item)
            except StopIteration:
                self.exhausted = True
                raise IndexError("Index out of range") from None
        if idx >= len(self.list):
            raise IndexError("Index out of range")
        return self.list[idx]
```

Now, let's write a pytest test case for the `LazyList` class to ensure that it handles index errors correctly:

```python
import pytest
from flutes.iterator import LazyList

def test_lazy_list_getitem_index_error():
    lazy_list = LazyList([1, 2, 3, 4])
    
    with pytest.raises(IndexError):
        # This should raise an IndexError because the list has not been exhausted yet and index 5 is out of range
        _ = lazy_list[5]

def test_lazy_list_getitem_valid_index():
    lazy_list = LazyList([1, 2, 3, 4])
    
    assert lazy_list[0] == 1
    assert lazy_list[2] == 3

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList___getitem___1_test_edge_case_none
flutes/Test4DT_tests/test_flutes_iterator_LazyList___getitem___1_test_edge_case_none.py:40:9: E0001: Parsing failed: 'unterminated string literal (detected at line 40) (Test4DT_tests.test_flutes_iterator_LazyList___getitem___1_test_edge_case_none, line 40)' (syntax-error)


"""