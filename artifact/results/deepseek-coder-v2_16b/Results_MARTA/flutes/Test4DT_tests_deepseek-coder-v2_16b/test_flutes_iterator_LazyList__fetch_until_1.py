
import pytest
from flutes.iterator import LazyList

def test_lazy_list_creation():
    lazy_list = LazyList([1, 2, 3, 4])
    assert list(lazy_list) == [1, 2, 3, 4]

def test_access_by_index():
    lazy_list = LazyList([1, 2, 3, 4])
    assert lazy_list[0] == 1

def test_fetch_until():
    lazy_list = LazyList([1, 2, 3, 4])
    lazy_list._fetch_until(2)
    assert lazy_list[2] == 3
