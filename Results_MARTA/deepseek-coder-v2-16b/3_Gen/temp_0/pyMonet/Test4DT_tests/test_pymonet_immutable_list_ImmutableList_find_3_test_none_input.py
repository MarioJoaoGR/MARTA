
import pytest
from pymonet.immutable_list import ImmutableList

def test_none_input():
    empty_lst = ImmutableList()
    assert empty_lst.find(lambda x: x is None) is None
