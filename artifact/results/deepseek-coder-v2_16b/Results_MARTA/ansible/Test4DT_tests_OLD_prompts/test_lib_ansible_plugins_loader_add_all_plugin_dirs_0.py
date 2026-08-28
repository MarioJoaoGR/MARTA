
import os
from unittest.mock import patch
import pytest
from lib.ansible.plugins.loader import add_all_plugin_dirs

def test_valid_input():
    temp_dir = 'temp_dir'
    with patch('os.makedirs', side_effect=FileExistsError):
        with pytest.raises(FileExistsError):
            os.makedirs(temp_dir)
