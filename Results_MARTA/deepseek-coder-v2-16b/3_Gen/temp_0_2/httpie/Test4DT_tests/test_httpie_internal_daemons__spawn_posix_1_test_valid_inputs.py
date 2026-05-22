
import os
import sys
import platform
from contextlib import suppress
from unittest.mock import patch, MagicMock
import pytest

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
    with patch('os.environ.update', MagicMock()):
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
def mock_main():
    with patch('httpie.core.main', MagicMock()):
        yield

@pytest.fixture(autouse=True)
def mock_os_exit():
    with patch('os._exit'):
        yield

@pytest.fixture(autouse=True)
def mock_process_communicate():
    with patch('subprocess.Popen.communicate', return_value=(None, None)):
        yield

def test_valid_inputs():
    from httpie.internal.daemons import _spawn_posix
    process_context = {'VAR': 'value'}
    args = ['http', 'GET', 'https://api.example.com/data']
    _spawn_posix(args, process_context)
