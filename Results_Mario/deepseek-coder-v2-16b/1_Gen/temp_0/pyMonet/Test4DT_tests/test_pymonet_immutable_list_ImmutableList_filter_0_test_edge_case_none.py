
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_case_none():
    empty_list = ImmutableList()
    filtered_list = empty_list.filter(lambda x: x is not None)
    assert filtered_list.is_empty == True
