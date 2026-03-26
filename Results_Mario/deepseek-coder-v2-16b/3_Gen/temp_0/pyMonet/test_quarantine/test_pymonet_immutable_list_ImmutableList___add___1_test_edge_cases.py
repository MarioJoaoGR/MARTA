
from pymonet.immutable_list import ImmutableList

def test_edge_cases():
    none_list = ImmutableList(is_empty=True)
    empty_list = ImmutableList()
    empty_list_with_head = ImmutableList(head=None)
    
    assert none_list.is_empty is True
    assert empty_list.is_empty is True
    assert empty_list_with_head.is_empty is False

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        none_list = ImmutableList(is_empty=True)
        empty_list = ImmutableList()
        empty_list_with_head = ImmutableList(head=None)
    
        assert none_list.is_empty is True
>       assert empty_list.is_empty is True
E       assert False is True
E        +  where False = <pymonet.immutable_list.ImmutableList object at 0x7f91bb1afa90>.is_empty

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___1_test_edge_cases.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.08s ===============================
"""