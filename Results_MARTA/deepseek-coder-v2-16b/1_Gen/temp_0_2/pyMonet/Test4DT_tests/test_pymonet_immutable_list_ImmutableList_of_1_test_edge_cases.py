
from pymonet.immutable_list import ImmutableList

def test_list_with_one_element():
    single_element_list = ImmutableList.of(1)
    assert single_element_list.is_empty is False
    assert single_element_list.head == 1
    assert single_element_list.tail is None

def test_list_with_multiple_elements():
    multi_element_list = ImmutableList.of(1, 2, 3)
    assert multi_element_list.is_empty is False
    assert multi_element_list.head == 1
    assert multi_element_list.tail.head == 2
    assert multi_element_list.tail.tail.head == 3
    assert multi_element_list.tail.tail.tail is None
