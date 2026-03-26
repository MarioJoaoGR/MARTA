
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_input():
    empty_list = ImmutableList()
    new_list = empty_list.unshift(1)
    assert not new_list.is_empty, "The original list should be empty"
    assert new_list.head == 1, "The head of the new list should be 1"
    assert isinstance(new_list.tail, ImmutableList), "The tail of the new list should be an instance of ImmutableList"
    assert new_list.tail.is_empty, "The tail of the new list should be empty"

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_unshift_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        empty_list = ImmutableList()
        new_list = empty_list.unshift(1)
        assert not new_list.is_empty, "The original list should be empty"
        assert new_list.head == 1, "The head of the new list should be 1"
        assert isinstance(new_list.tail, ImmutableList), "The tail of the new list should be an instance of ImmutableList"
>       assert new_list.tail.is_empty, "The tail of the new list should be empty"
E       AssertionError: The tail of the new list should be empty
E       assert False
E        +  where False = <pymonet.immutable_list.ImmutableList object at 0x7f0b46e16150>.is_empty
E        +    where <pymonet.immutable_list.ImmutableList object at 0x7f0b46e16150> = <pymonet.immutable_list.ImmutableList object at 0x7f0b46e16710>.tail

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_unshift_0_test_valid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_unshift_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.07s ===============================
"""