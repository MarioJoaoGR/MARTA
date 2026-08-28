
import pytest
from pymonet.immutable_list import ImmutableList


def test_create_single_element_list():
    my_list = ImmutableList(head=1)
    assert my_list.to_list() == [1]

def test_create_multiple_elements_list():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    my_list = ImmutableList(head=1, tail=sub_list)
    assert my_list.to_list() == [1, 2, 3]

def test_compare_equal_lists():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2))
    list2 = ImmutableList(head=1, tail=ImmutableList(head=2))
    assert list1 == list2

def test_compare_unequal_lists():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2))
    list2 = ImmutableList(head=1, tail=ImmutableList(head=3))
    with pytest.raises(AssertionError):
        assert list1 == list2