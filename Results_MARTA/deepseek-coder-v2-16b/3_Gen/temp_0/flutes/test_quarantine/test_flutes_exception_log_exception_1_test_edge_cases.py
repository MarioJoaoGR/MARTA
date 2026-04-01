
import pytest
from unittest.mock import patch
from flutes.log import log
from flutes.exception import log_exception
import traceback
import subprocess

def test():
    with patch('flutes.log.log') as mock_log:
        exc = ValueError('Invalid value')
        user_msg = None
        log_exception(exc, user_msg=user_msg)
        assert mock_log.called

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_exception_log_exception_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_____________________________________ test _____________________________________

    def test():
        with patch('flutes.log.log') as mock_log:
            exc = ValueError('Invalid value')
            user_msg = None
            log_exception(exc, user_msg=user_msg)
>           assert mock_log.called
E           AssertionError: assert False
E            +  where False = <MagicMock name='log' id='139648492826960'>.called

flutes/Test4DT_tests/test_flutes_exception_log_exception_1_test_edge_cases.py:14: AssertionError
----------------------------- Captured stdout call -----------------------------
[2026-03-19 19:48:48] NoneType: None

[2026-03-19 19:48:48] <ValueError> Invalid value
------------------------------ Captured log call -------------------------------
ERROR    flutes.log:log.py:182 NoneType: None

ERROR    flutes.log:log.py:182 <ValueError> Invalid value
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_exception_log_exception_1_test_edge_cases.py::test
============================== 1 failed in 0.09s ===============================

"""