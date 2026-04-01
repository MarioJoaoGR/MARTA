
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_input():
    # Setup
    empty_list = ImmutableList()
    
    # Function call
    new_list = empty_list.unshift(1)
    
    # Assertions
    assert new_list.head == 1
    assert isinstance(new_list.tail, ImmutableList)
    assert new_list.is_empty is False
