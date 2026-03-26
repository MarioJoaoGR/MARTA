
import pytest
from pymonet.immutable_list import ImmutableList

# Test creating an empty ImmutableList instance
def test_empty_immutable_list():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty is True

# Test creating a list with one element
def test_immutable_list_with_one_element():
    list_with_one_element = ImmutableList(head=1)
    assert list_with_one_element.head == 1
    assert list_with_one_element.is_empty is False

# Test creating a list with multiple elements
def test_immutable_list_with_multiple_elements():
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    assert list_with_multiple_elements.head == 1
    assert list_with_multiple_elements.tail.head == 2

# Test concatenating two ImmutableList instances
def test_concatenate_immutable_lists():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2))
    list2 = ImmutableList(head=3, tail=ImmutableList(head=4))
    concatenated_list = list1 + list2
    assert concatenated_list.to_list() == [1, 2, 3, 4]

# Test adding an invalid type to ImmutableList (should raise ValueError)
def test_invalid_addition():
    with pytest.raises(ValueError):
        ImmutableList().__add__(None)
