
import pytest
from typing import Iterable, List, TypeVar, Callable, Optional
import weakref

T = TypeVar('T')

class LazyList:
    'A wrapper over an iterable to allow lazily converting it into a list. The iterable is only iterated up to the accessed indices.'
    
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
        self._fetch_until(idx)
        if idx < len(self.list):
            return self.list[idx]
        else:
            raise IndexError("Index out of range")

# Test cases
def test_valid_case():
    lazy_list = LazyList([1, 2, 3, 4])
    assert list(lazy_list) == [1, 2, 3, 4]

def test_edge_case():
    lazy_list = LazyList([])
    with pytest.raises(IndexError):
        lazy_list[0]

def test_error_case():
    lazy_list = LazyList([1, 2, 3, 4])
    with pytest.raises(IndexError):
        lazy_list[10]
