
import pytest
from pymonet.immutable_list import ImmutableList

# Test creating an empty ImmutableList instance
def test_empty_instance():
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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_empty_instance ______________________________

    def test_empty_instance():
        empty_list = ImmutableList()
>       assert empty_list.is_empty is True, f"Expected is_empty to be True but got {empty_list.is_empty}"
E       AssertionError: Expected is_empty to be True but got False
E       assert False is True
E        +  where False = <pymonet.immutable_list.ImmutableList object at 0x7f82258c5510>.is_empty

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___0.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___0.py::test_empty_instance
========================= 1 failed, 1 passed in 0.05s ==========================
"""