
import pytest
from pymonet.maybe import Maybe

def test_edge_cases():
    # Test None value
    maybe_none = Maybe(value=None, is_nothing=False)
    assert maybe_none.is_nothing == False
    assert maybe_none.value is None
    
    # Test empty list
    maybe_empty_list = Maybe(value=[], is_nothing=True)
    assert maybe_empty_list.is_nothing == True
    assert maybe_empty_list.value == []

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_2_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None value
        maybe_none = Maybe(value=None, is_nothing=False)
        assert maybe_none.is_nothing == False
        assert maybe_none.value is None
    
        # Test empty list
        maybe_empty_list = Maybe(value=[], is_nothing=True)
        assert maybe_empty_list.is_nothing == True
>       assert maybe_empty_list.value == []
E       AttributeError: 'Maybe' object has no attribute 'value'

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_2_test_edge_cases.py:14: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_2_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.08s ===============================
"""