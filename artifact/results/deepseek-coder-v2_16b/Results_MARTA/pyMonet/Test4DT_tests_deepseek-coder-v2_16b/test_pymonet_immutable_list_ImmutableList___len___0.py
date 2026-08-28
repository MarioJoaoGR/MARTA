
import pytest
from pymonet.immutable_list import ImmutableList

# Test valid input where ImmutableList is not empty and has a valid head
def test_valid_input():
    my_list = ImmutableList(head=1)
    assert len(my_list) == 1

# Test edge case where ImmutableList is empty
def test_empty_list():
    my_list = ImmutableList(is_empty=True)
    assert len(my_list) == 0

# Test valid input where ImmutableList has multiple elements
def test_multiple_elements():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    my_list = ImmutableList(head=1, tail=sub_list)
    assert len(my_list) == 3
