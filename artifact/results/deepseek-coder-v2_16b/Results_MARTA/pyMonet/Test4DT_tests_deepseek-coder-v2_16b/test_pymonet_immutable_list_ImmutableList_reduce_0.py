
import pytest
from pymonet.immutable_list import ImmutableList

# Test reducing an empty list
def test_reduce_empty_list():
    my_list = ImmutableList(is_empty=True)
    result = my_list.reduce(lambda acc, item: acc + item, 0)
    assert result == 0

# Test reducing a list with one element
def test_reduce_one_element_list():
    my_list = ImmutableList(head=1)
    result = my_list.reduce(lambda acc, item: acc + item, 0)
    assert result == 1

# Test reducing a list with multiple elements
def test_reduce_multiple_elements_list():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    my_list = ImmutableList(head=1, tail=sub_list)
    result = my_list.reduce(lambda acc, item: acc + item, 0)
    assert result == 6

# Test reducing a list with a different accumulator initial value
def test_reduce_with_different_initial_value():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    my_list = ImmutableList(head=1, tail=sub_list)
    result = my_list.reduce(lambda acc, item: acc + item, 10)
    assert result == 16
