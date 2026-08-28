
import pytest
from ansible.config.data import ConfigData

@pytest.fixture
def config():
    return ConfigData()

# Test setting and getting a global setting

# Test adding and getting a plugin

# Test getting a global setting without a plugin
def test_get_global_setting_without_plugin(config):
    with pytest.raises(AttributeError):
        config.set_global_setting('log_level', 'INFO')

# Test updating a global setting

# Test updating a plugin-specific setting
def test_update_plugin_specific_setting(config):
    with pytest.raises(AttributeError):
        config.add_plugin('logging', {'file': 'logs/app.log', 'level': 'INFO'})