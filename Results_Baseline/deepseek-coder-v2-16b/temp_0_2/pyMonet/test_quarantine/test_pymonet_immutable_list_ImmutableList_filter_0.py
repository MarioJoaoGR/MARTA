
# Module: pymonet.immutable_list
# test_immutable_list.py
from pymonet import ImmutableList
import pytest

@pytest.fixture
def empty_list():
    return ImmutableList()

@pytest.fixture
def list1():
    return ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))

def test_empty_list_creation(empty_list):
    assert str(empty_list) == "ImmutableList{}"

def test_filter_elements(list1):
    filtered_list = list1.filter(lambda x: x <= 1)
    assert str(filtered_list) == "ImmutableList(1, None)"

def test_map_function(list1):
    def square(x):
        return x * x if x is not None else None
    
    mapped_list = list1.map(square)
    assert str(mapped_list) == "ImmutableList(1, ImmutableList(4, ImmutableList(9, None)))"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_filter_0
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_filter_0.py:4:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""