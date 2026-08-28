# Module: ansible.plugins.connection.paramiko_ssh
import pytest
import paramiko
import sys
from unittest.mock import patch

# Module: ansible.plugins.connection.paramiko_ssh

@pytest.fixture
def ssh_client():
    return paramiko.SSHClient()

@pytest.fixture
def myaddpolicy(ssh_client):
    return MyAddPolicy(new_stdin=sys.stdin, connection=ssh_client)

def test_myaddpolicy_init(myaddpolicy):
    assert isinstance(myaddpolicy._new_stdin, type(sys.stdin))
    assert myaddpolicy.connection == sys.stdin
    assert myaddpolicy._options == sys.stdin

@patch('builtins.input', return_value='yes')
def test_myaddpolicy_missing_host_key(mock_input, ssh_client):
    policy = MyAddPolicy(new_stdin=sys.stdin, connection=ssh_client)
    with patch.object(paramiko.SSHClient, 'load_system_host_keys', return_value=None):
        # Assuming load_system_host_keys would be called to check for existing keys
        policy.missing_host_key('hostname')
        assert ssh_client._hostkeys['hostname'] == paramiko.AutoAddPolicy().auto_add('hostname')

if __name__ == "__main__":
    pytest.main()
