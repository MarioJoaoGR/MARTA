
import pytest
from pymonet.immutable_list import ImmutableList

def test_single_element_init():
    list_with_one_element = ImmutableList(head=1)
    assert list_with_one_element.head == 1
    assert list_with_one_element.tail is None
    assert not list_with_one_element.is_empty
