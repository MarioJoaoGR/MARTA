# Module: mimesis.providers.path
import pytest
from mimesis.providers import Path
import sys
from pathlib import PurePosixPath, PureWindowsPath

# Test initialization with default platform (current system platform)
def test_init_with_default_platform():
    path = Path()  # Uses the current system platform
    assert isinstance(path._pathlib_home, type(PurePosixPath()) if sys.platform == 'linux' else PureWindowsPath)

# Test initialization with specified platform
def test_init_with_specified_platform():
    path = Path(platform='win32')  # Explicitly specifies 'win32' platform
    assert isinstance(path._pathlib_home, PureWindowsPath)

# Test using user() method
def test_user_method():
    path = Path(platform='linux')
    user_path = path.user()
    assert isinstance(user_path, str)
    # Additional assertions to check the structure of the generated path for Linux
    assert '/home/' in user_path

# Test using dev_dir() method
def test_dev_dir_method():
    path = Path(platform='linux')
    dev_dir_path = path.dev_dir()
    assert isinstance(dev_dir_path, str)
    # Additional assertions to check the structure of the generated path for Linux
    assert '/home/' in dev_dir_path

# Test using project_dir() method
def test_project_dir_method():
    path = Path(platform='linux')
    project_dir_path = path.project_dir()
    assert isinstance(project_dir_path, str)
    # Additional assertions to check the structure of the generated path for Linux
    assert '/home/' in project_dir_path

# Test using user() method with win32 platform
def test_user_method_win32():
    path = Path(platform='win32')
    user_path = path.user()
    assert isinstance(user_path, str)
    # Additional assertions to check the structure of the generated path for Windows
    assert 'C:\\' in user_path or '/Users/' in user_path  # Adjust based on Windows home directory format

# Test using dev_dir() method with win32 platform
def test_dev_dir_method_win32():
    path = Path(platform='win32')
    dev_dir_path = path.dev_dir()
    assert isinstance(dev_dir_path, str)
    # Additional assertions to check the structure of the generated path for Windows
    assert 'C:\\' in dev_dir_path or '/Users/' in dev_dir_path  # Adjust based on Windows home directory format

# Test using project_dir() method with win32 platform
def test_project_dir_method_win32():
    path = Path(platform='win32')
    project_dir_path = path.project_dir()
    assert isinstance(project_dir_path, str)
    # Additional assertions to check the structure of the generated path for Windows
    assert 'C:\\' in project_dir_path or '/Users/' in project_dir_path  # Adjust based on Windows home directory format
