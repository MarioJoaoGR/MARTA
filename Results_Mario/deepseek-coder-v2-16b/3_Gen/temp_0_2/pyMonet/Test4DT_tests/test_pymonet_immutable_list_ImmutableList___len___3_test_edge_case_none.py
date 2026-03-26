
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_case_none():
    none_list = ImmutableList(is_empty=True)
    assert len(none_list) == 0
