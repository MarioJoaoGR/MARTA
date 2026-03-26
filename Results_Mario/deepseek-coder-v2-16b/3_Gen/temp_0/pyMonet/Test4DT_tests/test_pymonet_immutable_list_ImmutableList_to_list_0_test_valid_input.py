
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_input():
    my_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    assert my_list.to_list() == [1, 2, 3]
