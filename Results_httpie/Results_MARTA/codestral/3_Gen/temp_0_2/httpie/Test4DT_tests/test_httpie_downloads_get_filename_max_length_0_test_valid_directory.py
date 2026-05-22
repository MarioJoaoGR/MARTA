
import os
from unittest.mock import patch

def get_filename_max_length(directory: str) -> int:
    max_len = 255
    if hasattr(os, 'pathconf') and 'PC_NAME_MAX' in os.pathconf_names:
        max_len = os.pathconf(directory, 'PC_NAME_MAX')
    return max_len

def test_valid_directory():
    with patch('os.pathconf', return_value=255):
        assert get_filename_max_length('/home/user') == 255
