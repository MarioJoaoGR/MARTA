# Module: isort.exceptions
import pytest

from isort.exceptions import InvalidSettingsPath


# Test case 1: Raising exception with an invalid file path
def test_invalid_settings_path_file():
    settings_path = "invalid/path/to/settings"
    with pytest.raises(InvalidSettingsPath) as exc_info:
        raise InvalidSettingsPath(settings_path)
    assert str(exc_info.value) == f"isort was told to use the settings_path: {settings_path} as the base directory or file that represents the starting point of config file discovery, but it does not exist."

# Test case 2: Raising exception with a non-existent directory path
def test_invalid_settings_path_directory():
    settings_path = "/nonexistent/directory"
    with pytest.raises(InvalidSettingsPath) as exc_info:
        raise InvalidSettingsPath(settings_path)
    assert str(exc_info.value) == f"isort was told to use the settings_path: {settings_path} as the base directory or file that represents the starting point of config file discovery, but it does not exist."

# Test case 3: Raising exception with an invalid file path (example using a variable)
def test_invalid_settings_path_variable():
    settings_path = "nonexistent/file.conf"
    with pytest.raises(InvalidSettingsPath) as exc_info:
        raise InvalidSettingsPath(settings_path)
    assert str(exc_info.value) == f"isort was told to use the settings_path: {settings_path} as the base directory or file that represents the starting point of config file discovery, but it does not exist."

# Test case 4: Raising exception with a non-existent file path
def test_invalid_settings_path_nonexistent_file():
    settings_path = "nonexistent/file.conf"
    with pytest.raises(InvalidSettingsPath) as exc_info:
        raise InvalidSettingsPath(settings_path)
    assert str(exc_info.value) == f"isort was told to use the settings_path: {settings_path} as the base directory or file that represents the starting point of config file discovery, but it does not exist."
