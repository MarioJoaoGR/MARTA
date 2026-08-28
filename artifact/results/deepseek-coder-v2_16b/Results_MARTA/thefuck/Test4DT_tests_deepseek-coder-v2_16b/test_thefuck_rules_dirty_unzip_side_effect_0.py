
import pytest
import zipfile
import os
from unittest.mock import patch
from thefuck.rules.dirty_unzip import side_effect, _zip_file



def test_invalid_inputs():
    old_cmd = None
    command = {'script_parts': ['unzip', '-r', 'archive.zip', '/path/to/extract']}
    
    with patch('thefuck.rules.dirty_unzip.os.remove') as mock_remove:
        with pytest.raises(AttributeError):
            side_effect(old_cmd, command)