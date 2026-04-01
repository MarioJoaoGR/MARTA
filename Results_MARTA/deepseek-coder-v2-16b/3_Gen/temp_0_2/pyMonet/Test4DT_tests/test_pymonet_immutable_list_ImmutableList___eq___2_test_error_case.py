
from pymonet.immutable_list import ImmutableList

def test_error_case():
    empty_list1 = ImmutableList()
    empty_list2 = ImmutableList()
    
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))
    list2 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))
    
    assert empty_list1 == empty_list2
    assert list1 == list2
