
# Module: pymonet.immutable_list
import pytest
from pymonet import ImmutableList

# Test creating an empty list
def test_create_empty_list():
    empty_list = ImmutableList()
    assert str(empty_list) == "ImmutableList[]"

# Test creating a list with elements 1, 2, and 3
def test_create_list_with_elements():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    assert str(list1) == "ImmutableList[1, ImmutableList[2, ImmutableList[3, None]]]"

# Test appending an element to the list
def test_append_element():
    empty_list = ImmutableList()
    new_list = empty_list.append(4)
    assert str(new_list) == "ImmutableList[4]"  # This should not change the original list

# Test unshifting an element to the beginning of the list
def test_unshift_element():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    unshift_list = list1.unshift(0)
    assert str(unshift_list) == "ImmutableList[0, 1, ImmutableList[2, ImmutableList[3, None]]]"

# Test mapping a function over the list
def test_map_function():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    def square(x):
        return x * x if x is not None else None
    mapped_list = list1.map(square)
    assert str(mapped_list) == "ImmutableList[1, ImmutableList[4, ImmutableList[9, None]]]"

# Test filtering elements based on a condition
def test_filter_elements():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    filtered_list = list1.filter(lambda x: x <= 1)
    assert str(filtered_list) == "ImmutableList[1]"

# Test finding the first element that satisfies a condition
def test_find_element():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    result = list1.find(lambda x: x > 2)
    assert result == 3

# Test reducing the list to a single value
def test_reduce_list():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    def add(x, y): return x + y
    reduced_value = list1.reduce(add, 0)
    assert reduced_value == 6

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_of_0
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_0.py:4:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""