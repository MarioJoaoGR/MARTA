
import pytest
from pymonet.immutable_list import ImmutableList

def test_multiple_elements_init():
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    assert list_with_multiple_elements.head == 1
    assert list_with_multiple_elements.tail.head == 2
    assert list_with_multiple_elements.is_empty is False
