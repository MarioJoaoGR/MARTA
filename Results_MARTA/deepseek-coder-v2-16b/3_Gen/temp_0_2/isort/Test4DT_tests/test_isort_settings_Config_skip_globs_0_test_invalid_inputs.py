
import pytest
from isort.settings import Config
from isort.exceptions import UnsupportedSettings, InvalidSettingsPath, ProfileDoesNotExist, FormattingPluginDoesNotExist

def test_invalid_inputs():
    with pytest.raises(UnsupportedSettings):
        # Test initializing with invalid types for config_overrides
        Config(config_overrides={"quiet": "true"})
