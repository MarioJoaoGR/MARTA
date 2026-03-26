
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_case():
    empty_list = ImmutableList()
    assert len(empty_list) == 0
    
    single_element_list = ImmutableList(head=1)
    assert len(single_element_list) == 1
    
    multi_element_list = ImmutableList(head=1, tail=ImmutableList(head=2))
    assert len(multi_element_list) == 2
