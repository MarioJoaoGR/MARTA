
import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_get_configuration_definitions_all(config_manager):
    # Test retrieving all configuration definitions without specific plugin type or name
    ret = config_manager.get_configuration_definitions()
    assert isinstance(ret, dict), "Expected a dictionary"
    assert len(ret) > 0, "Expected non-empty dictionary"

def test_get_configuration_definitions_by_type(config_manager):
    # Test retrieving configuration definitions by plugin type
    ret = config_manager.get_configuration_definitions(plugin_type='type')
    assert isinstance(ret, dict), "Expected a dictionary"