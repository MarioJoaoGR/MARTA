
import pytest
from pymonet.immutable_list import ImmutableList

# Test creating an immutable list with head, tail, and is_empty attributes
def test_create_immutable_list():
    # Create a simple immutable list with head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True))
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))
    assert immutable_list.head == 1
    assert isinstance(immutable_list.tail, ImmutableList)
    assert immutable_list.tail.head == 2
    assert immutable_list.tail.tail.is_empty

# Test appending an element to the immutable list
def test_append_element():
    # Create a simple immutable list with head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True))
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))
    updated_list = immutable_list.append(3)
    assert updated_list.head == 1
    assert isinstance(updated_list.tail, ImmutableList)
    assert updated_list.tail.head == 2