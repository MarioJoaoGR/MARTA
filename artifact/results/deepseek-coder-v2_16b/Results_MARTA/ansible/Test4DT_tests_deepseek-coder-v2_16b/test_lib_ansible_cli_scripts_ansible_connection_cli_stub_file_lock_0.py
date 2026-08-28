
import os
import fcntl
import pytest
from contextlib import contextmanager

@contextmanager
def file_lock(lock_path):
    lock_fd = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
    fcntl.lockf(lock_fd, fcntl.LOCK_EX)
    yield
    fcntl.lockf(lock_fd, fcntl.LOCK_UN)
    os.close(lock_fd)

def test_valid_input():
    # Test standard input for file lock functionality with a valid path
    lock_path = 'test_file.lock'
    with file_lock(lock_path):
        assert os.path.exists(lock_path)
    assert not os.path.exists(lock_path)

def test_edge_case():
    # Test edge cases such as None, empty strings, and invalid paths
    lock_path = None
    with pytest.raises(TypeError):
        with file_lock(lock_path):
            pass
    
    lock_path = ''
    with pytest.raises(FileNotFoundError):
        with file_lock(lock_path):
            pass
    
    lock_path = '/invalid/path'
    with pytest.raises(FileNotFoundError):
        with file_lock(lock_path):
            pass

def test_invalid_input():
    # Test handling of invalid inputs that should raise exceptions
    lock_path = 'non_existent_file.lock'
    with pytest.raises(FileNotFoundError):
        with file_lock(lock_path):
            pass
    
    # Create a directory instead of a file to simulate an invalid path scenario
    os.mkdir('invalid_directory')
    lock_path = 'invalid_directory/lock'
    with pytest.raises(IsADirectoryError):
        with file_lock(lock_path):
            pass
