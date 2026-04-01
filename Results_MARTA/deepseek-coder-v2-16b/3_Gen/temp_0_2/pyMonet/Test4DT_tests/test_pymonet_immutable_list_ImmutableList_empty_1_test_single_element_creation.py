
import pytest
from pymonet.immutable_list import ImmutableList

def test_single_element_creation():
    # Test creating an ImmutableList with a single element
    immutable_list = ImmutableList(head=1)
    
    assert isinstance(immutable_list, ImmutableList), "The object is not an instance of ImmutableList"
    assert immutable_list.head == 1, "Head does not match the expected value"
    assert immutable_list.tail is None, "Tail should be None for a single element list"
    assert not immutable_list.is_empty, "List should not be empty"
