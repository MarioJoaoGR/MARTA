
import pytest
from pymonet.immutable_list import ImmutableList

# Test creating an ImmutableList with elements [1, 2, 3]
def test_create_immutable_list():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    assert immutable_list.head == 1
    assert immutable_list.tail.head == 2
    assert immutable_list.tail.tail.head == 3

# Test accessing elements in the list
def test_access_elements():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    assert immutable_list.head == 1
    assert immutable_list.tail.head == 2
    assert immutable_list.tail.tail.head == 3

# Test converting to a Python list
def test_to_list():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    assert immutable_list.to_list() == [1, 2, 3]

# Test mapping a function over the elements
def test_map():
    def square(x): return x * x
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    new_list = immutable_list.map(square)
    assert new_list.to_list() == [1, 4, 9]

# Test filtering the list
def test_filter():
    def is_even(x): return x % 2 == 0
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    filtered_list = immutable_list.filter(is_even)