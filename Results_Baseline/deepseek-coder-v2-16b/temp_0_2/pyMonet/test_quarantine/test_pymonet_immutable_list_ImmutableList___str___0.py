
# Module: pymonet.immutable_list
import pytest
from pymonet import ImmutableList

# Test creating an empty list
def test_create_empty_list():
    empty_list = ImmutableList.empty()
    assert str(empty_list) == 'ImmutableList[]'
    assert empty_list.is_empty is True

# Test creating a list with elements 1, 2, and 3
def test_create_list_with_elements():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    assert str(list1) == 'ImmutableList[1, 2, 3]'
    assert list1.is_empty is False

# Test converting the immutable list to a Python built-in list
def test_to_list():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    assert list1.to_list() == [1, 2, 3]
    
    empty_list = ImmutableList()
    assert empty_list.to_list() == [] if list1.head is None else [list1.head]

# Test appending an element to the immutable list
def test_append():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    new_list = list1.append(4)
    assert str(new_list) == 'ImmutableList[1, 2, 3, 4]'

# Test unshifting an element to the beginning of the immutable list
def test_unshift():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    unshift_list = list1.unshift(0)
    assert str(unshift_list) == 'ImmutableList[0, 1, 2, 3]'

# Test mapping a function over the immutable list
def test_map():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    def square(x): return x * x if x is not None else None
    mapped_list = list1.map(square)
    assert str(mapped_list) == 'ImmutableList[1, 4, 9]'

# Test filtering elements based on a condition
def test_filter():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    filtered_list = list1.filter(lambda x: x <= 1)
    assert str(filtered_list) == 'ImmutableList[1]'

# Test finding the first element that satisfies a condition
def test_find():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    result = list1.find(lambda x: x > 2)
    assert result == 3

# Test reducing the immutable list to a single value
def test_reduce():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    def add(x, y): return x + y
    reduced_value = list1.reduce(add, 0)
    assert reduced_value == 6

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList___str___0
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___str___0.py:4:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""