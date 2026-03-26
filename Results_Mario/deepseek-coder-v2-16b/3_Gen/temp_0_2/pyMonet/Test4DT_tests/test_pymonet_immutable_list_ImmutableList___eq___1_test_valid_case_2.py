
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_case_2():
    # Setup
    empty_list = ImmutableList()
    non_empty_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))
    
    # Test equality with an empty list
    assert empty_list == ImmutableList()
    
    # Test inequality with a non-empty list
    assert not (empty_list == non_empty_list)
