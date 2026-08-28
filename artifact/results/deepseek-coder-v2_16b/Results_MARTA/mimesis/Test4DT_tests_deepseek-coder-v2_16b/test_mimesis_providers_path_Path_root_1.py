
import pytest
from mimesis.providers.path import Path
from pathlib import PurePosixPath, PureWindowsPath
import sys


def test_specified_platform_win32():
    path_instance = Path(platform='win32')
    assert isinstance(path_instance._pathlib_home, PureWindowsPath), "Platform 'win32' should use PureWindowsPath."

def test_specified_platform_linux():
    path_instance = Path(platform='linux')
    assert isinstance(path_instance._pathlib_home, PurePosixPath), "Platform 'linux' should use PurePosixPath."
