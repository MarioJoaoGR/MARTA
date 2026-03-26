# Module: pymonet.immutable_list
# Import the function using its provided module name
from pymonet.immutable_list import ImmutableList
import pytest

# Test creating an empty ImmutableList instance
def test_create_empty_immutable_list():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty is True

# Test initializing a list with one element
def test_initialize_with_one_element():
    list_with_one_element = ImmutableList(head=1)
    assert list_with_one_element.head == 1
    assert list_with_one_element.is_empty is False

# Test initializing a list with multiple elements
def test_initialize_with_multiple_elements():
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    assert list_with_multiple_elements.head == 1
    assert list_with_multiple_elements.tail.head == 2
    assert list_with_multiple_elements.is_empty is False

# Test converting the immutable list to a Python built-in list
def test_convert_to_list():
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    assert list_with_multiple_elements.to_list() == [1, 2]

# Test appending an element to the end of the list
def test_append_element():
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    new_list = list_with_multiple_elements.append(3)
    assert new_list.to_list() == [1, 2, 3]

# Test prepending an element to the beginning of the list
def test_prepend_element():
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    new_list = list_with_multiple_elements.unshift(0)
    assert new_list.to_list() == [0, 1, 2]

# Test mapping a function over the list
def test_map_function():
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    mapped_list = list_with_multiple_elements.map(lambda x: x * 2)
    assert mapped_list.to_list() == [2, 4]

# Test filtering the list based on a condition
def test_filter_function():
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    filtered_list = list_with_multiple_elements.filter(lambda x: x > 1)
    assert filtered_list.to_list() == [2]

# Test finding an element in the list that satisfies a condition
def test_find_element():
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    result = list_with_multiple_elements.find(lambda x: x == 2)
    assert result == 2

# Test reducing the list to a single value using a reducer function
def test_reduce_function():
    def add(x, y): return x + y
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    reduced_value = list_with_multiple_elements.reduce(add, 0)
    assert reduced_value == 3
