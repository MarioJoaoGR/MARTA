
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_input():
    # Setup
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    
    # Test
    assert immutable_list.to_list() == [1, 2, 3]
