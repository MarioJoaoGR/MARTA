
import pytest
from isort.exceptions import InvalidSettingsPath
import os

def check_settings_path(path):
    if not os.path.exists(path):
        raise InvalidSettingsPath(path)

def test_invalid_settings_path_root_slash():
    """Test with '/' as the settings path, assuming it does not exist."""
    invalid_path = '/'
    try:
        check_settings_path(invalid_path)
    except InvalidSettingsPath as e:
        assert str(e) == f"isort was told to use the settings_path: {invalid_path} as the base directory or file that represents the starting point of config file discovery, but it does not exist."
        assert e.settings_path == invalid_path

def test_invalid_settings_path_current_directory_dot_slash():
    """Test with './' as the settings path, assuming it does not exist."""
    invalid_path = './'
    try:
        check_settings_path(invalid_path)
    except InvalidSettingsPath as e:
        assert str(e) == f"isort was told to use the settings_path: {invalid_path} as the base directory or file that represents the starting point of config file discovery, but it does not exist."
        assert e.settings_path == invalid_path

def test_invalid_settings_path_parent_directory_dot_dot_slash():
    """Test with '../' as the settings path, assuming it does not exist."""
    invalid_path = '../'
    try:
        check_settings_path(invalid_path)
    except InvalidSettingsPath as e:
        assert str(e) == f"isort was told to use the settings_path: {invalid_path} as the base directory or file that represents the starting point of config file discovery, but it does not exist."
        assert e.settings_path == invalid_path
