# Module: pymonet.immutable_list
# test_immutable_list.py
from pymonet.immutable_list import ImmutableList

def test_create_immutable_list():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    assert immutable_list.to_list() == [1, 2, 3]

def test_access_elements():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    assert immutable_list.head == 1
    assert immutable_list.tail.head == 2
    assert immutable_list.tail.tail.head == 3

def test_map_function():
    def square(x): return x * x
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    new_list = immutable_list.map(square)
    assert new_list.to_list() == [1, 4, 9]

def test_filter_list():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    filtered_list = immutable_list.filter(lambda x: x > 1)
    assert filtered_list.to_list() == [2, 3]

def test_append_element():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    updated_list = immutable_list.append(4)
    assert updated_list.to_list() == [1, 2, 3, 4]

def test_unshift_element():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    new_immutable_list = immutable_list.unshift(0)
    assert new_immutable_list.to_list() == [0, 1, 2, 3]

def test_string_representation():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    assert str(immutable_list) == 'ImmutableList[1, 2, 3]'
