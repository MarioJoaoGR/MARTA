
# Module: pymonet.immutable_list
from pymonet.immutable_list import ImmutableList

def test_eq_same():
    # Test equality with another instance of ImmutableList that is identical
    list1 = ImmutableList(head=1, tail=[2], is_empty=False)
    list2 = ImmutableList(head=1, tail=[2], is_empty=False)
    assert list1 == list2

def test_eq_different_type():
    # Test equality with a non-ImmutableList object
    list1 = ImmutableList(head=1, tail=[2], is_empty=False)
    assert not list1 == []

def test_eq_different_head():
    # Test equality when heads are different
    list1 = ImmutableList(head=1, tail=[2], is_empty=False)
    list2 = ImmutableList(head=2, tail=[2], is_empty=False)
    assert not list1 == list2

def test_eq_different_tail():
    # Test equality when tails are different
    list1 = ImmutableList(head=1, tail=[2], is_empty=False)
    list2 = ImmutableList(head=1, tail=[3], is_empty=False)
    assert not list1 == list2

def test_eq_different_is_empty():
    # Test equality when is_empty states are different
    list1 = ImmutableList(head=1, tail=[2], is_empty=True)
    list2 = ImmutableList(head=1, tail=[2], is_empty=False)
    assert not list1 == list2

def test_eq_none():
    # Test equality when one of the instances has a None head or tail
    list1 = ImmutableList(head=None, tail=[2], is_empty=False)
    list2 = ImmutableList(head=None, tail=[3], is_empty=False)
    assert not list1 == list2
