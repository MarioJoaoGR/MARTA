# Module: isort.exceptions
import pytest
from isort.exceptions import FileSkipSetting

# Test case to check if the exception message includes the correct file path and reason
def test_file_skip_setting_with_correct_message():
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting("path/to/skipped_file")
    assert str(exc_info.value) == "path/to/skipped_file was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

# Test case to check if the exception can be instantiated with different file paths
def test_file_skip_setting_with_different_file_paths():
    file_paths = ["path/to/file1", "another/path/file2"]
    for path in file_paths:
        with pytest.raises(FileSkipSetting) as exc_info:
            raise FileSkipSetting(path)
        assert str(exc_info.value) == f"{path} was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

# Test case to check if the exception can be handled correctly with try-except block
def test_file_skip_setting_try_except():
    file_path = "path/to/handled_file"
    try:
        raise FileSkipSetting(file_path)
    except FileSkipSetting as e:
        assert str(e) == f"{file_path} was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"
