
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_case_single():
    # Test creating a list with one element
    my_list = ImmutableList.of(1)
    
    assert my_list.head == 1
    assert my_list.tail is None
    assert not my_list.is_empty
