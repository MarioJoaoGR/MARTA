
import pytest
from mimesis.providers.path import Path
from pathlib import PureWindowsPath, PurePosixPath
import sys

# Test initialization with specified platform for Windows
@pytest.fixture(params=['win32'])
def path_instance_windows(request):
    return Path(platform=request.param)

# Test initialization with specified platform for Linux
@pytest.fixture(params=['linux'])
def path_instance_linux(request):
    return Path(platform=request.param)

# Test that the _pathlib_home attribute is PureWindowsPath for Windows platform
def test_valid_input_windows(path_instance_windows):
    assert isinstance(path_instance_windows._pathlib_home, PureWindowsPath)

# Test that the _pathlib_home attribute is PurePosixPath for Linux platform
def test_valid_input_linux(path_instance_linux):
    assert isinstance(path_instance_linux._pathlib_home, PurePosixPath)
