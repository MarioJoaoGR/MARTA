
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_input():
    my_list = ImmutableList(head=1, tail=None)
    assert len(my_list) == 1

def test_empty_list():
    empty_list = ImmutableList(is_empty=True)
    assert len(empty_list) == 0

def test_multiple_elements():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    my_list = ImmutableList(head=1, tail=sub_list)
    assert len(my_list) == 3
