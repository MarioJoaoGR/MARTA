
import pytest
from pymonet.immutable_list import ImmutableList

# Test creating an empty list using __init__ method
def test_create_empty_list():
    my_list = ImmutableList(is_empty=True)
    assert my_list.is_empty is True

# Test creating a non-empty list using __init__ method with head and tail
def test_create_non_empty_list():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    my_list = ImmutableList(head=1, tail=sub_list)
    assert my_list.head == 1
    assert my_list.tail.head == 2
    assert my_list.tail.tail.head == 3

# Test creating an empty list using the class method `empty`
def test_create_empty_list_using_class_method():
    my_list = ImmutableList.empty()
    assert my_list.is_empty is True
