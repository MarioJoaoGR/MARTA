
import pytest
from ansible.plugins.connection.paramiko_ssh import Connection
import paramiko

@pytest.fixture(scope="module")
def connection():
    return Connection()

# Test 1: Default port (22)
def test_valid_input_default_port(connection):
    sock_kwarg = connection._parse_proxy_command()
    assert isinstance(sock_kwarg, dict), "Expected a dictionary for default port"
    assert 'sock' in sock_kwarg, "Expected 'sock' key in the dictionary"
    assert isinstance(sock_kwarg['sock'], paramiko.ProxyCommand), "'sock' should be an instance of paramiko.ProxyCommand"

# Test 2: Custom port
def test_valid_input_custom_port(connection):
    sock_kwarg = connection._parse_proxy_command(port=2299)
    assert isinstance(sock_kwarg, dict), "Expected a dictionary for custom port"
    assert 'sock' in sock_kwarg, "Expected 'sock' key in the dictionary"
    assert isinstance(sock_kwarg['sock'], paramiko.ProxyCommand), "'sock' should be an instance of paramiko.ProxyCommand"

# Test 3: No proxy command found
def test_missing_proxy_command(connection):
    sock_kwarg = connection._parse_proxy_command()
    assert isinstance(sock_kwarg, dict), "Expected a dictionary even if no proxy command is found"
    assert 'sock' not in sock_kwarg, "Expected 'sock' key to be missing when no proxy command is found"
