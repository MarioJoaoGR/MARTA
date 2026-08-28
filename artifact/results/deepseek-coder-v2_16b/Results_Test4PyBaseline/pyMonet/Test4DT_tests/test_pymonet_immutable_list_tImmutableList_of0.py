
import pytest
from pymonet.immutable_list import ImmutableList

# Test creating an immutable list with elements [1, 2, 3]
def test_create_immutable_list():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))
    assert immutable_list.head == 1
    assert immutable_list.tail.head == 2
    assert immutable_list.tail.tail.is_empty is True

# Test accessing elements in the list
def test_accessing_elements():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))
    assert immutable_list.head == 1
    assert immutable_list.tail.head == 2
    assert immutable_list.tail.tail.is_empty is True

# Test converting the list to a Python list
def test_to_list():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))