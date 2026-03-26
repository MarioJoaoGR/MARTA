
from isort.exceptions import InvalidSettingsPath
import pytest

def test_valid_input():
    settings_path = "some/valid/path"
    with pytest.raises(InvalidSettingsPath) as exc_info:
        raise InvalidSettingsPath(settings_path)
    
    assert str(exc_info.value) == (
        f"isort was told to use the settings_path: {settings_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not exist."
    )
