
import pytest
from unittest.mock import patch
from httpie.ssl_ import _is_key_file_encrypted

def test_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        assert not _is_key_file_encrypted("nonexistent_file.txt")
