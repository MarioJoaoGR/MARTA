
import pytest
from unittest.mock import patch
from mimesis.providers.path import Path, PureWindowsPath, PurePosixPath
import sys


def test_linux_platform():
    with patch('mimesis.providers.path.sys.platform', return_value='linux'):
        path_instance = Path()
        assert isinstance(path_instance._pathlib_home, PurePosixPath)

def test_darwin_platform():
    with patch('mimesis.providers.path.sys.platform', return_value='darwin'):
        path_instance = Path()
        assert isinstance(path_instance._pathlib_home, PurePosixPath)

