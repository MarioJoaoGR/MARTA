
# Module: pymonet.immutable_list
# test_immutable_list.py
from pymonet import ImmutableList
import pytest

@pytest.fixture
def empty_list():
    return ImmutableList()

@pytest.fixture
def list_with_elements():
    return ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))

def test_empty_list_creation(empty_list):
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail is None

def test_list_with_elements_creation(list_with_elements):
    assert list_with_elements.is_empty is False
    assert list_with_elements.head == 1
    assert list_with_elements.tail.head == 2
    assert list_with_elements.tail.tail.head == 3
    assert list_with_elements.tail.tail.tail is None

def test_append_to_empty_list(empty_list):
    new_list = empty_list.append(1)
    assert new_list.is_empty is False
    assert new_list.head == 1
    assert new_list.tail is None

def test_append_to_list_with_elements(list_with_elements):
    new_list = list_with_elements.append(4)
    assert new_list.is_empty is False
    assert new_list.head == 1
    assert new_list.tail.head == 2
    assert new_list.tail.tail.head == 3
    assert new_list.tail.tail.tail.head == 4
    assert new_list.tail.tail.tail.tail is None

def test_append_with_none_element(list_with_elements):
    with pytest.raises(TypeError):
        list_with_elements.append(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_append_0
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_append_0.py:4:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""