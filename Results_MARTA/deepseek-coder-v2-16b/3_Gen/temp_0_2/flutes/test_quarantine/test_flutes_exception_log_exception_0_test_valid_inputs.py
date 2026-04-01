
from flutes.exception import log_exception
import pytest
from unittest.mock import patch

def test_valid_inputs():
    with patch('flutes.log') as mock_log:
        try:
            1 / 0  # This will raise a ZeroDivisionError
        except Exception as e:
            log_exception(e)
    
        assert mock_log.called
        args, kwargs = mock_log.call_args
        assert "error" in kwargs["level"]

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

flutes/Test4DT_tests/test_flutes_exception_log_exception_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        with patch('flutes.log') as mock_log:
            try:
                1 / 0  # This will raise a ZeroDivisionError
            except Exception as e:
                log_exception(e)
    
>           assert mock_log.called
E           AssertionError: assert False
E            +  where False = <MagicMock name='log' id='139999336057232'>.called

flutes/Test4DT_tests/test_flutes_exception_log_exception_0_test_valid_inputs.py:13: AssertionError
----------------------------- Captured stdout call -----------------------------
[2026-03-24 01:47:52] Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_exception_log_exception_0_test_valid_inputs.py", line 9, in test_valid_inputs
    1 / 0  # This will raise a ZeroDivisionError
    ~~^~~
ZeroDivisionError: division by zero

[2026-03-24 01:47:52] <ZeroDivisionError> division by zero
------------------------------ Captured log call -------------------------------
ERROR    flutes.log:log.py:182 Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_exception_log_exception_0_test_valid_inputs.py", line 9, in test_valid_inputs
    1 / 0  # This will raise a ZeroDivisionError
    ~~^~~
ZeroDivisionError: division by zero

ERROR    flutes.log:log.py:182 <ZeroDivisionError> division by zero
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_exception_log_exception_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================
"""