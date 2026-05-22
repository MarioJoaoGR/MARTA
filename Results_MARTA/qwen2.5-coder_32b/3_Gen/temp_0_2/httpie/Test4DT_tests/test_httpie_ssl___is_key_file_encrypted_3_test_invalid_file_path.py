
from httpie.ssl_ import _is_key_file_encrypted
from unittest.mock import patch, MagicMock
import pytest

def test_invalid_file_path():
    with patch('httpie.ssl_.open', create=True) as mock_open:
        # Mock the file object to raise an exception when opened
        mock_open.side_effect = FileNotFoundError("File does not exist")
        
        # Call the function with an invalid file path
        with pytest.raises(FileNotFoundError):
            _is_key_file_encrypted('invalid/path/to/keyfile')
