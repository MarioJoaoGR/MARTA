
# Module: pymonet.immutable_list
import pytest
from pymonet import ImmutableList  # Fixed import statement to match the module name

# Test cases for the empty method
def test_empty_method():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail is None

# Test cases for the reduce method
def test_reduce_method():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    
    def add(x, y): return x + y
    
    assert lst.reduce(add, 0) == 6

# Test cases for the reduce method with an empty list
def test_reduce_empty_list():
    empty_list = ImmutableList()
    
    def add(x, y): return x + y
    
    assert empty_list.reduce(add, 0) == 0

# Test cases for the reduce method with a single element list
def test_reduce_single_element():
    lst = ImmutableList(head=1, tail=None)
    
    def add(x, y): return x + y
    
    assert lst.reduce(add, 0) == 1

# Test cases for the reduce method with a function that modifies the accumulator
def test_reduce_with_modifying_function():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    
    def multiply(x, y): return x * y
    
    assert lst.reduce(multiply, 1) == 6

# Test cases for the reduce method with a function that returns None
def test_reduce_with_none_returning_function():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    
    def return_none(x, y): return None
    
    with pytest.raises(TypeError):
        lst.reduce(return_none, 0)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_reduce_0
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_reduce_0.py:4:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""