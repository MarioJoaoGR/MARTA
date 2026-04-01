
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_case():
    none_comparison = ImmutableList() == None
    assert none_comparison is False, "Expected False because an ImmutableList instance should not be equal to None"
    
    empty_list_comparison = ImmutableList() == ImmutableList()
    assert empty_list_comparison is True, "Expected True because two empty ImmutableList instances are considered equal"
