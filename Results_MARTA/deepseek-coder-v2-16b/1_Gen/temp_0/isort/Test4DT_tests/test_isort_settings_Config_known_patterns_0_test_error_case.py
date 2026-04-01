
import pytest
from isort import Config
from isort.exceptions import InvalidSettingsPath, ProfileDoesNotExist, UnsupportedSettings

@pytest.mark.parametrize("invalid_config", [
    {"settings_file": "non_existent_file"},
    {"settings_path": "non_existent_directory"},
    {"profile": "nonexistent_profile"}
])
def test_error_case(invalid_config):
    with pytest.raises(Exception) as exc_info:
        Config(**invalid_config)
    
    assert isinstance(exc_info.value, (FileNotFoundError, ValueError)) or \
           isinstance(exc_info.value, (InvalidSettingsPath, ProfileDoesNotExist, UnsupportedSettings)), \
           f"Expected a FileNotFoundError or ValueError but got {type(exc_info.value)}"
