
from pymonet.immutable_list import ImmutableList

def test_valid_case_empty():
    # Test creating an empty list
    empty_list = ImmutableList()
    
    # Check if the list is indeed empty
    assert empty_list.is_empty == True

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_0_test_valid_case_empty.py F [100%]

=================================== FAILURES ===================================
____________________________ test_valid_case_empty _____________________________

    def test_valid_case_empty():
        # Test creating an empty list
        empty_list = ImmutableList()
    
        # Check if the list is indeed empty
>       assert empty_list.is_empty == True
E       assert False == True
E        +  where False = <pymonet.immutable_list.ImmutableList object at 0x7f0df030ee90>.is_empty

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_0_test_valid_case_empty.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_0_test_valid_case_empty.py::test_valid_case_empty
============================== 1 failed in 0.08s ===============================
"""