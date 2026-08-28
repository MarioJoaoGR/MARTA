
import pytest
from pymonet.immutable_list import ImmutableList

# Test cases for ImmutableList class
def test_create_empty_list():
    empty_list = ImmutableList(is_empty=True)
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail is None

def test_create_non_empty_list():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))
    assert immutable_list.head == 1
    assert immutable_list.tail.head == 2
    assert immutable_list.tail.tail.is_empty is True

def test_add_element_to_list():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))
    new_immutable_list = immutable_list.unshift(0)
    assert new_immutable_list.head == 0
    assert new_immutable_list.tail.head == 1
    assert new_immutable_list.tail.tail.head == 2
    assert new_immutable_list.tail.tail.tail.is_empty is True

def test_add_element_to_empty_list():
    empty_list = ImmutableList(is_empty=True)
    new_empty_list = empty_list.unshift(1)
    assert new_empty_list.head == 1