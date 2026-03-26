
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_case_empty_list():
    # Arrange
    empty_immutable_list = ImmutableList(is_empty=True)
    
    # Act & Assert
    assert empty_immutable_list.to_list() == []

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_to_list_1_test_edge_case_empty_list.py F [100%]

=================================== FAILURES ===================================
__________________________ test_edge_case_empty_list ___________________________

    def test_edge_case_empty_list():
        # Arrange
        empty_immutable_list = ImmutableList(is_empty=True)
    
        # Act & Assert
>       assert empty_immutable_list.to_list() == []
E       assert [None] == []
E         
E         Left contains one more item: None
E         Use -v to get more diff

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_to_list_1_test_edge_case_empty_list.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_to_list_1_test_edge_case_empty_list.py::test_edge_case_empty_list
============================== 1 failed in 0.08s ===============================
"""