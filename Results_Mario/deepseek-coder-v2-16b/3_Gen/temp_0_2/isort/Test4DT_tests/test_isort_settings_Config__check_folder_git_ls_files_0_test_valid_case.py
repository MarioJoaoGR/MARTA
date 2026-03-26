
import pytest
from unittest.mock import patch, MagicMock
from isort.settings import Config, _Config, InvalidSettingsPath, ProfileDoesNotExist, UnsupportedSettings
from isort.exceptions import FormattingPluginDoesNotExist

@pytest.mark.parametrize("config_overrides", [
    {"quiet": True},
    {"settings_file": "path/to/valid/config.ini"},
    {"settings_path": "path/to/project"}
])
def test_valid_case(config_overrides):
    with patch('isort.settings._get_config_data', return_value={}), \
         patch('isort.settings._find_config', return_value=("path/to/project", {})), \
         patch('isort.settings.entry_points', return_value=[MagicMock(name='plugin1', load=lambda: {'formatter': 'mock'})]):
        try:
            config = Config(**config_overrides)
        except InvalidSettingsPath as e:
            assert str(e) == f"isort was told to use the settings_path: {config_overrides['settings_path']} as the base directory or file that represents the starting point of config file discovery, but it does not exist."
