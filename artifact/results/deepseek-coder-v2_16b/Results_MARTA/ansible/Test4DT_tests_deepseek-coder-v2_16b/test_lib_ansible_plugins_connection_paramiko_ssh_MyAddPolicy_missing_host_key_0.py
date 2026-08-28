
import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
from ansible.errors import AnsibleError
from lib.ansible.plugins.connection.paramiko_ssh import MyAddPolicy

@pytest.fixture
def setup_policy():
    new_stdin = StringIO('no\n')  # Mock stdin with "no" input
    connection = MagicMock()
    client = MagicMock()
    key = MagicMock()
    policy = MyAddPolicy(new_stdin, connection)
    return policy, client, key, connection


def test_missing_host_key_accept(setup_policy):
    policy, client, key, connection = setup_policy
    new_stdin = StringIO('yes\n')  # Mock stdin with "yes" input
    
    with patch('sys.stdin', new_stdin):
        policy.missing_host_key(client, 'example.com', key)
        
    assert key._added_by_ansible_this_time is True