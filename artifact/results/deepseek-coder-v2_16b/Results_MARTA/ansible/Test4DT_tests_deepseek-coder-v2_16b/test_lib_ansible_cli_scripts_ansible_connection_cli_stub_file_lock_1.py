
import pytest
import os
import fcntl
from ansible.cli.scripts.ansible_connection_cli_stub import file_lock

def test_valid_input():
    lock_path = 'test.lock'
    with file_lock(lock_path):
        assert os.path.exists(lock_path)
