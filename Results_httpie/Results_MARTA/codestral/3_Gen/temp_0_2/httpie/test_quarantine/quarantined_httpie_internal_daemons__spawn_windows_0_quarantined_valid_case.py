
import pytest
from unittest.mock import patch
from httpie.internal.daemons import _spawn_windows
from subprocess import CREATE_NEW_PROCESS_GROUP, CREATE_NO_WINDOW, STARTF_USESHOWWINDOW, STARTUPINFO

def test_valid_case():
    with patch('httpie.internal.daemons._start_process') as mock_start_process:
        cmd = ['cmd', '/c', 'echo', 'Hello, World!']
        process_context = {'PATH': 'C:\\Windows\\System32'}
        
        creationflags = CREATE_NEW_PROCESS_GROUP | CREATE_NO_WINDOW
        startupinfo = STARTUPINFO()
        startupinfo.dwFlags |= STARTF_USESHOWWINDOW
        
        _spawn_windows(cmd, process_context)
        
        mock_start_process.assert_called_with(
            cmd,
            env=process_context,
            creationflags=creationflags,
            startupinfo=startupinfo
        )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests_codestral/test_httpie_internal_daemons__spawn_windows_0_test_valid_case.py _
ImportError while importing test module '/projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_codestral/test_httpie_internal_daemons__spawn_windows_0_test_valid_case.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
httpie/Test4DT_tests_codestral/test_httpie_internal_daemons__spawn_windows_0_test_valid_case.py:5: in <module>
    from subprocess import CREATE_NEW_PROCESS_GROUP, CREATE_NO_WINDOW, STARTF_USESHOWWINDOW, STARTUPINFO
E   ImportError: cannot import name 'CREATE_NEW_PROCESS_GROUP' from 'subprocess' (/usr/local/lib/python3.11/subprocess.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_codestral/test_httpie_internal_daemons__spawn_windows_0_test_valid_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""