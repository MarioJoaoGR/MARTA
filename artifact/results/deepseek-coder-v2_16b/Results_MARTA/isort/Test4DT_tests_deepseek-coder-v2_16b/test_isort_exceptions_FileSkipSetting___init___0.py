
import pytest
from isort.exceptions import FileSkipSetting

# Test for valid input scenario
def test_valid_input():
    # Setup: Real instance of FileSkipSetting with a valid file path
    file_path = "example/valid/file.py"
    try:
        raise FileSkipSetting(file_path)
    except FileSkipSetting as e:
        assert str(e) == f"{file_path} was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

# Test for handling None input scenario
def test_edge_case_none():
    # Setup: None
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting(None)
    assert str(exc_info.value) == "None was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

# Test for raising ValueError with invalid file path scenario
def test_invalid_input():
    # Setup: Real instance of FileSkipSetting with an invalid file path
    file_path = "invalid/file.py"
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting(file_path)
    assert str(exc_info.value) == f"{file_path} was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"
