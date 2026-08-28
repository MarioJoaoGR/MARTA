
import pytest
from pymonet.immutable_list import ImmutableList

# Test creating an ImmutableList with a head element and a tail list
def test_create_immutable_list_with_head_and_tail():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))
    assert immutable_list.head == 1
    assert isinstance(immutable_list.tail, ImmutableList)
    assert immutable_list.tail.head == 2
    assert immutable_list.tail.tail.is_empty

# Test concatenating two ImmutableList instances
def test_concatenate_two_immutable_lists():
    immutable_list1 = ImmutableList(head=1)
    immutable_list2 = ImmutableList(head=2, tail=ImmutableList(is_empty=True))
    combined_list = immutable_list1 + immutable_list2
    assert combined_list.head == 1
    assert isinstance(combined_list.tail, ImmutableList)
    assert combined_list.tail.head == 2
    assert combined_list.tail.tail.is_empty

# Test creating an empty ImmutableList
def test_create_empty_immutable_list():
    empty_list = ImmutableList()