
import subprocess
from typing import List
from unittest.mock import patch
from httpie.manager.compat import PipError, _run_pip_subprocess

def test_valid_inputs():
    with patch('httpie.manager.compat._run_pip_subprocess') as mock_run:
        mock_run.return_value = b'output'
        
        result = _run_pip_subprocess(['pip', '--isolated'], ['install', 'somepackage'])
        
        assert isinstance(result, bytes)
        assert mock_run.call_count == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""