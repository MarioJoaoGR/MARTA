
from pymonet.immutable_list import ImmutableList

def test_valid_case_multiple_elements():
    # Create a list with multiple elements
    multi_element_list = ImmutableList(head=1, tail=ImmutableList(head=2))
    
    # Check the length of the list
    assert len(multi_element_list) == 2
