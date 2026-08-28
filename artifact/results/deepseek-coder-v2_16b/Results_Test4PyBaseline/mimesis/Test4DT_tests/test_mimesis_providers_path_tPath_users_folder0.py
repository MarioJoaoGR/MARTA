
import pytest
from mimesis.providers.path import Path, PurePosixPath, PureWindowsPath, PLATFORMS, USERNAMES, FOLDERS
import sys

# Test initialization with default platform (current system platform)
def test_init_default_platform():
    path = Path()
    assert path.platform == sys.platform

# Test initialization with specified 'linux' platform
def test_init_specified_linux():
    path = Path(platform='linux')
    assert path.platform == 'linux'
    assert isinstance(path._pathlib_home, PurePosixPath)

# Test initialization with specified 'win32' platform
def test_init_specified_win32():
    path = Path(platform='win32')
    assert path.platform == 'win32'
    assert isinstance(path._pathlib_home, PureWindowsPath)

# Test generating a random user for 'linux' platform
def test_user_linux():
    path = Path(platform='linux')
    user = path.user()
    assert isinstance(user, str)