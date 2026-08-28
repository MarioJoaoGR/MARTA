
import pytest
from ansible.module_utils.connection import exec_command
from unittest.mock import MagicMock

# Mocking the Connection class and its methods for testing
class Connection:
    def __init__(self, socket_path):
        self._socket_path = socket_path
    
    def exec_command(self, command):
        if command == 'ls /':
            return 'output of ls /'
        else:
            raise ConnectionError("Command not supported", code=1)

class ConnectionError(Exception):
    def __init__(self, message, code=None):
        self.err = message
        self.code = code

# Mocking the to_text function for testing
def to_text(data, errors='surrogate_then_replace'):
    return data

@pytest.fixture
def valid_module():
    module = MagicMock()
    module._socket_path = "mocked_socket_path"
    return module

@pytest.fixture
def invalid_module():
    return None

def test_exec_command_successful(valid_module):
    command = 'ls /'
    result = exec_command(valid_module, command)
    assert result == (0, 'output of ls /\n', '')

def test_exec_command_invalid_module(invalid_module):
    command = 'ls /'
    with pytest.raises(TypeError) as excinfo:
        exec_command(invalid_module, command)
    assert str(excinfo.value) == "exec_command() missing 1 required positional argument: 'module'"

def test_exec_command_incorrect_module_type():
    with pytest.raises(TypeError) as excinfo:
        exec_command("invalid_module", 'ls /')
    assert str(excinfo.value) == "module is of incorrect type"

def test_exec_command_unsupported_command():
    valid_module = MagicMock()
    valid_module._socket_path = "mocked_socket_path"
    command = 'invalid_command'
    with pytest.raises(ConnectionError) as excinfo:
        exec_command(valid_module, command)
    assert str(excinfo.value.err) == "Command not supported"
    assert excinfo.value.code == 1
