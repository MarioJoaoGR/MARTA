
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_inputs():
    # Test mapping over an empty list
    empty_list = ImmutableList()
    mapped_empty_list = empty_list.map(lambda x: x + 1 if x is not None else None)
    assert isinstance(mapped_empty_list, ImmutableList)
    assert mapped_empty_list.is_empty

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_map_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test mapping over an empty list
        empty_list = ImmutableList()
        mapped_empty_list = empty_list.map(lambda x: x + 1 if x is not None else None)
        assert isinstance(mapped_empty_list, ImmutableList)
>       assert mapped_empty_list.is_empty
E       assert False
E        +  where False = <pymonet.immutable_list.ImmutableList object at 0x7facd4530490>.is_empty

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_map_1_test_valid_inputs.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_map_1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.09s ===============================
"""