
import pytest
from unittest.mock import patch
from pymonet.immutable_list import ImmutableList

# Scenario 1: Test reduce method with an empty list and a function that adds to the accumulator
def test_valid_case_empty_list():
    my_list = ImmutableList(is_empty=True)
    
    def add_to_acc(acc, item):
        return acc + item
    
    result = my_list.reduce(add_to_acc, 0)
    assert result == 0

# Scenario 2: Test reduce method with a single element list and a function that adds to the accumulator
def test_valid_case_single_element():
    my_list = ImmutableList(head=1)
    
    def add_to_acc(acc, item):
        return acc + item
    
    result = my_list.reduce(add_to_acc, 0)
    assert result == 1

# Scenario 3: Test reduce method with a list of multiple elements and a function that adds to the accumulator
def test_valid_case_multiple_elements():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    my_list = ImmutableList(head=1, tail=sub_list)
    
    def add_to_acc(acc, item):
        return acc + item
    
    result = my_list.reduce(add_to_acc, 0)
    assert result == 6

# Scenario 4: Test reduce method with a None input and a function that adds to the accumulator
def test_edge_case_none():
    my_list = ImmutableList(head=None)
    
    def add_to_acc(acc, item):
        return acc + item
    
    result = my_list.reduce(add_to_acc, 0)
    assert result == 0

# Scenario 5: Test reduce method with an empty list and a function that adds to the accumulator
def test_edge_case_empty():
    my_list = ImmutableList(is_empty=True)
    
    def add_to_acc(acc, item):
        return acc + item
    
    result = my_list.reduce(add_to_acc, 0)
    assert result == 0

# Scenario 6: Test reduce method with an invalid function input and expect a TypeError
def test_error_case_invalid_fn():
    my_list = ImmutableList(head=1, tail=ImmutableList(head=2))
    
    def invalid_fn(acc):  # Invalid function signature
        return acc
    
    with pytest.raises(TypeError):
        my_list.reduce(invalid_fn, 0)
