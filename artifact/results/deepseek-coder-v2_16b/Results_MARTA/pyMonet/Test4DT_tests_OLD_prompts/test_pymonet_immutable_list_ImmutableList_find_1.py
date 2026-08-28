
import pytest
from pymonet.immutable_list import ImmutableList

def test_find_valid():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    result = lst.find(lambda x: x > 2)
    assert result == 3

def test_find_none():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    result = lst.find(lambda x: x < 0)
    assert result is None

def test_find_empty_list():
    lst = ImmutableList(is_empty=True)
    result = lst.find(lambda x: True)
    assert result is None
