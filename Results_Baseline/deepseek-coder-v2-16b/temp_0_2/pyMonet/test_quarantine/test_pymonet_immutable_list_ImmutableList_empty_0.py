
# Module: pymonet.immutable_list
import pytest
from pymonet import ImmutableList  # Corrected import statement

# Test creating an empty ImmutableList instance
def test_create_empty_immutable_list():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail is None

# Test the __init__ method with default values
def test_init_default_values():
    ilist = ImmutableList()
    assert ilist.is_empty is False
    assert ilist.head is None
    assert ilist.tail is None

# Test the __init__ method with provided head and tail
def test_init_with_head_and_tail():
    ilist = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    assert ilist.is_empty is False
    assert ilist.head == 1
    assert ilist.tail.head == 2
    assert ilist.tail.tail.head == 3
    assert ilist.tail.tail.tail is None

# Test the empty method directly on the class
def test_empty_class_method():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_empty_0
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_empty_0.py:4:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""