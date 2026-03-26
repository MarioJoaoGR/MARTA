
import os
from pathlib import Path
from unittest.mock import patch, DEFAULT
from isort.place import _src_path_is_module

def test_valid_input():
    src_path = Path(os.getcwd() + '/test_directory')
    os.makedirs(src_path, exist_ok=True)
    
    with patch('isort.place._src_path_is_module', return_value=True):
        assert _src_path_is_module(src_path, 'test_directory') is True
