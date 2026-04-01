
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_input():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=None))
    result = lst.find(lambda x: x > 0)
    assert result == 1
