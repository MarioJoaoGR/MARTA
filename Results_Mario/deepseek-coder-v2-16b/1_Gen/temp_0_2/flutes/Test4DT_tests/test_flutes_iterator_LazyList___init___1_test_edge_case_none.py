
from flutes.iterator import LazyList
import pytest
import weakref

def test_edge_case_none():
    lazy_list = LazyList([])
    assert list(lazy_list) == []
