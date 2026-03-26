
import pytest
from pymonet.immutable_list import ImmutableList

# Test creating an empty list
def test_create_empty_list():
    empty_list = ImmutableList()
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_unshift_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_create_empty_list ____________________________

    def test_create_empty_list():
        empty_list = ImmutableList()
>       assert str(empty_list) == 'ImmutableList(None, None)'
E       AssertionError: assert 'ImmutableList[None]' == 'ImmutableList(None, None)'
E         
E         - ImmutableList(None, None)
E         ?              ^    ^^^^^^^
E         + ImmutableList[None]
E         ?              ^    ^

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_unshift_0.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_unshift_0.py::test_create_empty_list
========================= 1 failed, 1 passed in 0.06s ==========================
"""