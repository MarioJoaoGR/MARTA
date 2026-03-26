
import pytest
from isort.settings import Config, UnsupportedSettings

def test_invalid_input():
    with pytest.raises(UnsupportedSettings):
        Config(config_overrides=None)
        Config(config_overrides=123)
        Config(config_overrides={})
        Config(config_overrides=[])
        Config(config_overrides=())
