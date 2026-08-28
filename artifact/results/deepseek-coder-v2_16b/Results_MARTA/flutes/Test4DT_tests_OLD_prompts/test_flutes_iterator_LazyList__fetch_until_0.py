
import pytest
from typing import Iterable, List, Optional, Callable, TypeVar
from flutes.iterator import LazyList

T = TypeVar('T')

@pytest.fixture
def lazy_list():
    return LazyList([1, 2, 3, 4])

def test_lazy_list_iteration(lazy_list):
    items = []
    for item in lazy_list:
        items.append(item)
    assert items == [1, 2, 3, 4]

def test_lazy_list_access_by_index(lazy_list):
    assert lazy_list[0] == 1
    lazy_list._fetch_until(2)
    assert lazy_list[2] == 3

def test_lazy_list_fetch_up_to_index():
    lazy_list = LazyList([1, 2, 3, 4])
    lazy_list._fetch_until(2)
    with pytest.raises(IndexError):
        assert lazy_list[5] == 6  # This should raise an IndexError because the list is not fully fetched yet.
