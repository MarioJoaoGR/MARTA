
import pytest
from pymonet.immutable_list import ImmutableList  # Assuming the module name is pymonet.immutable_list

def test_empty_list():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail is None

def test_list_with_one_element():
    single_element_list = ImmutableList.of(1)
    assert single_element_list.is_empty is False
    assert single_element_list.head == 1
    assert single_element_list.tail.is_empty is True
    assert single_element_list.tail.head is None

def test_list_with_multiple_elements():
    multi_element_list = ImmutableList.of(1, 2, 3)
    assert multi_element_list.is_empty is False
    assert multi_element_list.head == 1
    assert multi_element_list.tail.head == 2
    assert multi_element_list.tail.tail.head == 3
    assert multi_element_list.tail.tail.tail.is_empty is True
    assert multi_element_list.tail.tail.tail.head is None

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
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_list_with_one_element __________________________

    def test_list_with_one_element():
        single_element_list = ImmutableList.of(1)
        assert single_element_list.is_empty is False
        assert single_element_list.head == 1
>       assert single_element_list.tail.is_empty is True
E       AttributeError: 'NoneType' object has no attribute 'is_empty'

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_1_test_edge_cases.py:15: AttributeError
_______________________ test_list_with_multiple_elements _______________________

    def test_list_with_multiple_elements():
        multi_element_list = ImmutableList.of(1, 2, 3)
        assert multi_element_list.is_empty is False
        assert multi_element_list.head == 1
        assert multi_element_list.tail.head == 2
        assert multi_element_list.tail.tail.head == 3
>       assert multi_element_list.tail.tail.tail.is_empty is True
E       AttributeError: 'NoneType' object has no attribute 'is_empty'

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_1_test_edge_cases.py:24: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_1_test_edge_cases.py::test_list_with_one_element
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_1_test_edge_cases.py::test_list_with_multiple_elements
========================= 2 failed, 1 passed in 0.07s ==========================
"""