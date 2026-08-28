
import pytest
from pymonet.immutable_list import ImmutableList



def test_unshift_maintains_other_elements():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    initial_list = ImmutableList(head=1, tail=sub_list)
    new_list = initial_list.unshift(0)
    assert new_list.head == 0
    assert new_list.tail.head == 1
    assert new_list.tail.tail.head == 2
    assert new_list.tail.tail.tail.head == 3