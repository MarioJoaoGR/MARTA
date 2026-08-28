
import pytest
from pymonet.immutable_list import ImmutableList

# Test creating an empty list
def test_create_empty_list():
    my_list = ImmutableList(is_empty=True)
    assert my_list.is_empty is True
    assert my_list.head is None
    assert my_list.tail is None

# Test creating a list with one element
def test_create_single_element_list():
    my_list = ImmutableList(head=1)
    assert my_list.is_empty is False
    assert my_list.head == 1
    assert my_list.tail is None

# Test creating a list with multiple elements
def test_create_multiple_element_list():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    my_list = ImmutableList(head=1, tail=sub_list)
    assert my_list.is_empty is False
    assert my_list.head == 1
    assert my_list.tail.head == 2
    assert my_list.tail.tail.head == 3

# Test converting to a Python list
def test_convert_to_python_list():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    my_list = ImmutableList(head=1, tail=sub_list)
    python_list = my_list.to_list()
    assert python_list == [1, 2, 3]

# Test checking equality of two immutable lists
def test_check_equality():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2))
    list2 = ImmutableList(head=1, tail=ImmutableList(head=2))
    are_equal = (list1 == list2)
    assert are_equal is True
