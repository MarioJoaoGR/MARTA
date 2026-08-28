
import pytest
from flutes.iterator import LazyList

def test_fetch_until_positive_index():
    lazy_list = LazyList(range(5))
    lazy_list._fetch_until(2)
    assert lazy_list.list == [0, 1, 2]

def test_fetch_until_full_list():
    lazy_list = LazyList(range(5))
    lazy_list._fetch_until(None)
    assert lazy_list.list == [0, 1, 2, 3, 4]


def test_fetch_until_exhausted():
    lazy_list = LazyList(range(5))
    lazy_list._fetch_until(10)  # Index out of range, should exhaust the list
    assert lazy_list.list == [0, 1, 2, 3, 4]

def test_fetch_until_zero_index():
    lazy_list = LazyList(range(5))
    lazy_list._fetch_until(0)
    assert lazy_list.list == [0]