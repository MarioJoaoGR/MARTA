
import pytest
from pymonet.maybe import Maybe

def test_edge_case():
    none_maybe = Maybe(value=None, is_nothing=True)
    empty_maybe = Maybe(value=[], is_nothing=False)
    
    assert none_maybe.is_nothing == True
    assert none_maybe.value is None
    
    assert empty_maybe.is_nothing == False
    assert empty_maybe.value == []

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_just_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        none_maybe = Maybe(value=None, is_nothing=True)
        empty_maybe = Maybe(value=[], is_nothing=False)
    
        assert none_maybe.is_nothing == True
>       assert none_maybe.value is None
E       AttributeError: 'Maybe' object has no attribute 'value'

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_just_1_test_edge_case.py:10: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_just_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.06s ===============================
"""