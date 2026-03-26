
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_inputs():
    # Test creating an ImmutableList with a single element
    list_with_one_element = ImmutableList.of(1)
    assert list_with_one_element.head == 1
    assert list_with_one_element.tail is None
    assert not list_with_one_element.is_empty

    # Test creating an ImmutableList with multiple elements
    list_with_multiple_elements = ImmutableList.of(1, 2, 3)
    assert list_with_multiple_elements.head == 1
    assert list_with_multiple_elements.tail.head == 2
    assert list_with_multiple_elements.tail.tail.head == 3
    assert not list_with_multiple_elements.is_empty
