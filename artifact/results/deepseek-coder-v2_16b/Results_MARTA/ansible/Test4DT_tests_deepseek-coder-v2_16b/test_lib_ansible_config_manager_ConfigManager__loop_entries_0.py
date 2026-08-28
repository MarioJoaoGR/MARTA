
import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_ConfigManager__loop_entries_basic(config_manager):
    container = {'log_level': 'INFO', 'max_connections': 10}
    entry_list = [{'name': 'log_level'}, {'name': 'max_connections'}]
    
    value, origin = config_manager._loop_entries(container, entry_list)
    
    assert value == 'INFO'
    assert origin == 'log_level'
