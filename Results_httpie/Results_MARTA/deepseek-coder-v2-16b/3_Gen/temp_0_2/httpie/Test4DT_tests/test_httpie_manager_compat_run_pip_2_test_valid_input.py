
import subprocess
import sys
from unittest import mock
from httpie.manager.compat import run_pip, _discover_system_pip, _run_pip_subprocess

def test_valid_input():
    with mock.patch('httpie.manager.compat._discover_system_pip', return_value='mocked_pip'):
        with mock.patch('sys.executable', 'python3'):
            args = ['install', 'numpy']
            result = run_pip(args)
            assert isinstance(result, bytes)
