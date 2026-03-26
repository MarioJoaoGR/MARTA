
# Module: pymonet.immutable_list
import pytest
from pymonet import ImmutableList

# Test case to check the creation of an empty list using the `empty` method
def test_create_empty_list():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty, "Expected is_empty flag to be True for an empty list"
    assert empty_list.head is None, "Expected head to be None for an empty list"
    assert empty_list.tail is None, "Expected tail to be None for an empty list"

# Test case to check the `find` method with a non-empty list and a matching condition
def test_find_method_with_matching_condition():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    result = lst.find(lambda x: x > 2)
    assert result == 3, "Expected to find the element 3 which satisfies the condition"

# Test case to check the `find` method with a non-empty list and no matching condition
def test_find_method_without_matching_condition():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    result = lst.find(lambda x: x > 5)
    assert result is None, "Expected to find no element as none satisfies the condition"

# Test case to check the `find` method with an empty list
def test_find_method_with_empty_list():
    empty_list = ImmutableList(is_empty=True)
    result = empty_list.find(lambda x: x > 0)
    assert result is None, "Expected to find no element as the list is empty"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_find_0
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_find_0.py:4:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""