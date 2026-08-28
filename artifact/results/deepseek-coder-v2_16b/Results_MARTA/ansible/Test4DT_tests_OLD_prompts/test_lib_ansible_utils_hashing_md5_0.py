
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.hashing import md5 as _md5


def test_nonexistent_file():
    with patch('os.path.exists', return_value=False):  # Mocking os.path.exists to return False for a non-existent file
        assert _md5('nonexistentfile.txt') is None, "Expected None for a non-existent file"

def test_directory_path():
    with patch('os.path.isfile', return_value=False):  # Mocking os.path.isfile to return False for a directory path
        assert _md5('directory/') is None, "Expected None for a directory path"
