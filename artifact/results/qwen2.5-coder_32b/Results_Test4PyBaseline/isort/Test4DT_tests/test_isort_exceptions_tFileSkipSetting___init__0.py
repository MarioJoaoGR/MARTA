# Module: isort.exceptions
import pytest
from isort.exceptions import FileSkipSetting

def test_file_skip_setting_with_valid_file_path():
    # Test with a valid file path
    file_path = '/path/to/skipped_file.py'
    with pytest.raises(FileSkipSetting) as excinfo:
        raise FileSkipSetting(file_path)
    assert str(excinfo.value) == f"{file_path} was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

def test_file_skip_setting_with_empty_string():
    # Test with an empty string as file path
    file_path = ''
    with pytest.raises(FileSkipSetting) as excinfo:
        raise FileSkipSetting(file_path)
    assert str(excinfo.value) == f"{file_path} was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

def test_file_skip_setting_with_relative_path():
    # Test with a relative file path
    file_path = './relative/path/to/skipped_file.py'
    with pytest.raises(FileSkipSetting) as excinfo:
        raise FileSkipSetting(file_path)
    assert str(excinfo.value) == f"{file_path} was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

def test_file_skip_setting_with_absolute_path():
    # Test with an absolute file path
    file_path = '/absolute/path/to/skipped_file.py'
    with pytest.raises(FileSkipSetting) as excinfo:
        raise FileSkipSetting(file_path)
    assert str(excinfo.value) == f"{file_path} was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

def test_file_skip_setting_with_special_characters():
    # Test with a file path containing special characters
    file_path = '/path/to/skipped_file@#.py'
    with pytest.raises(FileSkipSetting) as excinfo:
        raise FileSkipSetting(file_path)
    assert str(excinfo.value) == f"{file_path} was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"
