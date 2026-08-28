# Module: isort.exceptions
import pytest
from isort.exceptions import InvalidSettingsPath

def test_invalid_settings_path_with_absolute_path():
    path = "/nonexistent/directory/config.ini"
    with pytest.raises(InvalidSettingsPath) as excinfo:
        raise InvalidSettingsPath(path)
    assert str(excinfo.value) == (f"isort was told to use the settings_path: {path} "
                                  "as the base directory or file that represents the starting point of config file discovery, but it does not exist.")
    assert excinfo.value.settings_path == path

def test_invalid_settings_path_with_relative_path():
    path = "../config/nonexistent_config.yaml"
    with pytest.raises(InvalidSettingsPath) as excinfo:
        raise InvalidSettingsPath(path)
    assert str(excinfo.value) == (f"isort was told to use the settings_path: {path} "
                                  "as the base directory or file that represents the starting point of config file discovery, but it does not exist.")
    assert excinfo.value.settings_path == path

def test_invalid_settings_path_with_non_existent_file_in_existing_directory():
    existing_directory = "/usr/local/etc/"
    non_existent_file = f"{existing_directory}missing_config.json"
    with pytest.raises(InvalidSettingsPath) as excinfo:
        raise InvalidSettingsPath(non_existent_file)
    assert str(excinfo.value) == (f"isort was told to use the settings_path: {non_existent_file} "
                                  "as the base directory or file that represents the starting point of config file discovery, but it does not exist.")
    assert excinfo.value.settings_path == non_existent_file

def test_invalid_settings_path_with_empty_string():
    path = ""
    with pytest.raises(InvalidSettingsPath) as excinfo:
        raise InvalidSettingsPath(path)
    assert str(excinfo.value) == (f"isort was told to use the settings_path: {path} "
                                  "as the base directory or file that represents the starting point of config file discovery, but it does not exist.")
    assert excinfo.value.settings_path == path

def test_invalid_settings_path_with_whitespace():
    path = "   "
    with pytest.raises(InvalidSettingsPath) as excinfo:
        raise InvalidSettingsPath(path)
    assert str(excinfo.value) == (f"isort was told to use the settings_path: {path} "
                                  "as the base directory or file that represents the starting point of config file discovery, but it does not exist.")
    assert excinfo.value.settings_path == path
