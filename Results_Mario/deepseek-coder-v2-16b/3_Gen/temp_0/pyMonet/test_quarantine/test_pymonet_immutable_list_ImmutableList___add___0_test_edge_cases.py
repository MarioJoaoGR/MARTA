
from pymonet.immutable_list import ImmutableList

def test_edge_cases():
    none_list = None
    empty_list = ImmutableList()
    
    # Test adding an empty list to another empty list
    result1 = empty_list + empty_list
    assert result1.is_empty is True, "Expected the result of adding two empty lists to be an empty list"

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        none_list = None
        empty_list = ImmutableList()
    
        # Test adding an empty list to another empty list
        result1 = empty_list + empty_list
>       assert result1.is_empty is True, "Expected the result of adding two empty lists to be an empty list"
E       AssertionError: Expected the result of adding two empty lists to be an empty list
E       assert False is True
E        +  where False = <pymonet.immutable_list.ImmutableList object at 0x7fc7b394bcd0>.is_empty

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___0_test_edge_cases.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.07s ===============================
"""