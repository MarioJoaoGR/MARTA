
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_input():
    empty_list = ImmutableList()
    list_with_one_element = ImmutableList(head=1)
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    
    # Test filtering an empty list
    filtered_empty_list = empty_list.filter(lambda x: x > 1)
    assert filtered_empty_list.is_empty is True
    
    # Test filtering a list with one element
    filtered_one_element_list = list_with_one_element.filter(lambda x: x > 0)
    assert filtered_one_element_list.head == 1
    
    # Test filtering a list with multiple elements
    filtered_multiple_elements_list = list_with_multiple_elements.filter(lambda x: x > 1)
    assert filtered_multiple_elements_list.head == 2

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_filter_2_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        empty_list = ImmutableList()
        list_with_one_element = ImmutableList(head=1)
        list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2))
    
        # Test filtering an empty list
>       filtered_empty_list = empty_list.filter(lambda x: x > 1)

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_filter_2_test_valid_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/immutable_list.py:122: in filter
    if fn(self.head):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = None

>   filtered_empty_list = empty_list.filter(lambda x: x > 1)
E   TypeError: '>' not supported between instances of 'NoneType' and 'int'

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_filter_2_test_valid_input.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_filter_2_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""