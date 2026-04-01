
import pytest
from pymonet.immutable_list import ImmutableList

def test_invalid_creation():
    # Test case 1: Passing both head and tail
    with pytest.raises(TypeError):
        ImmutableList(head=1, tail=ImmutableList())

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_empty_2_test_invalid_creation.py F [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_creation _____________________________

    def test_invalid_creation():
        # Test case 1: Passing both head and tail
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_empty_2_test_invalid_creation.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_empty_2_test_invalid_creation.py::test_invalid_creation
============================== 1 failed in 0.08s ===============================
"""