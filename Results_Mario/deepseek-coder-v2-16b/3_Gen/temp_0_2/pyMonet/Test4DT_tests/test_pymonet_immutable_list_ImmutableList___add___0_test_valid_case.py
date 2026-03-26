
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_case():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2))
    list2 = ImmutableList(head=3, tail=ImmutableList(head=4))
    
    concatenated_list = list1.__add__(list2)
    
    assert isinstance(concatenated_list, ImmutableList)
    assert concatenated_list.head == 1
    assert isinstance(concatenated_list.tail, ImmutableList)
    assert concatenated_list.tail.head == 2
    assert isinstance(concatenated_list.tail.tail, ImmutableList)
    assert concatenated_list.tail.tail.head == 3
    assert isinstance(concatenated_list.tail.tail.tail, ImmutableList)
    assert concatenated_list.tail.tail.tail.head == 4
