
import pytest
from pymonet.immutable_list import ImmutableList

# Test creating an empty list
def test_empty_list():
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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_to_list_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_empty_list ________________________________

    def test_empty_list():
        empty_list = ImmutableList()
>       assert empty_list.to_list() == []
E       assert [None] == []
E         
E         Left contains one more item: None
E         Use -v to get more diff

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_to_list_0.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_to_list_0.py::test_empty_list
========================= 1 failed, 1 passed in 0.05s ==========================
"""