
import pytest
from flutes.iterator import LazyList

def test_fetch_until_valid_index():
    lazy_list = LazyList([1, 2, 3, 4, 5])
    lazy_list._fetch_until(2)
    assert lazy_list.list == [1, 2, 3]

def test_fetch_until_negative_index():
    lazy_list = LazyList([1, 2, 3, 4, 5])
    lazy_list._fetch_until(-1)
    assert lazy_list.list == [1, 2, 3, 4, 5]

def test_fetch_until_exhausted_iterable():
    lazy_list = LazyList([1, 2, 3])
    lazy_list._fetch_until(10)  # Attempt to fetch more than available
    assert lazy_list.exhausted is True
