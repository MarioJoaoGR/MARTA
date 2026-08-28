
import pytest
from unittest.mock import patch
from pathlib import PurePosixPath, PureWindowsPath
from mimesis.providers.path import Path

def test_valid_input_linux():
    with patch('sys.platform', 'linux'):
        path_instance = Path(platform='linux')
        assert isinstance(path_instance._pathlib_home, PurePosixPath)

def test_valid_input_win32():
    with patch('sys.platform', 'win32'):
        path_instance = Path(platform='win32')
        assert isinstance(path_instance._pathlib_home, PureWindowsPath)

def test_invalid_input_error_handling():
    try:
        path_instance = Path(platform='unknown')
    except KeyError as e:
        assert str(e) == "'unknown'"
