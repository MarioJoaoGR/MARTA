
import pytest
from pymonet.immutable_list import ImmutableList

# Test creating an Immutable List with Elements [1, 2, 3]
def test_create_immutable_list():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    assert immutable_list.to_list() == [1, 2, 3]

# Test accessing elements in the list
def test_access_elements():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    assert immutable_list.head == 1
    assert immutable_list.tail.head == 2
    assert immutable_list.tail.tail.head == 3

# Test mapping a function over the elements
def test_map_function():
    def square(x): return x * x
    new_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3))).map(square)
    assert new_list.to_list() == [1, 4, 9]

# Test filtering the list
def test_filter_function():
    filtered_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3))).filter(lambda x: x > 1)
    assert filtered_list.to_list() == [2, 3]

# Test appending an element to the end of the list
def test_append_element():
    updated_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3))).append(4)
    assert updated_list.to_list() == [1, 2, 3, 4]

# Test adding an element to the beginning of the list
def test_unshift_element():
    new_immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3))).unshift(0)
    assert new_immutable_list.to_list() == [0, 1, 2, 3]

# Test creating an empty Immutable List
def test_create_empty_immutable_list():
    empty_immutable_list = ImmutableList()