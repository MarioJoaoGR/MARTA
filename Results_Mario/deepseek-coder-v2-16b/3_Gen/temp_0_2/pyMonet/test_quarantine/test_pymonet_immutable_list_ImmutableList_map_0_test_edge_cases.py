
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_cases():
    # Test None as head value
    with pytest.raises(TypeError):
        ImmutableList(head=None)
    
    # Test empty list initialization
    empty_list = ImmutableList()
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail is None
    
    # Test single element list
    single_element_list = ImmutableList(head=1)
    assert single_element_list.is_empty is False
    assert single_element_list.head == 1
    assert single_element_list.tail.is_empty is True
    
    # Test multiple element list
    multi_element_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    assert multi_element_list.is_empty is False
    assert multi_element_list.head == 1
    assert multi_element_list.tail.head == 2
    assert multi_element_list.tail.tail.head == 3
    
    # Test map function with None head value
    def add_one(x):
        return x + 1 if x is not None else None
    
    mapped_list = multi_element_list.map(add_one)
    assert mapped_list.head == 2
    assert mapped_list.tail.head == 3
    assert mapped_list.tail.tail.head == 4
    
    # Test map function with None values in the list
    multi_element_list_with_none = ImmutableList(head=None, tail=ImmutableList(head=2, tail=ImmutableList(head=None)))
    mapped_list_with_none = multi_element_list_with_none.map(add_one)
    assert mapped_list_with_none.head is None
    assert mapped_list_with_none.tail.head == 3
    assert mapped_list_with_none.tail.tail.head is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_map_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None as head value
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_map_0_test_edge_cases.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_map_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.09s ===============================
"""