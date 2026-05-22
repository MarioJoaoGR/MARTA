
import os
import sys
import platform
from unittest.mock import patch, MagicMock
import pytest
from httpie.core import main as httpie_main

@pytest.fixture(autouse=True)
def mock_os_fork():
    with patch('os.fork', return_value=0):
        yield

@pytest.fixture(autouse=True)
def mock_os_setsid():
    with patch('os.setsid'):
        yield

@pytest.fixture(autouse=True)
def mock_os_environ_update():
    with patch('os.environ.update'):
        yield

@pytest.fixture(autouse=True)
def mock_sys_stdin_close():
    with patch('sys.stdin.close'):
        yield

@pytest.fixture(autouse=True)
def mock_sys_stdout_close():
    with patch('sys.stdout.close'):
        yield

@pytest.fixture(autouse=True)
def mock_sys_stderr_close():
    with patch('sys.stderr.close'):
        yield

@pytest.fixture(autouse=True)
def mock_os_exit():
    with patch('os._exit') as mock_os_exit:
        yield

@pytest.fixture(autouse=True)
def mock_httpie_main():
    with patch('httpie.core.main', return_value=None):
        yield

def test_valid_inputs():
    from httpie.internal.daemons import _spawn_posix
    args = ['arg1', 'arg2']
    process_context = {'VAR': 'value'}
    _spawn_posix(args, process_context)
