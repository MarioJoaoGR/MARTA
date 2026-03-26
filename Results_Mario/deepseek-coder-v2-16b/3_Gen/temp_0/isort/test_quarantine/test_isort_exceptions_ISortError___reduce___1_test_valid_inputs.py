
import pytest
from isort.exceptions import ISortError
from functools import partial

def test_valid_inputs():
    error = ISortError()
    reduced = error.__reduce__()
    
    assert isinstance(reduced, tuple)
    assert len(reduced) == 2
    assert reduced[0] is type(error)
    assert not reduced[1]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_exceptions_ISortError___reduce___1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        error = ISortError()
        reduced = error.__reduce__()
    
        assert isinstance(reduced, tuple)
        assert len(reduced) == 2
>       assert reduced[0] is type(error)
E       AssertionError: assert functools.partial(<class 'isort.exceptions.ISortError'>) is <class 'isort.exceptions.ISortError'>
E        +  where <class 'isort.exceptions.ISortError'> = type(ISortError())

isort/Test4DT_tests/test_isort_exceptions_ISortError___reduce___1_test_valid_inputs.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_ISortError___reduce___1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.12s ===============================
"""