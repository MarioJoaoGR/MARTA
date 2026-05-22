
import pytest
from unittest.mock import patch
from httpie.plugins.manager import PluginManager

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_plugin_manager_repr(plugin_manager):
    with patch('httpie.plugins.manager.PluginManager.__repr__', return_value='<PluginManager self>'):
        assert repr(plugin_manager) == '<PluginManager self>'
