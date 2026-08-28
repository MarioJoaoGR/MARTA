
import pytest
from unittest.mock import patch, Mock
from lib.ansible.plugins.connection.paramiko_ssh import Connection
import os

def test_valid_input():
    conn = Connection()
    conn.ssh._host_keys = {'example.com': {'rsa': Mock(get_base64=lambda: 'key123')}}
    with patch('os.path.expanduser', return_value='~/.ssh'):
        result = conn._save_ssh_host_keys('~/.ssh/known_hosts')
        assert result is True

def test_none_input():
    conn = Connection()
    result = conn._save_ssh_host_keys(None)
    assert result is False

def test_invalid_input():
    conn = Connection()
    with patch('os.path.expanduser', return_value='~/.ssh'):
        result = conn._save_ssh_host_keys('invalid/path')
        assert result is False
