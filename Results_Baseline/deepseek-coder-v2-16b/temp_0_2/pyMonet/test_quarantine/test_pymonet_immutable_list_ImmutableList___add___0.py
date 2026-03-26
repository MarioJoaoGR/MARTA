
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
    assert list1.is_empty is False
    assert list1.head == 1
    assert list1.tail.head == 2
    assert list1.tail.tail.head == 3
    assert list1.tail.tail.tail is None

# Test adding an element to the end of the list
def test_append_to_list():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    new_list = list1.append(4)
    assert new_list.is_empty is False
    assert new_list.head == 1
    assert new_list.tail.head == 2
    assert new_list.tail.tail.head == 3
    assert new_list.tail.tail.tail.head == 4
    assert new_list.tail.tail.tail.tail is None

# Test adding an element to the beginning of the list
def test_unshift_to_list():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    unshift_list = list1.unshift(0)
    assert unshift_list.is_empty is False
    assert unshift_list.head == 0
    assert unshift_list.tail.head == 1
    assert unshift_list.tail.tail.head == 2
    assert unshift_list.tail.tail.tail.head == 3
    assert unshift_list.tail.tail.tail.tail is None

# Test mapping a function over the list
def test_map_over_list():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    def square(x): return x * x if x is not None else None
    mapped_list = list1.map(square)
    assert mapped_list.is_empty is False
    assert mapped_list.head == 1
    assert mapped_list.tail.head == 4
    assert mapped_list.tail.tail.head == 9
    assert mapped_list.tail.tail.tail is None

# Test filtering elements based on a condition
def test_filter_list():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    filtered_list = list1.filter(lambda x: x <= 1)
    assert filtered_list.is_empty is False
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

# Test adding two lists together
def test_concatenate_lists():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    other_list = ImmutableList(head=4, tail=ImmutableList(head=5))
    concatenated_list = list1 + other_list
    assert concatenated_list.is_empty is False
    assert concatenated_list.head == 1
    assert concatenated_list.tail.head == 2
    assert concatenated_list.tail.tail.head == 3
    assert concatenated_list.tail.tail.tail.head == 4
    assert concatenated_list.tail.tail.tail.tail.head == 5
    assert concatenated_list.tail.tail.tail.tail.tail is None

# Test adding an invalid type to the list (should raise ValueError)
def test_invalid_addition():
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    with pytest.raises(ValueError):
        list1 + 42

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList___add___0
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___0.py:4:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""