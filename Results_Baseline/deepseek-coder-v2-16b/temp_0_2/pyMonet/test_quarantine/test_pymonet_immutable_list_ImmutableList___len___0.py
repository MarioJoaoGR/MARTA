
# Module: pymonet.immutable_list
import pytest
from pymonet import ImmutableList

# Test cases for the empty method
def test_empty_method():
    empty_list = ImmutableList.empty()
    assert isinstance(empty_list, ImmutableList), "Expected an instance of ImmutableList"
    assert empty_list.is_empty is True, "Expected is_empty to be True for an empty list"
    assert empty_list.head is None, "Expected head to be None for an empty list"
    assert empty_list.tail is None, "Expected tail to be None for an empty list"

# Test cases for the __init__ method
def test_init_method():
    # Creating a list with one element
    single_element_list = ImmutableList(head=5)
    assert isinstance(single_element_list, ImmutableList), "Expected an instance of ImmutableList"
    assert single_element_list.is_empty is False, "Expected is_empty to be False for a non-empty list"
    assert single_element_list.head == 5, "Expected head to be 5"
    assert single_element_list.tail is None, "Expected tail to be None for a list with one element"
    
    # Creating a longer list
    long_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    assert isinstance(long_list, ImmutableList), "Expected an instance of ImmutableList"
    assert long_list.is_empty is False, "Expected is_empty to be False for a non-empty list"
    assert long_list.head == 1, "Expected head to be 1"
    assert long_list.tail.head == 2, "Expected tail's head to be 2"
    assert long_list.tail.tail.head == 3, "Expected tail's tail's head to be 3"
    assert long_list.tail.tail.tail is None, "Expected tail's tail's tail to be None"

# Test cases for the __len__ method
def test_len_method():
    empty_list = ImmutableList()
    assert len(empty_list) == 0, "Expected length of an empty list to be 0"
    
    single_element_list = ImmutableList(head=5)
    assert len(single_element_list) == 1, "Expected length of a list with one element to be 1"
    
    long_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    assert len(long_list) == 3, "Expected length of the longer list to be 3"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList___len___0
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___len___0.py:4:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""