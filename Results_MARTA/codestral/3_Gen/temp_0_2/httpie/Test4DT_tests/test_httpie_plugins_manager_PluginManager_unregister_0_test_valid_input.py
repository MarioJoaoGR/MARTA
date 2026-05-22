
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

@pytest.fixture(autouse=True)
def setup_plugin_manager():
    with patch('httpie.plugins.manager.PluginManager') as MockPluginManager:
        manager = MockPluginManager.return_value
        yield manager

def test_valid_input(setup_plugin_manager):
    class MyPluginClass(BasePlugin):
        pass
    
    # Register the plugin temporarily for testing
    setup_plugin_manager.register(MyPluginClass)
    
    # Unregister the plugin
    setup_plugin_manager.unregister(MyPluginClass)
    
    # Check if the plugin is unregistered
    assert MyPluginClass not in setup_plugin_manager._plugins
