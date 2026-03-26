
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
    head = 1
    tail = ImmutableList(head=2, tail=ImmutableList(head=3, tail=None))
    my_list = ImmutableList(head=head, tail=tail)
    
    assert not my_list.is_empty
    assert my_list.head == head
    assert my_list.tail.head == 2
    assert my_list.tail.tail.head == 3
    assert my_list.tail.tail.tail is None

# Test converting the list to a Python built-in list
def test_convert_to_python_list():
    head = 1
    tail = ImmutableList(head=2, tail=ImmutableList(head=3, tail=None))
    my_list = ImmutableList(head=head, tail=tail)
    
    py_list = my_list.to_list()
    assert py_list == [head] + [t for t in tail.to_list()]

# Test appending an element to the list
def test_append_element():
    head = 1
    tail = ImmutableList(head=2, tail=ImmutableList(head=3, tail=None))
    my_list = ImmutableList(head=head, tail=tail)
    
    new_list = my_list.append(4)
    assert not new_list.is_empty
    assert new_list.to_list() == [head] + [t for t in tail.to_list()] + [4]

# Test unshifting an element to the beginning of the list
def test_unshift_element():
    head = 1
    tail = ImmutableList(head=2, tail=ImmutableList(head=3, tail=None))
    my_list = ImmutableList(head=head, tail=tail)
    
    unshift_list = my_list.unshift(0)
    assert not unshift_list.is_empty
    assert unshift_list.to_list() == [0] + [head] + [t for t in tail.to_list()]

# Test mapping a function over the list
def test_map_function():
    head = 1
    tail = ImmutableList(head=2, tail=ImmutableList(head=3, tail=None))
    my_list = ImmutableList(head=head, tail=tail)
    
    def square(x): return x * x if x is not None else None
    mapped_list = my_list.map(square)
    assert mapped_list.to_list() == [square(head)] + [square(t) for t in tail.to_list()]

# Test filtering elements based on a condition
def test_filter():
    head = 1
    tail = ImmutableList(head=2, tail=ImmutableList(head=3, tail=None))
    my_list = ImmutableList(head=head, tail=tail)
    
    filtered_list = my_list.filter(lambda x: x <= 1)
    assert filtered_list.to_list() == [head] + [t for t in tail.to_list() if t <= 1]

# Test finding the first element that satisfies a condition
def test_find():
    head = 1
    tail = ImmutableList(head=2, tail=ImmutableList(head=3, tail=None))
    my_list = ImmutableList(head=head, tail=tail)
    
    result = my_list.find(lambda x: x > 2)
    assert result == 3

# Test reducing the list to a single value
def test_reduce():
    head = 1
    tail = ImmutableList(head=2, tail=ImmutableList(head=3, tail=None))
    my_list = ImmutableList(head=head, tail=tail)
    
    def add(x, y): return x + y
    reduced_value = my_list.reduce(add, 0)
    assert reduced_value == sum([head] + [t for t in tail.to_list()])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_to_list_0
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_to_list_0.py:4:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""