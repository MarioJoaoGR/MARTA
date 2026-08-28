
import pytest
from ansible.config.data import ConfigData

# Test initialization of ConfigData class
def test_config_data_initialization():
    config = ConfigData()
    assert config._global_settings == {}