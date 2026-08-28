
import pytest
from pymonet.immutable_list import ImmutableList

# Test for creating an empty list
def test_empty_list():
    my_list = ImmutableList(is_empty=True)
    assert my_list.is_empty is True

# Test for creating a list with one element
def test_single_element_list():
    my_list = ImmutableList(head=1)
    assert my_list.head == 1
    assert my_list.tail is None
    assert my_list.is_empty is False

# Test for creating a list with multiple elements
def test_multiple_element_list():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    my_list = ImmutableList(head=1, tail=sub_list)
    assert my_list.head == 1
    assert my_list.tail.head == 2
    assert my_list.tail.tail.head == 3
    assert my_list.tail.tail.tail is None
    assert my_list.is_empty is False
