
import pytest
from ansible.module_utils.connection import Connection, ConnectionError

# Fixture to create a real instance of Connection for testing
@pytest.fixture(scope="function")
def real_connection():
    return Connection("/path/to/socket")

def test_valid_input(real_connection):
    # Test valid input with a real module instance and command
    result = real_connection.exec_command('ls -l')
    assert isinstance(result, tuple)
    assert len(result) == 3
    code, stdout, stderr = result
    assert isinstance(code, int)
    assert isinstance(stdout, str)
    assert isinstance(stderr, str) and not stderr

def test_none_input():
    # Test handling None input gracefully
    with pytest.raises(ConnectionError):
        exec_command(None, 'invalid_command')

def test_invalid_command(real_connection):
    # Test invalid command to check error handling
    with pytest.raises(ConnectionError):
        real_connection.exec_command('invalid_command')
