
import pytest
from flutes.log import log_exception
import traceback
import subprocess

def test_invalid_inputs():
    with pytest.raises(ValueError):
        raise ValueError("Invalid input")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_flutes_exception_log_exception_0_test_invalid_inputs.py _
ImportError while importing test module '/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_exception_log_exception_0_test_invalid_inputs.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
flutes/Test4DT_tests/test_flutes_exception_log_exception_0_test_invalid_inputs.py:3: in <module>
    from flutes.log import log_exception
E   ImportError: cannot import name 'log_exception' from 'flutes.log' (/projects/F202407648IACDCF2/mario/flutes/flutes/log.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_exception_log_exception_0_test_invalid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.18s ===============================
"""