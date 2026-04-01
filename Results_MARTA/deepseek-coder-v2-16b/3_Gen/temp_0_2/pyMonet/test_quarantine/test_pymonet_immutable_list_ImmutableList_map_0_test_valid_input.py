
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_input():
    # Create an empty list
    empty_list = ImmutableList()
    
    # Test map function with a simple identity function (should return the same list)
    mapped_empty_list = empty_list.map(lambda x: x)
    assert isinstance(mapped_empty_list, ImmutableList)
    assert mapped_empty_list.is_empty is True

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_map_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create an empty list
        empty_list = ImmutableList()
    
        # Test map function with a simple identity function (should return the same list)
        mapped_empty_list = empty_list.map(lambda x: x)
        assert isinstance(mapped_empty_list, ImmutableList)
>       assert mapped_empty_list.is_empty is True
E       assert False is True
E        +  where False = <pymonet.immutable_list.ImmutableList object at 0x7f27b0d8c210>.is_empty

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_map_0_test_valid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_map_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.07s ===============================
"""