
import os
from unittest.mock import patch

def get_filename_max_length(directory: str) -> int:
    max_len = 255
    if hasattr(os, 'pathconf') and 'PC_NAME_MAX' in os.pathconf_names:
        try:
            max_len = os.pathconf(directory, 'PC_NAME_MAX')
        except OSError as e:
            print(f"Error querying filename length: {e}")
    return max_len

def test_none_input():
    with patch('os.pathconf', side_effect=OSError("Test error")):
        assert get_filename_max_length(None) == 255
