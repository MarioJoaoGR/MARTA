
from isort.exceptions import InvalidSettingsPath
import pytest

def test_invalid_input():
    with pytest.raises(InvalidSettingsPath) as excinfo:
        raise InvalidSettingsPath("some/invalid/path")
    
    assert str(excinfo.value) == (
        "isort was told to use the settings_path: some/invalid/path as the base directory or "
        "file that represents the starting point of config file discovery, but it does not exist."
    )
