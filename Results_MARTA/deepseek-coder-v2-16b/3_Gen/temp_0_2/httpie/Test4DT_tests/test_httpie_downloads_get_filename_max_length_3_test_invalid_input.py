
import pytest
from unittest.mock import patch, MagicMock
import os

def get_filename_max_length(directory: str) -> int:
    max_len = 255
    if hasattr(os, 'pathconf') and 'PC_NAME_MAX' in os.pathconf_names:
        max_len = os.pathconf(directory, 'PC_NAME_MAX')
    return max_len

def test_invalid_input():
    with patch('os.pathconf', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            get_filename_max_length('/nonexistent/directory')
