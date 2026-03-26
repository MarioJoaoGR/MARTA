
import pytest
from unittest.mock import patch, MagicMock
import sys
from pytutils.files import islurp

def test_invalid_file_path():
    with patch('builtins.open', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            list(islurp('nonexistentfile.txt'))
