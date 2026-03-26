
import pytest
from unittest.mock import patch
from flutes.log import log_exception

def test():
    with patch('flutes.log.log') as mock_log:
        exc = ValueError('Invalid value')
        user_msg = 'User action required'
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
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_flutes_exception_log_exception_1_test_valid_inputs.py _
ImportError while importing test module '/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_exception_log_exception_1_test_valid_inputs.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
flutes/Test4DT_tests/test_flutes_exception_log_exception_1_test_valid_inputs.py:4: in <module>
    from flutes.log import log_exception
E   ImportError: cannot import name 'log_exception' from 'flutes.log' (/projects/F202407648IACDCF2/mario/flutes/flutes/log.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_exception_log_exception_1_test_valid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.16s ===============================

"""