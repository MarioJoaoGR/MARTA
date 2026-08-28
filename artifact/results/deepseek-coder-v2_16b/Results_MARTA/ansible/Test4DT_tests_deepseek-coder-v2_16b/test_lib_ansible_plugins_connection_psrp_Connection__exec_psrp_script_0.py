
import pytest
from ansible.plugins.connection.psrp import Connection

# Fixture to create a real instance of Connection for testing
@pytest.fixture
def connection():
    return Connection(remote_addr='127.0.0.1', remote_user='user', remote_password='pass')

# Test valid inputs scenario
def test_valid_inputs(connection):
    script = 'Write-Output "Hello, World!"'
    rc, stdout, stderr = connection._exec_psrp_script(script)
    assert rc == 0
    assert stdout.strip() == 'Hello, World!'
    assert stderr == ''

# Test edge cases scenario
def test_edge_cases(connection):
    script = None
    with pytest.raises(TypeError):
        connection._exec_psrp_script(script)

# Test invalid inputs scenario
def test_invalid_inputs(connection):
    script = 'InvalidScript'
    with pytest.raises(Exception):
        connection._exec_psrp_script(script)
