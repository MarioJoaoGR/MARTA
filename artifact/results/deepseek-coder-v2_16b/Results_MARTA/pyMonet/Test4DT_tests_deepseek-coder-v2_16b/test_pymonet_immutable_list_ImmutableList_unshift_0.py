
import pytest
from pymonet.immutable_list import ImmutableList

# Test adding an element to an empty list
def test_unshift_empty_list():
    my_list = ImmutableList(is_empty=True)
    new_list = my_list.unshift(1)
    assert not new_list.is_empty
    assert new_list.head == 1
    assert isinstance(new_list.tail, ImmutableList) and new_list.tail.is_empty

# Test adding an element to a non-empty list
def test_unshift_non_empty_list():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    my_list = ImmutableList(head=1, tail=sub_list)
    new_list = my_list.unshift(0)
    assert not new_list.is_empty
    assert new_list.head == 0
    assert new_list.tail.head == 1
    assert new_list.tail.tail.head == 2
    assert isinstance(new_list.tail.tail.tail, ImmutableList) and new_list.tail.tail.tail.head == 3

# Test adding an element to a list where the type can be inferred from the context
def test_unshift_inferred_type():
    my_list = ImmutableList(is_empty=True)
    new_list = my_list.unshift(1)  # Assuming T is int, so 1 is added to an empty list.
    assert not new_list.is_empty
    assert new_list.head == 1
    assert isinstance(new_list.tail, ImmutableList) and new_list.tail.is_empty
