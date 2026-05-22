
import sys
from unittest import mock
from httpie.manager.compat import run_pip, _run_pip_subprocess, _discover_system_pip

def test_empty_list_input():
    with mock.patch('httpie.manager.compat._discover_system_pip', return_value='pip'):
        with mock.patch('sys.executable', 'python'):
            result = run_pip([])
            assert result is not None
