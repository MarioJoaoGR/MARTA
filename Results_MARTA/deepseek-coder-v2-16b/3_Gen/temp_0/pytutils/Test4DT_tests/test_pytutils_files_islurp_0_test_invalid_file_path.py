
import pytest
from unittest.mock import patch, mock_open
import sys
from io import StringIO
from pytutils.files import islurp

def test_invalid_file_path():
    # Test with an invalid file path
    with patch('builtins.open', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            list(islurp('nonexistent_file.txt'))
