
import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

# Test case for when both plugin_type and name are provided
def test_get_configuration_definitions_by_type_and_name(config_manager):
    ret = config_manager.get_configuration_definitions(plugin_type='type', name='name')
    assert isinstance(ret, dict), "Expected a dictionary"