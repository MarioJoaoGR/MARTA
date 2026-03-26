
import pytest
from pymonet.immutable_list import ImmutableList

def test_empty():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail is None

def test_of_one_element():
    single_element_list = ImmutableList.of(1)
    assert single_element_list.is_empty is False
    assert single_element_list.head == 1
    assert single_element_list.tail.is_empty is True

def test_of_multiple_elements():
    multiple_element_list = ImmutableList.of(1, 2, 3)
    assert multiple_element_list.is_empty is False
    assert multiple_element_list.head == 1
    assert multiple_element_list.tail.head == 2
    assert multiple_element_list.tail.tail.head == 3

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_1_test_edge_cases.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_of_one_element ______________________________

    def test_of_one_element():
        single_element_list = ImmutableList.of(1)
        assert single_element_list.is_empty is False
        assert single_element_list.head == 1
>       assert single_element_list.tail.is_empty is True
E       AttributeError: 'NoneType' object has no attribute 'is_empty'

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_1_test_edge_cases.py:15: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_1_test_edge_cases.py::test_of_one_element
========================= 1 failed, 2 passed in 0.09s ==========================
"""