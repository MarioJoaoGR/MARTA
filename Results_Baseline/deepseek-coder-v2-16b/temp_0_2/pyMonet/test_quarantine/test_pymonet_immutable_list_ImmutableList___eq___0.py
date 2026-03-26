
# Module: pymonet.immutable_list
import pytest
from pymonet import ImmutableList

# Test creating an empty list
def test_create_empty_list():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail is None

# Test creating a list with elements
def test_create_list_with_elements():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    assert not list1.is_empty
    assert list1.head == 1
    assert list1.tail.head == 2
    assert list1.tail.tail.head == 3
    assert list1.tail.tail.tail is None

# Test comparing two equal lists
def test_compare_equal_lists():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=None))
    list2 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=None))
    assert list1 == list2

# Test comparing two unequal lists
def test_compare_unequal_lists():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=None))
    list2 = ImmutableList(head=1, tail=ImmutableList(head=3, tail=None))
    assert not (list1 == list2)

# Test appending an element to the list
def test_append_element():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=None))
    new_list = list1.append(3)
    assert not new_list.is_empty
    assert new_list.head == 1
    assert new_list.tail.head == 2
    assert new_list.tail.tail.head == 3
    assert new_list.tail.tail.tail is None

# Test unshifting an element to the beginning of the list
def test_unshift_element():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=None))
    unshift_list = list1.unshift(0)
    assert not unshift_list.is_empty
    assert unshift_list.head == 0
    assert unshift_list.tail.head == 1
    assert unshift_list.tail.tail.head == 2
    assert unshift_list.tail.tail.tail is None

# Test mapping a function over the list
def test_map_function():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    def square(x): return x * x if x is not None else None
    mapped_list = list1.map(square)
    assert not mapped_list.is_empty
    assert mapped_list.head == 1
    assert mapped_list.tail.head == 4
    assert mapped_list.tail.tail.head == 9
    assert mapped_list.tail.tail.tail is None

# Test filtering elements based on a condition
def test_filter_elements():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    filtered_list = list1.filter(lambda x: x <= 1)
    assert not filtered_list.is_empty
    assert filtered_list.head == 1
    assert filtered_list.tail is None

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
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList___eq___0
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___eq___0.py:4:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""