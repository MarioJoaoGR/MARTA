
import pytest
import os
import fcntl
from ansible.cli.scripts.ansible_connection_cli_stub import file_lock

def test_valid_input():
    lock_path = 'test.lock'
    with file_lock(lock_path):
        assert os.path.exists(lock_path), "Lock file should be created"
        assert os.path.isfile(lock_path), "Lock file should be a regular file"

def test_invalid_input():
    lock_path = 'nonexistent_directory/test.lock'
    with pytest.raises(FileNotFoundError):
        with file_lock(lock_path):
            pass
