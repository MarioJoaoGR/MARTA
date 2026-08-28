
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.connection.paramiko_ssh import MyAddPolicy, AnsibleError
import sys
from termios import tcflush

# Define the test cases for each scenario

def test_invalid_input():
    with patch('builtins.input', return_value='no'):
        client = MagicMock()
        connection = MagicMock()
        policy = MyAddPolicy(sys.stdin, connection)
        policy._options = {'host_key_checking': True, 'host_key_auto_add': False}
        key = MagicMock()
        key.get_fingerprint.return_value = b'fingerprint'
        key.get_name.return_value = 'ssh-rsa'

        with patch('sys.stdin', new=MagicMock()):
            with pytest.raises(AnsibleError):
                policy.missing_host_key(client, 'example.com', key)

def test_auto_add_enabled():
    client = MagicMock()
    connection = MagicMock()
    policy = MyAddPolicy(sys.stdin, connection)
    policy._options = {'host_key_checking': True, 'host_key_auto_add': True}
    key = MagicMock()
    key.get_fingerprint.return_value = b'fingerprint'
    key.get_name.return_value = 'ssh-rsa'

    policy.missing_host_key(client, 'example.com', key)

    assert True  # Assuming the test should pass if it reaches this point without raising an error