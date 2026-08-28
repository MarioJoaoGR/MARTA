
import pytest
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.errors import AnsibleError, AnsibleConnectionFailure

@pytest.fixture(scope="module")
def conn():
    return Connection()

# Test Scenario 1: test_valid_inputs
def test_valid_inputs(conn):
    result = conn.exec_command('ls -l')
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert isinstance(result[0], int)
    assert isinstance(result[1], bytes)
    assert isinstance(result[2], bytes)

# Test Scenario 2: test_edge_cases
def test_edge_cases(conn):
    result = conn.exec_command(None, None, None)
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert isinstance(result[0], int)
    assert isinstance(result[1], bytes)
    assert isinstance(result[2], bytes)

# Test Scenario 3: test_invalid_inputs
def test_invalid_inputs(conn):
    with pytest.raises(TypeError):
        conn.exec_command(123)
    with pytest.raises(AnsibleError):
        conn.exec_command('ls -l', in_data='some data')
