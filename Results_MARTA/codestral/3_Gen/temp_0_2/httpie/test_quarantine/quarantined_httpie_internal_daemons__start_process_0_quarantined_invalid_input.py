
import pytest
from httpie.internal.daemons import _start_process
from subprocess import Popen, DEVNULL
from unittest.mock import patch
import sys
import os

# Assuming `is_frozen` and `httpie.__main__.__file__` are defined elsewhere in the codebase
# You may need to adjust these imports based on your actual module structure

def test_invalid_input():
    with pytest.raises(FileNotFoundError):
        with patch('sys.executable', new='invalid'):
            _start_process(['invalid', 'command'], close_fds=True, stdout=DEVNULL, stderr=DEVNULL)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_internal_daemons__start_process_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(FileNotFoundError):
            with patch('sys.executable', new='invalid'):
>               _start_process(['invalid', 'command'], close_fds=True, stdout=DEVNULL, stderr=DEVNULL)

httpie/Test4DT_tests_codestral/test_httpie_internal_daemons__start_process_0_test_invalid_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cmd = ['invalid', 'command']
kwargs = {'close_fds': True, 'stderr': -3, 'stdout': -3}
prefix = ['invalid', '/projects/F202407648IACDCF2/mario/httpie/httpie/__main__.py']
main_entrypoint = '/projects/F202407648IACDCF2/mario/httpie/httpie/__main__.py'

    def _start_process(cmd: List[str], **kwargs) -> Popen:
        prefix = [sys.executable]
        # If it is frozen, sys.executable points to the binary (http).
        # Otherwise it points to the python interpreter.
        if not is_frozen:
            main_entrypoint = httpie.__main__.__file__
            prefix += [main_entrypoint]
>       return Popen(prefix + cmd, close_fds=True, shell=False, stdout=DEVNULL, stderr=DEVNULL, **kwargs)
E       TypeError: subprocess.Popen() got multiple values for keyword argument 'close_fds'

httpie/httpie/internal/daemons.py:29: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_internal_daemons__start_process_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""