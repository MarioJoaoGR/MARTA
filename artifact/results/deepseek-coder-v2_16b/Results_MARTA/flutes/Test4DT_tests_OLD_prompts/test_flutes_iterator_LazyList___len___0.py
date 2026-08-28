
import pytest
from flutes.iterator import LazyList

def test_lazy_list_iteration():
    lazy_list = LazyList([1, 2, 3, 4])
    iterated_elements = [item for item in lazy_list]
    assert iterated_elements == [1, 2, 3, 4]

def test_lazy_list_access_by_index():
    lazy_list = LazyList([1, 2, 3, 4])
    with pytest.raises(IndexError):
        print(lazy_list[5])  # This should raise an IndexError as the iterable is not fully fetched yet.

def test_lazy_list_len_after_exhaustion():
    lazy_list = LazyList([1, 2, 3, 4])
    for _ in lazy_list:
        pass
    assert len(lazy_list) == 4
