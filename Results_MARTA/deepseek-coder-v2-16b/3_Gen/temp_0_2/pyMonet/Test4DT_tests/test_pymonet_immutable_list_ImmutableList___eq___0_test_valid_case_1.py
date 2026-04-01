
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_case_1():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))
    list2 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))
    assert list1 == list2
