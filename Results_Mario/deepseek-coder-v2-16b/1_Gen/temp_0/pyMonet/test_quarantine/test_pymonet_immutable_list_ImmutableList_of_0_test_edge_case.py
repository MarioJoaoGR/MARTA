
from pymonet.immutable_list import ImmutableList

def test_edge_case():
    # Test None input
    none_input = ImmutableList(head=None)
    assert none_input.is_empty is True

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Test None input
        none_input = ImmutableList(head=None)
>       assert none_input.is_empty is True
E       assert False is True
E        +  where False = <pymonet.immutable_list.ImmutableList object at 0x7f86e0e36890>.is_empty

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_0_test_edge_case.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.07s ===============================
"""