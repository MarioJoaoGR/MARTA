# Module: pymonet.immutable_list
import pytest
from pymonet.immutable_list import ImmutableList

# Test cases for the reduce method in ImmutableList class
def test_reduce_empty_list():
    immutable_list = ImmutableList()
    def add(x, y): return x + y
    assert immutable_list.reduce(add, 0) == 0

def test_reduce_single_element():
    immutable_list = ImmutableList(head=1)
    def add(x, y): return x + y
    assert immutable_list.reduce(add, 0) == 1

def test_reduce_multiple_elements():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    def add(x, y): return x + y
    assert immutable_list.reduce(add, 0) == 6  # 0 + 1 + 2 + 3

def test_reduce_with_function():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    def multiply(x, y): return x * y
    assert immutable_list.reduce(multiply, 1) == 6  # 1 * 1 * 2 * 3

def test_reduce_with_different_accumulator():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    def add(x, y): return x + y
    assert immutable_list.reduce(add, 5) == 11  # 5 + 1 + 2 + 3
