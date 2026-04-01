
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_input():
    multiple_elements_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    filtered_list = multiple_elements_list.filter(lambda x: x > 1)
    
    assert filtered_list.head == 2
    assert isinstance(filtered_list.tail, ImmutableList)
    assert filtered_list.tail.head == 3
    assert filtered_list.tail.is_empty is False
