
from flutes.iterator import LazyList, Iterable, List
import pytest

def test_lazylist_init_with_iterable():
    lazy_list = LazyList([1, 2, 3, 4])
    assert isinstance(lazy_list, LazyList)
    for item in lazy_list:
        print(item)
        if item == 2:
            break
