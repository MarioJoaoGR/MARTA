
# Module: pymonet.immutable_list
import pytest
from pymonet import ImmutableList

# Test creating an empty list
def test_create_empty_list():
    empty_list = ImmutableList()
    assert empty_list.is_empty == True
    assert empty_list.head is None
    assert isinstance(empty_list.tail, type(None))

# Test creating a list with elements 1, 2, and 3
def test_create_list_with_elements():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    assert not list1.is_empty
    assert list1.head == 1
    assert list1.tail.head == 2
    assert list1.tail.tail.head == 3
    assert list1.tail.tail.tail is None

# Test creating a list with only one element
def test_create_list_with_one_element():
    single_element_list = ImmutableList(head=42)
    assert not single_element_list.is_empty
    assert single_element_list.head == 42
    assert single_element_list.tail is None

# Test creating a list with multiple elements and checking the properties
def test_create_and_check_properties():
    multi_element_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    assert not multi_element_list.is_empty
    assert multi_element_list.head == 1
    assert multi_element_list.tail.head == 2
    assert multi_element_list.tail.tail.head == 3
    assert multi_element_list.tail.tail.tail is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList___init___0
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___init___0.py:4:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""