
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_case_multiple():
    # Test creating a list with multiple elements
    my_list = ImmutableList.of(1, 2, 3)
    
    assert my_list.head == 1
    assert isinstance(my_list.tail, ImmutableList)
    assert my_list.tail.head == 2
    assert isinstance(my_list.tail.tail, ImmutableList)
    assert my_list.tail.tail.head == 3
    assert not my_list.is_empty
