
import pytest
from mimesis.providers import Path
import sys
from pathlib import PurePosixPath, PureWindowsPath

# Test initialization with default platform
def test_init_default_platform():
    path = Path(platform=sys.platform)
    if 'win' in sys.platform:
        assert isinstance(path._pathlib_home, PureWindowsPath)
    else:
        assert isinstance(path._pathlib_home, PurePosixPath)

# Test initialization with specified platform
def test_init_specified_platform():
    path = Path(platform='win32')
    assert isinstance(path._pathlib_home, PureWindowsPath)
    path = Path(platform='linux')
    assert isinstance(path._pathlib_home, PurePosixPath)

# Test home method with default platform
def test_home_default_platform():
    path = Path(platform=sys.platform)
    if 'win' in sys.platform:
        expected_home = str(PureWindowsPath())
    else:
        expected_home = str(PurePosixPath())