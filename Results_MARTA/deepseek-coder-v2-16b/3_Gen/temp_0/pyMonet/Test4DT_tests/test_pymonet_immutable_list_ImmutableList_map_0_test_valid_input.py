
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_input():
    empty_list = ImmutableList()
    list_with_one_element = ImmutableList(head=1)
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    
    # Test map function with a lambda function that doubles the value of each element
    mapped_list = list_with_multiple_elements.map(lambda x: x * 2)
    assert mapped_list.head == 2  # Output will be 2 (1 * 2)
    assert mapped_list.tail.head == 4  # Output will be 4 (2 * 2)
    
    # Test map function with a lambda function that adds 1 to each element
    mapped_list = list_with_multiple_elements.map(lambda x: x + 1)
    assert mapped_list.head == 2  # Output will be 2 (1 + 1)
    assert mapped_list.tail.head == 3  # Output will be 3 (2 + 1)
