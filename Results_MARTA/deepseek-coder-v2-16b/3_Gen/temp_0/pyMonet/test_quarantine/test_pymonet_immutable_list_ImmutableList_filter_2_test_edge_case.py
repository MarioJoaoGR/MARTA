
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_case():
    # Test case 1: Filtering an empty list should return an empty list
    empty_list = ImmutableList()
    filtered_empty_list = empty_list.filter(lambda x: x > 0)
    
    assert isinstance(filtered_empty_list, ImmutableList)
    assert filtered_empty_list.is_empty is True

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_filter_2_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Test case 1: Filtering an empty list should return an empty list
        empty_list = ImmutableList()
>       filtered_empty_list = empty_list.filter(lambda x: x > 0)

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_filter_2_test_edge_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/immutable_list.py:122: in filter
    if fn(self.head):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = None

>   filtered_empty_list = empty_list.filter(lambda x: x > 0)
E   TypeError: '>' not supported between instances of 'NoneType' and 'int'

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_filter_2_test_edge_case.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_filter_2_test_edge_case.py::test_edge_case
============================== 1 failed in 0.08s ===============================
"""