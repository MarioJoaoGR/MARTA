
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_case_none():
    single_element_list = ImmutableList(head=None)
    filtered_list = single_element_list.filter(lambda x: x is not None)
    assert filtered_list.is_empty == True
