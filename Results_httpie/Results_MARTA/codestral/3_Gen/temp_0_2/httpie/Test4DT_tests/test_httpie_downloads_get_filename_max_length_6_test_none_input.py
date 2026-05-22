
import pytest
from unittest.mock import patch, MagicMock
import os

def get_filename_max_length(directory: str) -> int:
    max_len = 255
    if hasattr(os, 'pathconf') and 'PC_NAME_MAX' in os.pathconf_names:
        max_len = os.pathconf(directory, 'PC_NAME_MAX')
    return max_len

def test_none_input():
    with patch('os.pathconf', side_effect=ValueError("Invalid directory")):
        with pytest.raises(ValueError):
            get_filename_max_length(None)
