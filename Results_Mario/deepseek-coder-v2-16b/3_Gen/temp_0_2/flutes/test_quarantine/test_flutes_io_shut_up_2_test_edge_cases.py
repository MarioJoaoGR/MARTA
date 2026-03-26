
import sys
import os
import pytest
from flutes.io import shut_up

def test_shut_up_edge_cases():
    with pytest.raises(TypeError):
        # This should raise a TypeError because the function does not yield anything in its context manager implementation
        with shut_up(stderr=True, stdout=False) as suppressed:
            pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io_shut_up_2_test_edge_cases.py F       [100%]

=================================== FAILURES ===================================
___________________________ test_shut_up_edge_cases ____________________________

    def test_shut_up_edge_cases():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_io_shut_up_2_test_edge_cases.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_shut_up_2_test_edge_cases.py::test_shut_up_edge_cases
============================== 1 failed in 0.10s ===============================
"""