
import pytest
from unittest.mock import patch
from pathlib import PurePosixPath, PureWindowsPath
from mimesis.providers.path import Path

def test_valid_input_default_platform():
    with patch('sys.platform', 'linux'):  # Mocking to simulate a Linux system
        path_instance = Path()
        assert isinstance(path_instance._pathlib_home, PurePosixPath)

def test_valid_input_specified_platform():
    with patch('sys.platform', 'win32'):  # Mocking to simulate a Windows system
        path_instance = Path(platform='win32')
        assert isinstance(path_instance._pathlib_home, PureWindowsPath)
