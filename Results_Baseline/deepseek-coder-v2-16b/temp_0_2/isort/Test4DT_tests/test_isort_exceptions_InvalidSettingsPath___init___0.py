# Module: isort.exceptions
import pytest

from isort.exceptions import InvalidSettingsPath


# Test cases for InvalidSettingsPath exception
def test_invalid_settings_path_non_existent_file():
    with pytest.raises(InvalidSettingsPath) as exc_info:
        raise InvalidSettingsPath("nonexistent_file.cfg")
    assert str(exc_info.value) == "isort was told to use the settings_path: nonexistent_file.cfg as the base directory or file that represents the starting point of config file discovery, but it does not exist."

def test_invalid_settings_path_non_existent_directory():
    with pytest.raises(InvalidSettingsPath) as exc_info:
        raise InvalidSettingsPath("nonexistent_directory/")
    assert str(exc_info.value) == "isort was told to use the settings_path: nonexistent_directory/ as the base directory or file that represents the starting point of config file discovery, but it does not exist."

def test_invalid_settings_path_valid_file():
    with pytest.raises(InvalidSettingsPath) as exc_info:
        raise InvalidSettingsPath("valid_config.cfg")
    assert str(exc_info.value) == "isort was told to use the settings_path: valid_config.cfg as the base directory or file that represents the starting point of config file discovery, but it does not exist."

def test_invalid_settings_path_valid_directory():
    with pytest.raises(InvalidSettingsPath) as exc_info:
        raise InvalidSettingsPath("valid_directory/")
    assert str(exc_info.value) == "isort was told to use the settings_path: valid_directory/ as the base directory or file that represents the starting point of config file discovery, but it does not exist."
