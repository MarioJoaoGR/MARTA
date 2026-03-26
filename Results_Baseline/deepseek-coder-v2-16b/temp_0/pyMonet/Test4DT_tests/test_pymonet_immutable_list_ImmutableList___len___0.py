# Module: pymonet.immutable_list
import pytest
from pymonet.immutable_list import ImmutableList

# Test cases for the __len__ method of ImmutableList class
def test_empty_list_length():
    empty_list = ImmutableList()
    assert len(empty_list) == 0, "Expected length of an empty list to be 0"

def test_single_element_list_length():
    single_element_list = ImmutableList(head=1)
    assert len(single_element_list) == 1, "Expected length of a list with one element to be 1"

def test_multiple_elements_list_length():
    multi_element_list = ImmutableList(head=1, tail=ImmutableList(head=2))
    assert len(multi_element_list) == 2, "Expected length of a list with multiple elements to be 2"

def test_len_after_append():
    original_list = ImmutableList(head=1, tail=ImmutableList(head=2))
    new_list = original_list.append(3)
    assert len(new_list) == 3, "Expected length of the list after appending an element to be 3"

def test_len_after_unshift():
    original_list = ImmutableList(head=1, tail=ImmutableList(head=2))
    new_list = original_list.unshift(0)
    assert len(new_list) == 3, "Expected length of the list after unshifting an element to be 3"

def test_len_after_mapping():
    original_list = ImmutableList(head=1, tail=ImmutableList(head=2))
    mapped_list = original_list.map(lambda x: x * 2)
    assert len(mapped_list) == 2, "Expected length of the list after mapping to remain unchanged"

def test_len_after_filtering():
    original_list = ImmutableList(head=1, tail=ImmutableList(head=2))
    filtered_list = original_list.filter(lambda x: x > 1)
    assert len(filtered_list) == 1, "Expected length of the list after filtering to be reduced"

def test_len_after_reducing():
    original_list = ImmutableList(head=1, tail=ImmutableList(head=2))
    reduced_value = original_list.reduce(lambda x, y: x + y, 0)
    assert len(original_list) == 2, "Expected length of the list after reducing to remain unchanged"
